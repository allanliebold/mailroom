"""Mailroom Madness."""
donar_list = {'John Smith': [100, 20, 50], 'Robert Stark': [5, 3, 1]}

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

def check_name(donar_name):
    """Check Name function."""
    if donar_name in donar_list:
        return True
    return False


def create_report():
    """Create Report."""
    return "REPORT CREATED"


if __name__ == '__main__': # pragma : no cover
    main()