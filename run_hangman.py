import init_db as fc
import gameplay
import sys

def playgame(user_id):
    while True:
        gameplay.st(0, user_id)
        ct = input("Want to continue? y/n: ").lower()
        if ct == 'n':
            print("Terminating *_*")
            print("Thanks for playing!!")
            sys.exit()

def menu():
    print('\t\t\t\t\t\t_WELCOME TO HANGMAN_')
    print("MENU:")
    print("1. Register")
    print("2. Already registered")
    print("3. Exit")
    while True:
        try:
            ch = int(input("Enter a choice: "))
            if 1 <= ch <= 3:
                return ch
            else:
                print("Invalid choice. Please enter between 1-3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    ch = menu()
    if ch == 1:
        name = input("Enter your name: ")
        fc.mycur.execute("INSERT INTO Player_Registration(name) VALUES (%s)", (name,))
        fc.mydb.commit()

        fc.mycur.execute("SELECT id, name FROM Player_Registration ORDER BY id DESC LIMIT 1")
        user_id, user_name = fc.mycur.fetchone()
        print(f"REGISTRATION SUCCESSFUL!! Username: {user_name}, ID: {user_id}")

        fc.mycur.execute("INSERT INTO id_player(p_id) VALUES (%s)", (user_id,))
        fc.mydb.commit()

        print("Please remember your ID for future use.")
        playgame(user_id)

    elif ch == 2:
        idd = int(input("Enter your ID: "))
        fc.mycur.execute("SELECT p_id FROM id_player WHERE p_id = %s", (idd,))
        if fc.mycur.fetchone():
            fc.mycur.execute("SELECT name FROM Player_Registration WHERE id = %s", (idd,))
            user_name = fc.mycur.fetchone()[0]
            print(f"Welcome back {user_name}!!!!")
            playgame(idd)
        else:
            print("ID not found!!")

    elif ch == 3:
        print("TERMINATING *_*")
        print("Thanks for coming!!")
