"""Mailroom Madness."""
donar_list = {}

def main():
    """Main Function."""
    running = True

    while(running is True):
        print("Hello, Welcome to Mail Room Madness") 

        option_select = input("Options 1) Send 'Thank You' 2) Create Report or 'q' to quit.")
        if option_select == 'q':
            running = False
        elif option_select == '1':
            print(send_thanks())
        elif option_select == '2':
            print(create_report())

    print("END")


def send_thanks():
    """Send Thank You."""
    return "THANK YOU"


def create_report():
    """Create Report."""
    return "REPORT CREATED"


if __name__ == '__main__': # pragma : no cover
    main()