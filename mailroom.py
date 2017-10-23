"""Mailroom Madness."""
donar_list = {'John Snow': ['100', '20', '50'], 'Robert Stark': ['50', '30', '10'],
              'Tyrion Lannister': ['500', '600']}
donar_report = {}

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
                donation_amount = add_donation(donar_name)
                print("E-mail Message: ")
                print(create_email(donar_name, donation_amount))
                print("SENT")
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
        return make_donation
    else:
        print("invalid donation")


def check_donation(donation):
    try:
        int(donation)
        return True
    except ValueError:
        return False


def create_email(donar_name, donation_amount):
    return "Thank you %s for your donation of $%s" %(donar_name, donation_amount)


def create_report():
    """Create Report."""
    print("Creating Report")

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
                report_body += "%s          %s             %s\n" %(donar,donar_report[donar][0],donar_report[donar][1]) 
    return(report_body)


def get_average_donation(donations):
    average = float(sum(donations)) / max(len(donations), 1)
    return "{0:.2f}".format(average)


if __name__ == '__main__': # pragma : no cover
    main()