def main():
    user_input = input("Please enter the time: ")
    print(meal_time(convert(user_input)))

def convert(time):
    hours,minutes = time.split(":")
    minutes = float(minutes)/60
    hours = float(hours)
    return hours+minutes

def meal_time(n):
    if n >= 7 and n <= 8:
        return "breakfast time"
    elif n >= 12 and n <= 13:
        return "lunch time"
    elif n >= 18 and n <= 19:
        return "dinner time"

if __name__ == "__main__":
    main()
