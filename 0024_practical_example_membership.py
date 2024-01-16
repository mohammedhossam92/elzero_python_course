# example with admin lists

admins = ["ahmed", "mona", "aicha", "maryam", "osama"]


user_name = input("please enter Your name? ").strip().lower()

if user_name in admins:
    print(f"hello {user_name} welcome back")

    option = input("do you want update or delete your name ? ").strip().lower()

    if option == "update":
        new_user_name = input("what is the new name?").strip().lower()

        admins[admins.index(user_name)] = new_user_name
        print("name updated successfully")
        print(admins)
    elif option == "delete":
        admins.remove(user_name)
        print("name deleted successfully")
        print(admins)
else:
    print("You are not an admin")