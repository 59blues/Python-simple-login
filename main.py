# https://www.youtube.com/watch?v=6iCP0EpRWFg&ab_channel=Suedew Credits to Suedew

users = {}


def new_user():
    create_user = input("Create username: ")

    if create_user in users:
        print("Username already taken")
    else:
        create_pw = input("Create password: ")
        users[create_user] = create_pw  # assign value(password) to key(username)
        print("--Account created--\n")
        cue()


def old_user():
    correct_credentials = False

    while not correct_credentials:
        username = input("Enter username: ")
        passw = input("Enter password: ")

        if username in users and users[username] == passw:
            correct_credentials = True
            print("--Login Successful--\n")
        else:
            print("--Invalid username/password--\nPlease try again:\n")


def change_pw():
    valid_user = False

    while not valid_user:
        username = input("Enter username: ")
        if username in users:
            password = input("Enter old password:")

            if password == users[username]:
                npassword = input("Enter New password: ")
                users[username] = npassword
                valid_user = True
                print("Password successfully changed!")
                cue()
            else:
                print("--Incorrect password--")

        else:
            print("--Username does not exist--")


def main_menu():
    status = input("Welcome!\n1)Log in\n2)Register Account\n3)Change password\n\n")
    if status == "1":
        old_user()
    elif status == "2":
        new_user()
    elif status == "3":
        change_pw()
    else:
        print("Invalid input!")


def cue():
    prompt = input("Press \"y\" to proceed login, \"n\" to return main menu:\n")
    if prompt == "y":
        old_user()
    elif prompt == "n":
        main_menu()


main_menu()

