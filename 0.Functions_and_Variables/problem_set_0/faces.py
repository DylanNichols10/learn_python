def main():
    userinput = input("Input some smileys or frownies to be replaced")
    convert(userinput)

def convert(text):
    print (text.replace(":)", "🙂").replace(":(","🙁"))

main()
