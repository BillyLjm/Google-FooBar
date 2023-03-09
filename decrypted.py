import base64

MESSAGE = '''
OU4fGRpNKTk+ZUlWTF5JPi8sNk5ATF5NIyYhJwgLGRwJbHBtZQwfGBxLIS8pZUVMSxxIKiU/NhpL TEM
OayMjIRsJCBBMIC9qbklLDRpGJS87JwQJAg0JbHBtZRwCABZNJy8pZUVMSwtPLigkNhpLTEMO azksJA
xLQFkJKiUiZUlWTF5ZJSRsZRQ=
'''

KEY = 'Billy.LJM'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
