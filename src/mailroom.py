"""Mailroom Madness.

This module gives a user access to a dictionary of donors and
the amounts they have donated. A user may select to send a thank
you e-mail to an existing donor, or add a new one. There is also
an option to generate a report of all donors in order of largest
to smallest total historical donation amount, as well as listing
their average donation amounts.
"""
donor_list = {'John Snow': ['100', '20', '50'],
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
            donor_name = send_thanks()
            if donor_name is not False:
                donation_amount = add_donation(donor_name)
                if donation_amount is not False:
                    print("E-mail Message: ")
                    print(create_email(donor_name, donation_amount))
                    print("SENT")
        elif option_select == '2':
            print(create_report())

    print("END")


def send_thanks():
    """Send Thank You.

    When option 1 is selected at the first prompt, a new prompt is
    brought up asking for a full name. If the name is not already in
    the dictionary of donors, the user may enter y to add it.

    Once a name in the dictionary has been provided, it is returned to
    the main function to proceed to the next step.
    """
    donor_name = input("Please enter a full name: ")

    if donor_name.lower() == 'q':
        return False
    elif not check_name(donor_name):
        add_name_option = input("Name %s is not in list, do you want to add "
                                "to the donor list? y) n) " % donor_name)
        if add_name_option == 'n' or add_name_option == 'q':
            return False
        elif add_name_option == 'y':
            donor_list[donor_name] = []
            return donor_name
    else:
        return donor_name


def check_name(donor_name):
    """Check if name entered is in the donor_list dictionary."""
    return donor_name in donor_list


def add_donation(donor_name):
    """Add Donation function.

    After receiving a valid donor name in the send_thanks function,
    the user is prompted to enter the dollar amount donated.
    """
    make_donation = input("Enter Donation Amount: ")
    if make_donation.lower() == 'q':
        return False

    if check_donation(make_donation) is True:
        donor_list[donor_name].append(int(make_donation))
        return make_donation
    else:
        print("Invalid donation amount")
        return False


def check_donation(donation):
    """Check Donation amount.

    A helper function called by add_donation to verify that an int
    has been entered, otherwise raise a ValueError.
    """
    try:
        int(donation)
        return True
    except:
        raise ValueError('Invalid amount entered')


def create_email(donor_name, donation_amount):
    """Create e-mail text.

    Return a string including the donor name and the amount donated.
    """
    return "Thank you %s for your donation of $%s" % (donor_name, donation_amount)


def create_report():
    """Create Report.

    Using the names and individual donations in the donor_list dictionary,
    this function creates a new dictionary called donor_report. Donor_report
    contains each donor's sum total and average donations.

    This donor_report dictionary is then used to create a string
    listing out the information in order starting from highest sum
    total. The string is returned to the main function to be printed.
    """
    print("Creating Report")
    donor_report = {}
    report_body = "Name of Donor     Total Donations     Average Donation\n"

    for donor, donations in donor_list.items():
        donations = [int(i) for i in donations]
        donor_report[donor] = [sum(donations), get_average_donation(donations)]

    temp = list()
    for k, v in donor_report.items():
        temp.append(v[0],)
    temp.sort()
    temp.reverse()

    for i in temp:
        for donor in donor_report:
            if donor_report[donor][0] == i:
                report_body += "%s              %s                 %s\n" % (donor, donor_report[donor][0], donor_report[donor][1])
    return(report_body)


def get_average_donation(donations):
    """Get average donation.

    A helper function called by create_report to calculate a donor's
    average donation amount.
    """
    average = float(sum(donations)) / max(len(donations), 1)
    return "{0:.2f}".format(average)


if __name__ == '__main__':  # pragma : no cover
    print("Hello, Welcome to Mail Room Madness")
    main()
