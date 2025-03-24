First, use a string format vulnerability in the generate_response function to get the secret key of the application
```json
{"command":"yes {response.__init__.__globals__[app].secret_key}"}
```

Then, set the uuid to an invalid UUID. You can then use the secret key to sign a new UUID and set it to the uuid parameter in the session cookie. This will cause the key returned to be "None" instead of the actual key used to sign. You can then sign you own jwt with this key and set the admin value to be true. Refer to solution.py for this.