import hmac
import pickle
import pickletools
from hashlib import sha256
from io import BytesIO

with open("SECRET_KEY", "rb") as f:
    SECRET_KEY = f.read()


class SaveUnpickler(pickle.Unpickler):
    def find_class(self, module: str, name: str):
        if (
            module == "__main__"
            and name.count(".") <= 1
            and "save" in name.lower()
            and len(name) <= 19
        ):
            return super().find_class(module, name)

        raise pickle.UnpicklingError("Dangerous pickle detected")


def save(state: object):
    state_bytes = pickle.dumps(state)
    state_signature = hmac.new(SECRET_KEY, state_bytes, sha256).hexdigest()
    return f"{state_bytes.hex()}.{state_signature}"


def load(state_signed: str):
    if state_signed.count(".") != 1:
        print("Invalid save format detected")
        return None

    state_bytes, state_signature = state_signed.split(".")
    state_bytes = bytes.fromhex(state_bytes)
    state_signature = bytes.fromhex(state_signature)
    loaded_signature = hmac.new(SECRET_KEY, state_bytes, sha256).digest()

    for op, _, _ in pickletools.genops(state_bytes):
        if op.code == "R":
            print("Disallowed opcode in save!")
            return None

    try:
        save_state = SaveUnpickler(BytesIO(state_bytes)).load()
    except pickle.UnpicklingError:
        print("Dangerous pickle detected")
        return None

    if hmac.compare_digest(state_signature, loaded_signature):
        return save_state
    else:
        print("Invalid save signature!")
        return None
