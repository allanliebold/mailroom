donar_list = {}

def main():
    
    running = True

    while(running == True):
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
    return "THANK YOU"

def create_report():
    return "REPORT CREATED"

if __name__ == '__main__':
    main()