def main():
    hello()
    name = input("What's your name? ")
    hello(name)

def hello(user = "world"):
    print(f"hello {user}")

main()

