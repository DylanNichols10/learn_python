# while True:
#     try:
#         x = int(input("What is x? "))
#     except ValueError:
#         print("x not valid num")
#     else:
#         break


# def get_user_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#             return x
#         except ValueError:
#             print("x not valid num")



def main():
    x = get_user_int("What's x? ")
    print (f"x is {x}")


def get_user_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass

main()

