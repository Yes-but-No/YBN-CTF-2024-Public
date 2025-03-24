import base64
import pickle


class SaveState:
    def __init__(self, name: str, farmed: int):
        self.name = name
        self.farmed = farmed


state = SaveState("test", 10**15)

state_bytes = pickle.dumps(state)
print(state_bytes)
state_b64 = base64.b64encode(state_bytes).decode("utf-8")
print(state_b64)
