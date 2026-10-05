expenses = []

while True:
    print("\n1 - Шығын қосу")
    print("2 - Жалпы шығын")
    print("3 - Шығу")

    choice = input("Таңдау: ")

    if choice == "1":
        name = input("Шығын атауы: ")
        amount = float(input("Сомасы: "))
        expenses.append((name, amount))
        print("Қосылды!")

    elif choice == "2":
        total = sum(amount for name, amount in expenses)
        print("Барлық шығын:", total, "теңге")

    elif choice == "3":
        break
