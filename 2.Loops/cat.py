# for _ in range(3):
#   print ("meow")

# print("meow \n" * 3, end = "")

#while True:
#   n = int(input("Input an integer "))
#  if n > 0:
#     break

#for _ in range(n):
#   print("meow")

def main():
    user_input = get_number()
    meow(user_input)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
