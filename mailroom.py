"""Mailroom Madness."""
donar_list = {'John Snow': [100, 20, 50], 'Robert Stark': [5, 3, 1]}

def main():
    """Main Function."""
    running = True

    while(running is True):
        print("Hello, Welcome to Mail Room Madness") 

        option_select = input("Options 1) Send 'Thank You' 2) Create Report or 'q' to quit. ")
        if option_select == 'q':
            running = False
        elif option_select == '1':
            donar_name = send_thanks()
            if donar_name != False:
                #add donation
                add_donation(donar_name)
                print(donar_list)
        elif option_select == '2':
            print(create_report())

    print("END")


def send_thanks():
    """Send Thank You."""
    donar_name = input("Please enter a full name: ")

    if check_name(donar_name)==False:
        add_name_option = input("Name %s is not in list, do you want to add to donar list? y) n) " % donar_name)
        if add_name_option == 'n':
            return False
        elif add_name_option == 'y':
            donar_list[donar_name] = []
            return donar_name
    else:
        return donar_name

def check_name(donar_name):
    """Check Name function."""
    if donar_name in donar_list:
        return True
    else:
        return False

def add_donation(donar_name):

    make_donation = input("Enter Donation Amount: ")
    if check_donation(make_donation) == True:
        donar_list[donar_name].append(int(make_donation))
    else:
        print("invalid donation")

def check_donation(donation):
    try:
        int(donation)
        return True
    except ValueError:
        return False

def create_report():
    """Create Report."""
    return "REPORT CREATED"


if __name__ == '__main__': # pragma : no cover
    main()