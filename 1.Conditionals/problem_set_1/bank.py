def main():
    user_greeting = input("Ask a greeting: ")
    print(eval_greet(user_greeting))

def eval_greet(s):
    s = s.lower().strip()
    if s.startswith("hello"):
        return "$0"
    elif s.startswith("h"):
        return "$20"
    else:
        return "$100"

main()
