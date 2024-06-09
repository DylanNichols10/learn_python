def main():
    userinput = int(input("please input a integer mass in kg "))
    userinput = energy(userinput)
    print(userinput)

def energy(mass):
    return (mass * 300000000**2)

main()

