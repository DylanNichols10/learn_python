def main():
    usertext = input ("please input some text to be \"slowed\" down")
    slowdowntime(usertext)

def slowdowntime(text):
    print(text.replace(" ","..."))

main()

