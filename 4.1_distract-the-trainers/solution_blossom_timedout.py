""" BillyLjm, 2023
=====================
Distract the Trainers
=====================

The time for the mass escape has come, and you need to distract the bunny
trainers so that the workers can make it out! Unfortunately for you, they're
watching the bunnies closely. Fortunately, this means they haven't realized yet
that the space station is about to explode due to the destruction of the
LAMBCHOP doomsday device. Also fortunately, all that time you spent working as
first a minion and then a henchman means that you know the trainers are fond of
bananas. And gambling. And thumb wrestling.

The bunny trainers, being bored, readily accept your suggestion to play the
Banana Games.

You will set up simultaneous thumb wrestling matches. In each match, two
trainers will pair off to thumb wrestle. The trainer with fewer bananas will bet
all their bananas, and the other trainer will match the bet. The winner will
receive all of the bet bananas. You don't pair off trainers with the same number
of bananas (you will see why, shortly). You know enough trainer psychology to
know that the one who has more bananas always gets over-confident and loses.
Once a match begins, the pair of trainers will continue to thumb wrestle and
exchange bananas, until both of them have the same number of bananas. Once that
happens, both of them will lose interest and go back to supervising the bunny
workers, and you don't want THAT to happen!

For example, if the two trainers that were paired started with 3 and 5 bananas,
after the first round of thumb wrestling they will have 6 and 2 (the one with 3
bananas wins and gets 3 bananas from the loser). After the second round, they
will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they
stop and get back to training bunnies.

How is all this useful to distract the bunny trainers? Notice that if the
trainers had started with 1 and 4 bananas, then they keep thumb wrestling!
1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the trainers in such a way that the
maximum number of trainers go into an infinite thumb wrestling loop!

Write a function solution(banana_list) which, given a list of positive integers
depicting the amount of bananas the each trainer starts with, returns the fewest
possible number of bunny trainers that will be left to watch the workers.
Element i of the list will be the number of bananas that trainer i (counting
from 0) starts with.

The number of trainers will be at least 1 and not more than 100, and the number
of bananas each trainer starts with will be a positive integer no more than
1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

=============
Author's Note
=============
As noted below, this version uses the RobertDurfee's well-written Blossom
algorithm to pair the trainers up to maximise the looping games. This should
guarantee an optimal pairing in a relatively efficient manner.

However, it still timed out on Google's private test cases. And I don't know
of any algorithm that is faster than Blossom algorithm. So, I ended up using
a (non-guaranteed?) greedy pairing in the other file that passed.
"""

"""
================================
RobertDurfee's Blossom algorithm
================================
The big chunk of code below is copied from RobertDurfee at
https://github.com/RobertDurfee/Blossom/blob/master/blossom.py#L1
"""
# https://en.wikipedia.org/wiki/Blossom_algorithm
def get_maximum_matching(graph, matching):
    augmenting_path = get_augmenting_path(graph, matching)
    if len(augmenting_path) > 0:
        return get_maximum_matching(graph, matching.augment(augmenting_path))
    else:
        return matching

# https://en.wikipedia.org/wiki/Blossom_algorithm
def get_augmenting_path(graph, matching):
    forest = Forest()
    graph.unmark_all_edges()
    graph.mark_edges(matching.get_edges())
    for exposed_vertice in matching.get_exposed_vertices():
        forest.add_singleton_tree(exposed_vertice)
    v = forest.get_unmarked_even_vertice()
    while v is not None:
        e = graph.get_unmarked_neighboring_edge(v)
        while e is not None:
            _, w = e
            if not forest.does_contain_vertice(w):
                x = matching.get_matched_vertice(w)
                forest.add_edge((v, w))
                forest.add_edge((w, x))
            else:
                if forest.get_distance_to_root(w) % 2 != 0:
                    pass
                else:
                    if forest.get_root(v) != forest.get_root(w):
                        path = forest.get_path_from_root_to(v) + forest.get_path_to_root_from(w)
                        return path
                    else:
                        blossom = forest.get_blossom(v, w)
                        graph_prime = graph.contract(blossom)
                        matching_prime = matching.contract(blossom)
                        path_prime = get_augmenting_path(graph_prime, matching_prime)
                        path = graph.lift_path(path_prime, blossom)
                        return path
            graph.mark_edge(e)
            e = graph.get_unmarked_neighboring_edge(v)
        forest.mark_vertice(v)
        v = forest.get_unmarked_even_vertice()
    return []

class Graph:

    def __init__(self):
        self.adjacency = {}
        self.unmarked_adjacency = {}
        self.__assert_representation()

    def __assert_representation(self):
        for t in self.adjacency:
            assert len(self.adjacency[t]) > 0, 'If vertice exists in adjacency matrix, it must have at least one neighbor'
            for u in self.adjacency[t]:
                self.__assert_edge_exists((t, u))
        for t in self.unmarked_adjacency:
            assert len(self.unmarked_adjacency[t]) > 0, 'If vertice exists in unmarked adjacency matrix, it must have at least one neighbor'
            for u in self.unmarked_adjacency[t]:
                self.__assert_edge_exists((t, u))
                self.__assert_unmarked_edge_exists((t, u))

    def __assert_edge_exists(self, edge):
        v, w = edge
        assert (v in self.adjacency) and (w in self.adjacency[v]), 'Edge must exist in adjacency matrix'
        assert (w in self.adjacency) and (v in self.adjacency[w]), 'Reciprocal edge must exist in adjacency matrix'

    def __assert_edge_does_not_exist(self, edge):
        v, w = edge
        assert (v not in self.adjacency) or (w not in self.adjacency[v]), 'Edge must not exist in adjacency matrix'
        assert (w not in self.adjacency) or (v not in self.adjacency[w]), 'Reciprocal edge must not exist in adjacency matrix'

    def __assert_unmarked_edge_exists(self, edge):
        v, w = edge
        assert (v in self.unmarked_adjacency) and (w in self.unmarked_adjacency[v]), 'Edge must exist in unmarked adjacency matrix'
        assert (w in self.unmarked_adjacency) and (v in self.unmarked_adjacency[w]), 'Reciprocal edge must exist in unmarked adjacency matrix'

    def __assert_unmarked_edge_does_not_exist(self, edge):
        v, w = edge
        assert (v not in self.unmarked_adjacency) or (w not in self.unmarked_adjacency[v]), 'Edge must not exist in unmarked adjacency matrix'
        assert (w not in self.unmarked_adjacency) or (v not in self.unmarked_adjacency[w]), 'Reciprocal edge must not exist in unmarked adjacency matrix'

    def __assert_vertice_exists(self, vertice):
        assert vertice in self.adjacency, 'Vertice must exist in adjacency matrix'

    def __assert_vertice_does_not_exist(self, vertice):
        assert vertice not in self.adjacency, 'Vertice must not exist in adjacency matrix'
        assert vertice not in self.unmarked_adjacency, 'Vertice must not exist in unmarked adjacency matrix'

    def copy(self):
        self.__assert_representation()
        graph = Graph()
        for t in self.adjacency:
            graph.adjacency[t] = set()
            for u in self.adjacency[t]:
                graph.adjacency[t].add(u)
        for t in self.unmarked_adjacency:
            graph.unmarked_adjacency[t] = set()
            for u in self.unmarked_adjacency[t]:
                graph.unmarked_adjacency[t].add(u)
        graph.__assert_representation()
        return graph

    def add_edge(self, edge):
        self.__assert_edge_does_not_exist(edge)
        self.__assert_unmarked_edge_does_not_exist(edge)
        v, w = edge
        if v not in self.adjacency:
            self.adjacency[v] = set()
        self.adjacency[v].add(w)
        if w not in self.adjacency:
            self.adjacency[w] = set()
        self.adjacency[w].add(v)
        if v not in self.unmarked_adjacency:
            self.unmarked_adjacency[v] = set()
        self.unmarked_adjacency[v].add(w)
        if w not in self.unmarked_adjacency:
            self.unmarked_adjacency[w] = set()
        self.unmarked_adjacency[w].add(v)
        self.__assert_representation()

    def unmark_all_edges(self):
        self.unmarked_adjacency = {}
        for t in self.adjacency:
            self.unmarked_adjacency[t] = set()
            for u in self.adjacency[t]:
                self.unmarked_adjacency[t].add(u)
        self.__assert_representation()

    def mark_edges(self, edges):
        for edge in edges:
            self.mark_edge(edge)
        self.__assert_representation()

    def mark_edge(self, edge):
        self.__assert_edge_exists(edge)
        self.__assert_unmarked_edge_exists(edge)
        v, w = edge
        self.unmarked_adjacency[v].remove(w)
        if len(self.unmarked_adjacency[v]) == 0:
            del self.unmarked_adjacency[v]
        self.unmarked_adjacency[w].remove(v)
        if len(self.unmarked_adjacency[w]) == 0:
            del self.unmarked_adjacency[w]
        self.__assert_representation()

    def get_unmarked_neighboring_edge(self, vertice):
        self.__assert_representation()
        if vertice in self.unmarked_adjacency:
            return vertice, next(iter(self.unmarked_adjacency[vertice]))
        else:
            return None

    def get_vertices(self):
        self.__assert_representation()
        return self.adjacency.keys()

    def contract(self, blossom):
        graph = self.copy()
        graph.__assert_vertice_does_not_exist(blossom.get_id())
        graph.adjacency[blossom.get_id()] = set()
        for t in blossom.get_vertices():
            graph.__assert_vertice_exists(t)
            for u in graph.adjacency[t]:
                graph.__assert_edge_exists((t, u))
                graph.adjacency[u].remove(t)
                if u != blossom.get_id():
                    graph.adjacency[blossom.get_id()].add(u)
                    graph.adjacency[u].add(blossom.get_id())
            del graph.adjacency[t]
        if len(graph.adjacency[blossom.get_id()]) == 0:
            # Required to maintain invariant
            del graph.adjacency[blossom.get_id()]
        graph.unmark_all_edges()
        graph.__assert_representation()
        return graph

    def lift_path(self, path, blossom):
        self.__assert_representation()
        if len(path) == 0:
            return path
        if len(path) == 1:
            assert False, 'A path cannot contain exactly one vertice'
        if path[0] == blossom.get_id():

            ############################################################################################################
            # LEFT ENDPOINT
            ############################################################################################################

            #  ,-o                    #    b                    #    o--,
            # |      b  o--o  o--o  o #        o  o--o  o--o  o #        o  o--o  o--o  o
            # o                       # o      |                # b
            #        o                # |      o                #        o
            #    o--'                 #  `-o                    #    o--'

            #  ,-o                    #    o--,
            # |      o  o--o  o--o  o #        o  o--o  o--o  o
            # o      |                # o
            #        o                # |      b
            #    b                    #  `-o

            w = path[1]
            blossom_path = []
            for v in blossom.traverse_left():
                blossom_path.append(v)
                if (w in self.adjacency[v]) and (len(blossom_path) % 2 != 0):
                    return blossom_path + path[1:]
            blossom_path = []
            for v in blossom.traverse_right():
                blossom_path.append(v)
                if (w in self.adjacency[v]) and (len(blossom_path) % 2 != 0):
                    return blossom_path + path[1:]
            assert False, 'At least one path with even edges must exist through the blossom'
        if path[-1] == blossom.get_id():

            ############################################################################################################
            # RIGHT ENDPOINT
            ############################################################################################################

            #                    o-.  #                    b    #                 ,--o
            # o  o--o  o--o  b      | # o  o--o  o--o  o        # o  o--o  o--o  o
            #                       o #                |      o #                       b
            #                o        #                o      | #                o
            #                 `--o    #                    o-'  #                 `--o

            #                    o-.  #                 ,--o
            # o  o--o  o--o  o      | # o  o--o  o--o  o
            #                |      o #                       o
            #                o        #                b      |
            #                    b    #                    o-'

            u = path[-2]
            blossom_path = []
            for v in blossom.traverse_left():
                blossom_path.append(v)
                if (u in self.adjacency[v]) and (len(blossom_path) % 2 != 0):
                    return path[:-1] + list(reversed(blossom_path))
            blossom_path = []
            for v in blossom.traverse_right():
                blossom_path.append(v)
                if (u in self.adjacency[v]) and (len(blossom_path) % 2 != 0):
                    return path[:-1] + list(reversed(blossom_path))
            assert False, 'At least one path with even edges must exist through the blossom'
        for i, v in enumerate(path):
            if v == blossom.get_id():
                u, w = path[i-1], path[i+1]
                if u in self.adjacency[blossom.get_base()]:

                    ####################################################################################################
                    # INTERIOR LEFT-ORIENTED BLOSSOM
                    ####################################################################################################

                    #            o     #                         #                         #          o--,
                    #                  #                         #                         #              o
                    #            o     #                         #                         # o  o--b
                    #            |     #          o--,           #          o--,           #              o
                    #            o     #              o  o--o  o #              o          #          o--'
                    #                  # o  o--b                 # o  o--b                 #
                    #            o--,  #              o          #              o  o--o  o #          o
                    #                o #          o--'           #          o--'           #          |
                    #   o  o--b        #                         #                         #          o
                    #                o #                         #                         #
                    #            o--'  #                         #                         #          o

                    blossom_path = []
                    for v in blossom.traverse_left():
                        blossom_path.append(v)
                        if (w in self.adjacency[v]) and (len(blossom_path) % 2 != 0):
                            return path[:i] + blossom_path + path[i+1:]
                    blossom_path = []
                    for v in blossom.traverse_right():
                        blossom_path.append(v)
                        if (w in self.adjacency[v]) and (len(blossom_path) % 2 != 0):
                            return path[:i] + blossom_path + path[i+1:]
                    assert False, 'At least one path with even edges must exist through the blossom'
                elif w in self.adjacency[blossom.get_base()]:

                    ####################################################################################################
                    # INTERIOR RIGHT-ORIENTED BLOSSOM
                    ####################################################################################################

                    #       o          #                         #                         #  ,--o
                    #                  #                         #                         # o
                    #       o          #                         #                         #        b--o  o
                    #       |          #           ,--o          #           ,--o          # o
                    #       o          # o  o--o  o              #          o              #  `--o
                    #                  #                 b--o  o #                 b--o  o #
                    #    ,--o          #          o              # o  o--o  o              #     o
                    #   o              #           `--o          #           `--o          #     |
                    #          b--o  o #                         #                         #     o
                    #   o              #                         #                         #
                    #    `--o          #                         #                         #     o

                    blossom_path = []
                    for v in blossom.traverse_left():
                        blossom_path.append(v)
                        if (u in self.adjacency[v]) and (len(blossom_path) % 2 != 0):
                            return path[:i] + list(reversed(blossom_path)) + path[i+1:]
                    blossom_path = []
                    for v in blossom.traverse_right():
                        blossom_path.append(v)
                        if (u in self.adjacency[v]) and (len(blossom_path) % 2 != 0):
                            return path[:i] + list(reversed(blossom_path)) + path[i+1:]
                    assert False, 'At least one path with even edges must exist through the blossom'
                else:
                    assert False, 'Exactly one side of the path must be incident to the base of the blossom'
        return path

class Matching:

    def __init__(self):
        self.adjacency = {}
        self.edges = set()
        self.exposed_vertices = set()
        self.__assert_representation()

    def __assert_representation(self):
        for t in self.adjacency:
            self.__assert_vertice_exists(t)
            if len(self.adjacency[t]) == 0:
                self.__assert_vertice_is_exposed(t)
            else:
                self.__assert_vertice_is_not_exposed(t)
                u = next(iter(self.adjacency[t]))
                self.__assert_edge_exists(tuple(sorted((t, u))))
                self.__assert_vertice_is_not_exposed(u)

    def __assert_edge_exists(self, edge):
        v, w = edge
        assert (v in self.adjacency) and (w in self.adjacency[v]), 'Edge must exist in adjacency matrix'
        assert (w in self.adjacency) and (v in self.adjacency[w]), 'Reciprocal edge must exist in adjacency matrix'
        assert edge in self.edges, 'Edge must exist in edges set'

    def __assert_edge_does_not_exist(self, edge):
        v, w = edge
        assert (v not in self.adjacency) or (w not in self.adjacency[v]), 'Edge must not exist in adjacency matrix'
        assert (w not in self.adjacency) or (v not in self.adjacency[w]), 'Reciprocal edge must not exist in adjacency matrix'
        assert edge not in self.edges, 'Edge must not exist in edges set'

    def __assert_vertice_is_exposed(self, vertice):
        assert vertice in self.adjacency, 'Vertice must exist in adjacency matrix'
        assert vertice in self.exposed_vertices, 'Vertice must exist in exposed vertices set'
        assert len(self.adjacency[vertice]) == 0, 'Vertice must have no neighbors'

    def __assert_vertice_is_not_exposed(self, vertice):
        assert vertice in self.adjacency, 'Vertice must exist in adjacency matrix'
        assert vertice not in self.exposed_vertices, 'Vertice must not exist in exposed vertices set'
        assert len(self.adjacency[vertice]) == 1, 'Vertice must have exactly one neighbor'

    def __assert_vertice_exists(self, vertice):
        assert vertice in self.adjacency, 'Vertice must exist in adjacency matrix'
        if vertice in self.exposed_vertices:
            assert len(self.adjacency[vertice]) == 0, 'If vertice is exposed, it must have no neighbors'
        else:
            assert len(self.adjacency[vertice]) == 1, 'If vertice is not exposed, it must have exactly one neighbor'

    def __assert_vertice_does_not_exist(self, vertice):
        assert vertice not in self.adjacency, 'Vertice must not exist in adjacency matrix'
        assert vertice not in self.exposed_vertices, 'Vertice must not be exposed'

    def copy(self):
        self.__assert_representation()
        matching = Matching()
        for t in self.adjacency.keys():
            matching.adjacency[t] = set()
            for u in self.adjacency[t]:
                matching.adjacency[t].add(u)
        for e in self.edges:
            matching.edges.add(e)
        for u in self.exposed_vertices:
            matching.exposed_vertices.add(u)
        matching.__assert_representation()
        return matching

    def augment(self, path):
        matching = self.copy()
        matching.__assert_vertice_is_exposed(path[0])
        matching.__assert_vertice_is_exposed(path[-1])
        matching.exposed_vertices.remove(path[0])
        matching.exposed_vertices.remove(path[-1])
        for i in range(len(path)-1):
            v, w = path[i], path[i+1]
            edge = tuple(sorted((v, w)))
            if edge in matching.edges:
                matching.__assert_edge_exists(edge)
                matching.edges.remove(edge)
                matching.adjacency[v].remove(w)
                matching.adjacency[w].remove(v)
            else:
                matching.__assert_edge_does_not_exist(edge)
                matching.edges.add(edge)
                matching.adjacency[v].add(w)
                matching.adjacency[w].add(v)
        matching.__assert_representation()
        return matching

    def get_edges(self):
        self.__assert_representation()
        return self.edges

    def get_exposed_vertices(self):
        self.__assert_representation()
        return self.exposed_vertices

    def get_matched_vertice(self, vertice):
        self.__assert_representation()
        self.__assert_vertice_is_not_exposed(vertice)
        return next(iter(self.adjacency[vertice]))

    def add_vertices(self, vertices):
        for vertice in vertices:
            self.add_vertice(vertice)
        self.__assert_representation()

    def add_vertice(self, vertice):
        self.__assert_vertice_does_not_exist(vertice)
        self.adjacency[vertice] = set()
        self.exposed_vertices.add(vertice)
        self.__assert_representation()

    def contract(self, blossom):
        matching = self.copy()
        matching.__assert_vertice_does_not_exist(blossom.get_id())
        matching.adjacency[blossom.get_id()] = set()
        if blossom.get_base() in matching.exposed_vertices:
            matching.exposed_vertices.add(blossom.get_id())
        for t in blossom.get_vertices():
            matching.__assert_vertice_exists(t)
            for u in matching.adjacency[t]:
                e = tuple(sorted((t, u)))
                matching.__assert_edge_exists(e)
                matching.edges.remove(e)
                matching.adjacency[u].remove(t)
                if u != blossom.get_id():
                    matching.edges.add(tuple(sorted((blossom.get_id(), u))))
                    matching.adjacency[blossom.get_id()].add(u)
                    matching.adjacency[u].add(blossom.get_id())
            del matching.adjacency[t]
            matching.exposed_vertices.discard(t)
        matching.__assert_representation()
        return matching

class Forest:

    def __init__(self):
        self.roots = {}
        self.distances_to_root = {}
        self.unmarked_even_vertices = set()
        self.parents = {}
        self.__assert_representation()

    def __assert_representation(self):
        for vertice in self.roots:
            self.__assert_vertice_exists(vertice)
        assert self.roots.keys() == self.distances_to_root.keys(), 'Roots and distances to root must have same keys'
        assert self.roots.keys() == self.parents.keys(), 'Roots and parents mut have same keys'
        for vertice in self.unmarked_even_vertices:
            self.__assert_vertice_exists(vertice)
            assert self.distances_to_root[vertice] % 2 == 0, 'Unmarked even vertice must have even distance to root'

    def __assert_vertice_exists(self, vertice):
        assert vertice in self.roots, 'Vertice must have a root'
        assert vertice in self.distances_to_root, 'Vertice must have a distance to root'
        assert vertice in self.parents, 'Vertice must have a parent'

    def __assert_vertice_does_not_exist(self, vertice):
        assert vertice not in self.roots, 'Vertice must not have a root'
        assert vertice not in self.distances_to_root, 'Vertice must not have a distance to root'
        assert vertice not in self.unmarked_even_vertices, 'Vertice must not exist in unmarked even vertices set'
        assert vertice not in self.parents, 'Vertice must not have a parent'

    def add_singleton_tree(self, vertice):
        self.__assert_vertice_does_not_exist(vertice)
        self.roots[vertice] = vertice
        self.distances_to_root[vertice] = 0
        self.unmarked_even_vertices.add(vertice)
        self.parents[vertice] = vertice
        self.__assert_representation()

    def get_unmarked_even_vertice(self):
        self.__assert_representation()
        if len(self.unmarked_even_vertices) > 0:
            return next(iter(self.unmarked_even_vertices))
        else:
            return None

    def mark_vertice(self, vertice):
        self.__assert_vertice_exists(vertice)
        if self.distances_to_root[vertice] % 2 == 0:
            assert vertice in self.unmarked_even_vertices, 'If vertice has an even distance to root, it must exist in unmarked even vertices set'
            self.unmarked_even_vertices.remove(vertice)
        self.__assert_representation()

    def does_contain_vertice(self, vertice):
        self.__assert_representation()
        return vertice in self.roots

    def add_edge(self, edge):
        v, w = edge
        if v not in self.roots:
            self.__assert_vertice_does_not_exist(v)
            self.__assert_vertice_exists(w)
            self.roots[v] = self.roots[w]
            self.distances_to_root[v] = 1 + self.distances_to_root[w]
            if self.distances_to_root[v] % 2 == 0:
                self.unmarked_even_vertices.add(v)
            self.parents[v] = w
        elif w not in self.roots:
            self.__assert_vertice_does_not_exist(w)
            self.__assert_vertice_exists(v)
            self.roots[w] = self.roots[v]
            self.distances_to_root[w] = 1 + self.distances_to_root[v]
            if self.distances_to_root[w] % 2 == 0:
                self.unmarked_even_vertices.add(w)
            self.parents[w] = v
        else:
            assert False, 'At least one incident vertice must not already exist'
        self.__assert_representation()

    def get_distance_to_root(self, vertice):
        self.__assert_representation()
        self.__assert_vertice_exists(vertice)
        return self.distances_to_root[vertice]

    def get_root(self, vertice):
        self.__assert_representation()
        self.__assert_vertice_exists(vertice)
        return self.roots[vertice]

    def get_path_from_root_to(self, vertice):
        self.__assert_representation()
        return list(reversed(self.get_path_to_root_from(vertice)))

    def get_path_to_root_from(self, vertice):
        self.__assert_representation()
        self.__assert_vertice_exists(vertice)
        root = self.roots[vertice]
        path = []
        parent = vertice
        while parent != root:
            path.append(parent)
            parent = self.parents[parent]
        path.append(root)
        assert len(set(path)) == len(path), 'Path to root must not contain any duplicate vertices'
        return path

    def get_blossom(self, v, w):
        self.__assert_representation()
        v_path = self.get_path_to_root_from(v)
        w_path = self.get_path_to_root_from(w)
        w_ancestors = set(w_path)
        v_blossom_vertices = []
        common_ancestor = None
        for u in v_path:
            if u in w_ancestors:
                common_ancestor = u
                break
            else:
                v_blossom_vertices.append(u)
        assert common_ancestor is not None, 'Common ancestor must exist'
        w_blossom_vertices = []
        for u in w_path:
            if u == common_ancestor:
                break
            else:
                w_blossom_vertices.append(u)
        blossom_vertices = [common_ancestor] + list(reversed(v_blossom_vertices)) + w_blossom_vertices
        assert len(set(blossom_vertices)) == len(blossom_vertices), 'Blossom must not contain any duplicate vertices'
        assert len(blossom_vertices) % 2 != 0, 'Blossom must contain an odd number of vertices'
        blossom = Blossom(blossom_vertices, common_ancestor)
        return blossom

class Blossom:

    count = 0

    def __init__(self, vertices, base):
        Blossom.count += 1
        self.id = -Blossom.count
        self.vertices = vertices
        self.base = base
        self.__assert_representation()

    def __assert_representation(self):
        assert self.vertices[0] == self.base, 'Blossom must begin with base vertice'
        assert len(self.vertices) % 2 != 0, 'Blossom must have an odd number of vertices'
        assert len(self.vertices) >= 3, 'Blossom must have at least three vertices'

    def get_id(self):
        self.__assert_representation()
        return self.id

    def get_vertices(self):
        self.__assert_representation()
        return self.vertices

    def get_base(self):
        self.__assert_representation()
        return self.base

    def traverse_right(self):
        self.__assert_representation()
        for vertice in self.vertices:
            yield vertice

    def traverse_left(self):
        self.__assert_representation()
        for vertice in reversed(self.vertices[1:] + self.vertices[:1]):
            yield vertice

"""
===========
My Solution
===========
Now, building on RobertDurfee's hard work, I can solve Google's foobar challenge!
"""
import math

def findGCD(l, s):
    """Euclid's algorithm for greatest common denominator"""
    if l < s:
        l, s = s, l
    while s:
        l, s = s, l%s
    return l

def solution(banana_list):
    """
    The game essentially pulls the proportion of bananas owned by
    each player towards 50/50. The larger proportion donates to the
    smaller one until the 50/50 mark is crossed, then the direction
    reverses. Thereafter, the proportion goes back and forth across
    the 50/50 mark. If it reaches the 50/50 mark eventually, the
    game will end in the next step. Or the game can also oscillate
    indefinitely about the 50/50 mark.

    In fact, there is only one oscillation trajectory which leads
    to the 50/50 mark and the game ending. In the penultimate step,
    the players have to reach a distribution of 1/2-1/2, and before
    that 1/4-3/4, and before 3/8-5/8, and 5/16-11/16, and so on.

    Analysing the patten, it can be seen that the denominator will
    be 2^n, and the numerator will be \abs[\sum_{i=0}^n (-2)^{i}].
    So we can check for this very easily by calculating n from the
    denominator, then calculating what the numerator has to be.

    Note that we still have to simulate the game until a reversal
    happens. And if sum of all banana's is odd, its an easy loop.

    ---

    Now we know how to determine the outcome of the game, but how
    do we pair the trainers up to maximise the number of looping
    games? This pairing could be viewed as a maximum cardinality
    matching problem, where we want to maximise the number of
    matched edges/looping games. A well-known algorithm to tackle
    this problem is the Blossom algorithm, which I'll implement.

    https://algorithms.discrete.ma.tum.de/graph-algorithms/matchings-blossom-algorithm/index_en.html

    The Blossom algorithm writing is a little involved; see the
    code I copied above. So I'll use a well-written implementation
    I found on Github :)
    """

    ntrain = len(banana_list)

    # construct graph for Blossom algorithm
    graph = Graph()
    for i in range(ntrain):
        for j in range(i, ntrain):
            # if sum of bananas odd, it'll loop forver
            if (banana_list[i] + banana_list[j]) % 2 == 1:
                graph.add_edge((i,j))
                continue
            # simulate game up to reversal
            num1, num2 = banana_list[i], banana_list[j]
            if num1 < num2:
                num1, num2 = num2, num1
            while num1 > num2:
                num1 -= num2
                num2 *= 2
            # find state as fraction of total bananas
            gcd = findGCD(num1, num2)
            num1 = num1 / gcd
            num2 = num2 / gcd
            denom = num1 + num2
            # if denominator != 2^n, it'll loop forever
            n = math.log(denom, 2)
            if not n.is_integer():
                graph.add_edge((i,j))
                continue
            # else check if num1, num2 are looping (for denom)
            num = 0
            for k in range(int(n)):
                num += (-2)**k
            if num1 != abs(num) and num2 != abs(num):
                graph.add_edge((i,j))
                continue

    # Blossom algorithm
    matching = Matching()
    matching.add_vertices(graph.get_vertices())
    matches = get_maximum_matching(graph, matching).edges

    return ntrain - 2 * len(matches)

print(solution([1,1]))

print(solution([1, 7, 3, 21, 13, 19]))
