def main():
    user_math = input("Expression: ")
    x, y, z = user_math.strip().split(" ")
    print(do_math(x,y,z))

def do_math(x,y,z):
    x = int(x)
    z = int(z)
    if y == "+":
        return float(x+z)
    if y == "*":
        return float(x*z)
    if y == "-":
        return float(x-z)
    if y == "/":
        return float(x/z)

main()
