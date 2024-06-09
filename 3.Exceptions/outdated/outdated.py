months =    [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# implement a program that prompts the user for a date in month-day-year order
# Then output that same date in YYYY-MM-DD format.
# If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

def main():

    while True:
        user_date = input("Date: ").strip()

        try:
            parse_date_num(user_date)
            break

        except ValueError:

            try:
                parse_date_str(user_date)
                break

            except ValueError as error:
                pass

def parse_date_num(date):
    split_date = date.split("/")

    if len(split_date) == 3:
        x,y,z = split_date
        for num in x,y,z:
            try:
                int(num)
            except ValueError:
                raise ValueError("Ints not detected in mm/dd/yyyy format")
        if int(x) > 12 or int(y) > 31:
            raise ValueError("Months or Days are not valid, i.e. >12 or > 31")
        else:
            print(f"{z}-{int(x):02}-{int(y):02}")
            return
    else:
        raise ValueError("Date not in correct format for parse_date_num()")


def parse_date_str(date):
    if "," not in date:
        raise ValueError("No comma = bad apparently")
    else:
        date = date.replace(",","")             # replace comma so we can simply split on " " for our 3 elements

    y,x,z = date.split()                        # y,x,z cause european brain had me thinking as 'dd month yyyy'

    if y in months:
        y = months.index(y)+1                   # +1 to offset zero index
        if int(x) > 31:
            raise ValueError("Days exceeds 31")
        else:
            print(f"{z}-{int(y):02}-{int(x):02}")
    else:
        raise ValueError("Value not found in Months Dictionary")

main()
