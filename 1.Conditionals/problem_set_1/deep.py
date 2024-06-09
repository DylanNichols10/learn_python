def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? " )
    deep(user_input)

def deep(p):
    if p.strip() == "42":
        print("Yes")
    elif p.lower().strip() == "forty-two":
        print("Yes")
    elif p.lower().strip() =="forty two":
        print("Yes")
    else:
        print("No")

main()
