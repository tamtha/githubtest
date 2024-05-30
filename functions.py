# Function must be defined before calling (using) it

def main():
    name = input("What's your name? ").title().strip()
    greet(name)


def greet(username="player"):
    print("hello,", username)


main()
