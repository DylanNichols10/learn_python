def main():
    x,y = get_user_frac("Fraction: ")
    print(calc_fract(x,y))

def get_user_frac(prompt):
    while True:
        try:
            fract = input(prompt)
            x = int((fract).split("/")[0])
            y = int((fract).split("/")[1])
            if y == 0:
                raise ValueError("Zero entered for denominator")
            if x > y:
                raise ValueError("Numerator cannot be greater than denominator in a fuel gauge")
            return x,y
        except ValueError as error:
            pass

def calc_fract(x,y):
    if x/y <= 0.01:
        return "E"
    elif x/y >= 0.99:
        return "F"
    else:
     return str(round(x/y*100))+"%"



main()
