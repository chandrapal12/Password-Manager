from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()



master_pwd = input("Enter your master password? ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(f"{name} | {fer.encrypt(pwd.encode()).decode()} \n")
    


while True:
    mode = input("Would you like to add a password or view existing ones (add or view) and press 'q' to quit  " )
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode")
        continue