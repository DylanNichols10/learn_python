def main():
    legal_tender = [25,10,5] # define accepted denominations
    remaining = 50
    while remaining > 0:
        coin = insert_coin(legal_tender,remaining)
        remaining = calculate_due(coin,remaining)

def insert_coin(legal_tender,remaining):
    while True:
        print("Amount Due:", str(remaining)) # i dont like this here but it fixes re-promting the amount due when an invalid coin has been entered
        n = int(input("Insert Coin: "))
        if n in legal_tender:
            break
    return n

def calculate_due(n,due):
    due = due - n
    if due <= 0:
        print("Change Owed: ", str(due*-1), sep="")
        return due
    else:
        return due

main()
