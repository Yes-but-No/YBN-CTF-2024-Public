from hashlib import sha256
from secrets import token_bytes
from string import printable

CHOICE_MESSAGE = """Homebrewed HMAC
1. Sign Message
2. Verify Message
3. Exit
"""


def sign(message: bytes, secret: bytes) -> str:
    return sha256(secret + message).hexdigest()


def verify(signed: str, secret: bytes) -> str | bool:
    try:
        message, signature = signed.split(".")
        message = bytes.fromhex(message)
        if sign(message, secret) == signature:
            message = message.decode(errors="ignore")
            return "".join([c for c in message if c in printable])
        else:
            return False
    except BaseException as e:
        print(e)
        return False


def main():
    SECRET = token_bytes(32)
    PASSPHRASE = "Yes, but no, but yes, but no."

    while True:
        print(CHOICE_MESSAGE)
        choice = input("> ")

        if choice == "1":
            message = input("Enter message to sign: ")
            if any(c not in printable for c in message):
                print("Invalid characters in message")
                continue
            if message == PASSPHRASE:
                print("Yes, but no :(")
                continue
            message = message.encode()
            signature = sign(message, SECRET)

            print(f"Signed Message: {message.hex()}.{signature}")

        elif choice == "2":
            signed = input("Enter signed message: ")
            if message := verify(signed, SECRET):
                print("Verified!")
                print(f"Message: {message}")
                if message == PASSPHRASE:
                    with open("flag.txt") as f:
                        print(f"Flag: {f.read()}")
                    break
            else:
                print("Invalid signature")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid input")

        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
