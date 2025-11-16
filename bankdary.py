class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("موجودی کافی برای برداشت وجود ندارد.")

    def display(self):
        print(f"نام صاحب حساب: {self.owner_name} | موجودی: {self.balance} تومان")


def main():
    accounts = []

    # مرحله اول: ایجاد حساب‌های بانکی
    num_accounts = int(input("چند حساب بانکی می‌خواهید ایجاد کنید؟ "))
    for _ in range(num_accounts):
        owner_name = input("نام صاحب حساب را وارد کنید: ")
        initial_balance = float(input(f"موجودی اولیه حساب برای {owner_name} را وارد کنید: "))
        account = BankAccount(owner_name, initial_balance)
        accounts.append(account)

    # منوی عملیات بانکی
    while True:
        print("\n===== منوی عملیات بانکی =====")
        print("1. نمایش موجودی همه حساب‌ها")
        print("2. سپرده‌گذاری در حساب")
        print("3. برداشت از حساب")
        print("4. نمایش حساب‌هایی با موجودی بیشتر از میانگین")
        print("5. خروج از برنامه")

        choice = input("لطفاً یک گزینه را وارد کنید: ")

        if choice == '1':
            # نمایش موجودی همه حساب‌ها
            for account in accounts:
                account.display()

        elif choice == '2':
            # سپرده‌گذاری در حساب
            account_name = input("نام حساب مورد نظر را وارد کنید: ")
            deposit_amount = float(input(f"مقدار سپرده را برای {account_name} وارد کنید: "))
            for account in accounts:
                if account.owner_name == account_name:
                    account.deposit(deposit_amount)
                    print(f"مبلغ {deposit_amount} تومان به حساب {account_name} اضافه شد.")
                    break
            else:
                print("حساب با این نام یافت نشد.")

        elif choice == '3':
            # برداشت از حساب
            account_name = input("نام حساب مورد نظر را وارد کنید: ")
            withdraw_amount = float(input(f"مقدار برداشت را برای {account_name} وارد کنید: "))
            for account in accounts:
                if account.owner_name == account_name:
                    account.withdraw(withdraw_amount)
                    break
            else:
                print("حساب با این نام یافت نشد.")

        elif choice == '4':
            # نمایش حساب‌هایی با موجودی بیشتر از میانگین
            total_balance = sum(account.balance for account in accounts)
            average_balance = total_balance / len(accounts) if accounts else 0
            print(f"میانگین موجودی حساب‌ها: {average_balance:.2f} تومان")
            print("حساب‌هایی با موجودی بیشتر از میانگین:")
            for account in accounts:
                if account.balance > average_balance:
                    account.display()

        elif choice == '5':
            # خروج از برنامه
            print("خروج از برنامه...")
            break

        else:
            print("لطفاً یک گزینه معتبر وارد کنید.")

if __name__ == "__main__":
    main()
