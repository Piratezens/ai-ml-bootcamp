class BankAccount:

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} credited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} debited successfully.")
        else:
            print("Insufficient balance!")

    def display(self):
        print("\nAccount Details")
        print("-----------------------")
        print("Name      :", self.name)
        print("Account No:", self.account_no)
        print("Balance   : $", self.balance)


students = [
    BankAccount("Ram", 1001, 5000),
    BankAccount("Sita", 1002, 6000),
    BankAccount("Hari", 1003, 4500),
    BankAccount("Gita", 1004, 7000),
    BankAccount("Anita", 1005, 5500)
]

while True:
    print("\n===== BANK MENU =====")
    print("1. Display All Accounts")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for student in students:
            student.display()

    elif choice == 2:
        acc = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))

        for student in students:
            if student.account_no == acc:
                student.deposit(amount)
                break
        else:
            print("Account not found!")

    elif choice == 3:
        acc = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdraw Amount: "))

        for student in students:
            if student.account_no == acc:
                student.withdraw(amount)
                break
        else:
            print("Account not found!")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")