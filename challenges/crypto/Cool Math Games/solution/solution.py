from pwn import remote
from string import ascii_lowercase, ascii_uppercase, digits
import random


# Server details
HOST = "127.0.0.1"  # Replace with the actual hostname or IP
PORT = 1337           # Replace with the actual port

def generate_random_string():
    """Generate a random string using the given seed."""
    return "".join(random.choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(32))

def brute_force_seed(user_id):
    """Brute-force the seed by comparing generated strings with the user ID."""
    """ for seed in range(0, 32768):  # Adjust range if the seed space is larger
        if generate_random_string(seed) == user_id:
            return seed
    return None """
    for i in range(0, 32768):
        random.seed(i)
        if user_id == "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(32)):
            return i
    return None

def main():
    conn = remote(HOST, PORT)

    conn.recvuntil(b"Your user ID is")
    user_id = conn.recvline().strip().decode().replace("\"", "")
    print(f"Extracted user ID: {user_id}")

    print("Brute-forcing the seed...")
    seed = brute_force_seed(user_id)
    if seed is None:
        print("Failed to find the seed.")
        conn.close()
        return
    print(f"Found seed: {seed}")
    
    random.seed(seed)
    generate_random_string() # empty out the first random string otherwise the whole order is screwed
    
    conn.recvuntil(b"Good luck!\n")
    for i in range(160):
        print("Line received: ", conn.recvline())
        answer_string = generate_random_string()
        print(f"Sending answer for round {i+1}: {answer_string}")
        conn.sendline(answer_string.encode())
        print("Answer sent")
        print("Awaiting answer...")
        target_str = f"******** Round {i+1} ********"
        response = conn.recvline().decode().strip()
        try:
            if response and "Sorry" not in response:
                print("Moving to next round...")
                continue
        except Exception as e:
            print("Error:", e)
            print(f"Response got: {response}")
            break

    # Retrieve the flag
    conn.recvuntil(b"Here is your flag:")
    flag = conn.recvline().decode().strip()
    print("Flag:", flag)
    conn.close()

if __name__ == "__main__":
    main()
