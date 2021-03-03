# https://www.youtube.com/watch?v=6iCP0EpRWFg&ab_channel=Suedew

users = {}


def new_user():
    create_user = input("Create username: ")

    if create_user in users:
        print("Username already taken")
    else:
        create_pw = input("Create password: ")
        users[create_user] = create_pw
        print("--Account created--\n")

        prompt = input("Press \"y\" to proceed login, \"n\" to return main menu:\n")
        if prompt == "y":
            old_user()
        elif prompt == "n":
            main_menu()


def old_user():
    correct_credentials = False

    while not correct_credentials:
        username = input("Enter username: ")
        passw = input("Enter password: ")

        if username in users and users[username] == passw:
            correct_credentials = True
            print("--Login Successful--\n")

            # prompt = input("Press \"y\" to exit, \"n\" to return main menu:\n")
            # if prompt == "y":
            #     exit()
            # elif prompt == "n":
            #     main_menu()

        else:
            print("--Invalid username or password--\nPlease Try again:\n")


def change_pw():
    username = input("Enter username: ")

    if username in users:
        password = input("Enter old password:")

        if password == users[username]:
            npassword = input("Enter New password: ")
            users[username] = npassword
            print("Password successfully changed!")
        else:
            print("Incorrect password")

    else:
        print("--Username does not exist--")
        # print("--Username does not exist--\nPlease try again\n")
        # change_pw()


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


main_menu()

