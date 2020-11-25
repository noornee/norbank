import json

user_data = []




def signup():
    print('Welcome to the signup page!\nFill in ur details to create an account')
    firstName = input('first name: ')
    lastName = input('last name: ')
    username = input('username: ')
    user_id = f"{username}{len(username)}"
    password = input('password: ')
    acc_balance = 0
    user_id = f"{username}{len(username)}"
 
    user_data.append({"firstName": firstName, "lastName": lastName,
                      "username": username, "user_id": user_id, "password": password, "balance": acc_balance})
    print(f'Account created!')
    print('--------------------')
    print(f"user_id is ==> {user_id}")
    print('--------------------')


def write_json(data, filename='bank.json'):
    with open(filename, 'w') as doc:
        json.dump(data, doc, indent=2)


def read_write_json():
    with open('bank.json') as doc:
        data = json.load(doc)
        temp = data['users']
        for info in user_data:
            temp.append(info)
        write_json(data)


signup()
read_write_json()
