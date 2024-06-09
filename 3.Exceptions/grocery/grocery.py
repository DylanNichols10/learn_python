def main():
    groceries = prompt_user_dict()
    for item in sorted(groceries):
        print(f"{groceries[item]} {item.upper()}")

def prompt_user_dict():
    dict_items = {}
    while True:
        try:
            item = input().lower()
            if item in dict_items:
                dict_items[item] = int(dict_items[item])+1
            else:
                dict_items[item] = 1

        except EOFError:
            return dict_items

main()
