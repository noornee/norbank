import json


def write_json(data, filename='bank.json'):
    with open(filename, 'w') as doc:
        json.dump(data, doc, indent=2)


class BankAccount:
    balance = 0

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        with open('bank.json') as doc:
            data = json.load(doc)
            temp = data['users']
            for user in temp:
                if self.user_id == user['user_id'] and self.password == user['password']:
                    self.balance += user['balance']

    def fullname(self):
        with open('bank.json') as doc:
            data = json.load(doc)
            temp = data['users']
            for user in temp:
                if self.user_id == user['user_id'] and self.password == user['password']:
                    return f"{user['firstName']} {user['lastName']}"              

    def account_info(self):
        print('ACCOUNT INFO')
        return f"fullname: {self.fullname()}\nid: {self.user_id}\nbalance: ${self.balance}"

    def account_type(self, acc_type):
        self.acc_type = ['Current', 'Savings']
        if acc_type == acc_type[0]:
            return f" acc name is {self.acc_type[0]}"
        else:
            return f" acc name is {self.acc_type[1]}"

    def check_balance(self):
        return f"your current balance is ${self.balance}"

    def deposit(self, amount):
        with open('bank.json') as doc:
            data = json.load(doc)
            temp = data['users']
            for user in temp:
                if self.user_id == user['user_id'] and self.password == user['password']:
                    self.balance += amount
                    new_bal = {'balance': self.balance}
                    user.update(new_bal)
                    write_json(data)
                    return f"you deposited ${amount}, your current balance is now ${self.balance}"

    def withdraw(self, amount):
        with open('bank.json') as doc:
            data = json.load(doc)
            temp = data['users']
            for user in temp:
                if self.user_id == user['user_id'] and self.password == user['password']:
                    self.balance -= amount
                    new_bal = {'balance': self.balance}
                    user.update(new_bal)
                    write_json(data)
        if amount <= self.balance:
            return f"you withdrew ${amount}, your current balance is now ${self.balance}"
        else:
            return 'your account balance is too low'

    @classmethod
    def from_string(cls, user_data):
        user_id, password = user_data.split(' ')
        return cls(user_id, password)
