class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {receipient}")
        else:
            print("insufficient funds")


class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_no):
        super().__init__(account_balance, phone_number)
        self.id_no = id_no

    def buyairtime(self, amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought successfully")


class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name
        self.business_name += business_name

    def receive_payment(self, amount):
        print(f"{amount} KES received from a customer")


personal = PersonalMpesa(2000, 113146948,"123456")
personal.send_money(300, 74783534)