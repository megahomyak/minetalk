from mcrcon import MCRcon

with open("password.txt") as f:
    PASSWORD = f.read().strip()

with MCRcon("127.0.0.1", PASSWORD) as rcon:
    while True:
        print(rcon.command(input("Command: ")))
