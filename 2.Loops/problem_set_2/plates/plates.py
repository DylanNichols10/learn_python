def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
       print("Invalid")


def is_valid(s):
    if check_start(s) and check_length(s) and check_nums(s) and check_punct(s):
        return True
    else:
        return False


def check_start(s):
    if s[0:2].isalpha():
         return True
    else:
        return False

def check_length(s):
    if len(s) >= 2 and len(s) <=6:
        return True
    else:
        return False

def check_nums(s):
    for char in s:
        if char.isdigit():
            intindex= s.find(char) # once we detect a number we can check if it is not a 0 and then verify the rest of the string doesn't contain any letters
            if s[intindex:].isdigit() and not int(char) == 0:
                return True
            else:
                return False
    return True

def check_punct(s):
    bad = [" ",".","'"]
    return not any (item in s for item in bad)

main()
