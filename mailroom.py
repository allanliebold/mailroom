"""Mailroom Madness."""
donar_list = {'John Snow': ['100', '20', '50'],
              'Robert Stark': ['50', '30', '10'],
              'Tyrion Lannister': ['500', '600']}


def main():
    """Main Function."""
    running = True

    while(running is True):
        option_message = """
        "1) Send 'Thank You' 2) Create Report or 'q' to quit. "
        """
        option_select = input(option_message)
        if option_select == 'q':
            running = False
        elif option_select == '1':
            donar_name = send_thanks()
            if donar_name is not False:
                donation_amount = add_donation(donar_name)
                if donation_amount is not False:
                    print("E-mail Message: ")
                    print(create_email(donar_name, donation_amount))
                    print("SENT")
        elif option_select == '2':
            print(create_report())

    print("END")


def send_thanks():
    """Send Thank You."""
    donar_name = input("Please enter a full name: ")

    if check_name(donar_name) is False:
        add_name_option = input("Name %s is not in list, do you want to add to donar list? y) n) " % donar_name)
        if add_name_option == 'n' or add_name_option == 'q':
            return False
        elif add_name_option == 'y':
            donar_list[donar_name] = []
            return donar_name
    else:
        return donar_name


def check_name(donar_name):
    """Check Name function."""
    if donar_name not in donar_list or donar_name == 'q':
        return False
    return True


def add_donation(donar_name):
    """Add Donation function."""
    make_donation = input("Enter Donation Amount: ")
    if check_donation(make_donation) is True:
        donar_list[donar_name].append(int(make_donation))
        return make_donation
    else:
        print("invalid donation")
        return False


def check_donation(donation):
    """Check Donation amount."""
    try:
        int(donation)
        return True
    except ValueError:
        return False


def create_email(donar_name, donation_amount):
    """Create e-mail text."""
    return "Thank you %s for your donation of $%s" %(donar_name, donation_amount)


def create_report():
    """Create Report."""
    print("Creating Report")
    donar_report = {}
    report_body = "Name of Donar     Total Donations     Average Donation\n"

    for donar, donations in donar_list.items():
        donations = [int(i) for i in donations]
        donar_report[donar] = [sum(donations), get_average_donation(donations)]

    temp = list()
    for k, v in donar_report.items():
        temp.append(v[0],)
    temp.sort()
    temp.reverse()

    for i in temp:
        for donar in donar_report:
            if donar_report[donar][0] == i:
                report_body += "%s              %s                 %s\n" %(donar,donar_report[donar][0],donar_report[donar][1]) 
    return(report_body)


def get_average_donation(donations):
    """Get average donation."""
    average = float(sum(donations)) / max(len(donations), 1)
    return "{0:.2f}".format(average)


if __name__ == '__main__': # pragma : no cover
    print("Hello, Welcome to Mail Room Madness")
    main()
