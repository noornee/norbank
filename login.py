import json
from bank_class import BankAccount


def login():
    print('------------------------------')
    print('Welcome to norbank!')
    print('fill in ur login details below')
    print('------------------------------')
    log_id = input('user_id: ')
    log_pword = input('password: ')
    with open('bank.json') as doc:
        data = json.load(doc)
        temp = data['users']
        for user in temp:
            if log_id == user['user_id'] and log_pword != user['password']:
                print('Invalid Password,try again')
                return login()
            elif log_id == user['user_id'] and log_pword == user['password']:
                x = f"{log_id} {log_pword}"
                print('🔅 logged in 🔅')
                return x

 


x1 = BankAccount.from_string(login())



def reverse_ui():
    opt = input('Do you want to go back? [y/n]: ')
    if opt == 'y':
        interface()



def interface():

    print('------------------------------')
    print(f"WELCOME #{x1.user_id}")
    print("heres a list of options u could choose: ")
    options = ['check account info', 'check balance', 'withdrawal', 'deposit']
    for i, option in zip(range(len(options)), options):
        print(f"{i}) {option}")
    print('********************')
    result = int(input('pick a number: '))
    print('********************')
    if result == 0:
        print(x1.account_info())
        reverse_ui()
    elif result == 1:
        print(options[1].upper())
        print(x1.check_balance())
        reverse_ui()
    elif result == 2:
        print(options[2].upper())
        num = int(input('input the amount u want to withdraw: '))
        print(x1.withdraw(num))
        reverse_ui()
    elif result == 3:
        print(options[3].upper())
        num = int(input('input the amount u want to deposit: '))
        print(x1.deposit(num))
        reverse_ui()
 
     




interface()

