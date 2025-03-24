from rng import Random
import asyncio, os




async def handle_prompt(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Received from {addr!r}")

    seed = int.from_bytes(os.urandom(10), "big")
    r = Random(seed) # seeded with random.getrandbits(128)

    writer.write(b"Welcome to MT23209! Play the guessing game and get your prize! (you have 1500 tries before system terminates connection)\nGuess correctly 100 consecutive times!\n")

    streak = 0

    for i in range(1500):
        writer.write(b"Guess your number here: ")


        try:
            data = await reader.read(20)
            guess = int(data.decode().strip())


        except ValueError:
            writer.write(b"That is not a valid number!\n")
            continue
        generated = r.extract_number()
        if generated == guess:
            streak += 1
            writer.write(f"Guess correct! {guess}\n".encode())

        else:
            if streak > 0:
                writer.write(b"Oh no! Your streak has been lost :( \n")
            streak = 0
            writer.write(f"The number I was thinking of was: {generated}\n".encode())

        if streak >= 100:
            # User has guessed correctly!
            writer.write(f"Congratulations! Here is your prize: {FLAG}\n".encode())
            writer.close()
            await writer.wait_closed()

            return



    writer.close()
    await writer.wait_closed()



FLAG = os.getenv("FLAG")

async def main():
    if FLAG == None:
        raise Exception("No flag provided!")
        return
    server = await asyncio.start_server(
        handle_prompt, '0.0.0.0', 10080)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
