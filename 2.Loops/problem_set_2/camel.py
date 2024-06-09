def main():
    user_input = input("camelCase : ")
    print("snake_case: " + snake_case(user_input))

def snake_case(s):
    snake = ""
    for char in s:
        if  char.isupper():
            char = "_" + char.lower()
        snake = snake + char
    return snake

main()
