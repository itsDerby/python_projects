def mainMenu():
    main = input("""
                1. Phone book
                2. Messages
                3. Chat
                4. Call Register
                5. Tones
                6. Settings
                7. Call Divert
                8. Games
                9. Calculator
                10. Reminders
                11. Clock
                12. Profiles
                13. SIM services """)
    match main:
        case "1":
            phonebook()
        case "2":
            messages()
        case "3":
            chat()
        case "4":
            call_register()
        case "5":
            tones()
        case "6":
            settings()
        case "7":
            call_divert()
        case "8":
            games()
        case "9":
            calculator()
        case "10":
            reminder()
        case "11":
            clock()
        case "12":
            profiles()
        case "13":
            sim_services()


def phonebook():
    phoneBook = input("""                     
                    1. Search
                    2. Service Nos
                    3. Add Name
                    4. Erase
                    5. Edit
                    6. Assign tone
                    7. Send B' Card
                    8. Options
                    9. Speed Dials
                    10. Voice Tag
                    0. <--""")
    if phoneBook == "0":
        mainMenu()

    match phoneBook:
        case "1":
            search = input("""Search 
           
           
                        Click 0 to go back""")
            if search == "0":
                phonebook()
            else:
                print("""invalid input""")
        case "2":
            service_no = input("""Service Number
            
            
                            Click 0 to go back""")
            if service_no == "0":
                phonebook()

            else:
                print("""INVALID INPUT""")
        case "3":
            add_name = input("""Add Name
            
            
                            Click 0 to go back""")
            if add_name == "0":
                phonebook()
            else:
                print("""invalid input""")

        case "4":
            erase = input("""Erase
            
            
                        Click 0 to go back""")
            if erase == "0":
                phonebook()
            else:
                print("""invalid input""")

        case "5":
            edit = input("""Edit
            
            
                        Click 0 to go back""")
            if edit == "0":
                phonebook()
            else:
                print("""invalid input""")

        case "6":
            assign_tone = input("""Assign Tone
            
            
                            Click 0 to go back""")
            if assign_tone == "0":
                phonebook()
            else:
                print("""invalid input""")

        case "7":
            bcard = input("""
            Send b' Card
            
            
            Click 0 to go back""")

            if bcard == "0":
                phonebook()
            else:
                print("""invalid input""")

        case "8":
            options()
        case "9":
            speed_dial = input("""
                            Speed dials
            
                            Click 0 to go back""")
            if speed_dial == "0":
                phonebook()
            else:
                print("""invalid input""")
        case 10:
            voice_tags = input("""
                            Voice Tags
                            
                            
                            Click 0 to go back""")
            if voice_tags == "0":
                phonebook()
            else:
                print("""invalid input""")
        case "0":
            mainMenu()
        case "_":
            print("invalid input")


def options():
    option = input("""
                    8. Options
                     1. Type of view
                     2. Memory status

                     Click 0 to go back to PhoneBook Menu""")
    match option:
        case "0":
            phonebook()
        case "1":
            back = input("""
                                        1. Type of view

                                        0. click 0 to go back
                                        """)
            if back == "0":
                options()
        case "2":
            back = input("""
                                    2. Memory status

                                    click 0 to go back""")
            if back == "0":
                options()


def messages():
    mainMenu()


def chat():
    mainMenu()


def show_call_duration():
    call_duration = input("""
    5. Show call duration
         1. Last call duration
         2. All calls' duration
         3. Received calls duration
         4. Dialled calls duration
         5. Clear timers
                                    
         0<----""")
    match call_duration:
        case "0":
            mainMenu()


def show_call_cost():
    show_call = input("""
                                1. Show call costs
                                    1. Last call cost
                                       2. All calls' cost
                                       3. Clear counters
                                       
                                       
                                       0<-----""")
    match show_call:
        case "0":
            show_call_cost()


def call_cost_settings():
    call_cost_settings = input("""
     7. Call cost settings
                1. Call cost limit
                2. Show costs in
                                       
                0<-----""")

    match call_cost_settings:
        case "0":
            mainMenu()


def call_register():
    register = input("""
                            1. Missed calls
                            2. Received calls
                            3. Dialled numbers
                            4. Erase recent call lists
                            5. Show call duration
                            6. Show call costs
                            7. Call cost settings
                            8. Prepaid credit
                            
                            
                            Click 0 to go back""")
    match register:
        case "0":
            register = input("Register")

            if register == "0":
                mainMenu()

            else:
                print("Invalid input")
        case "1":
            missed_call = input("""
                1. Missed Calls
        
        Click 0 to go back""")

            if missed_call == "0":
                call_register()

            else:
                print("Invalid input")

        case "2":
            receive_call = input("""Received Calls
            
            
                        Click 0 to go back to the call menu""")
            if receive_call == "0":
                call_register()

            print("2. Received calls")
        case "3":
            print(" 3. Dialled numbers")
        case "4":
            print(" 4. Erase recent call list")
        case "5":
            show_call_duration()
        case "6":
            show_call_cost()
        case "7":
            call_cost_settings()
        case "8":
            print("Prepaid Credit")


def tones():
    tone = input("""
                                    1. Ringing tone
                                    2. Ringing volume
                                    3. Incoming call alert
                                    4. Composer
                                    5. Message alert tone
                                    6. Keypad tones
                                    7. Warning and game tones
                                    8. Vibrating alert
                                    9. Screen saver


                                    Click 0 to go back""")
    match tone:
        case "0":
            mainMenu()


def call_divert():
    mainMenu()


def call_settings():
    call_setting = input("""
                                    1. Automatic redial
                                    2. Speed dialling
                                    3. Call waiting
                                    4. Own number sending
                                    5. Automatic answer

                                    0<------""")
    match call_setting:
        case "0":
            settings()


def phone_settings():
    phone_setting = input("""
                                1. Language
                                2. Cell info display
                                3. Welcome note
                                4. Network note
                                5. Lights
                                6. Confirm SIM service actions
                                
                                CLick 0 to go back to settings""")
    match phone_setting:
        case "0":
            settings()


def security_setting():
    security_settingg = input(""" 1. PIN code request
                                2. Call barring service
                                3. Fixed dialing
                                4. Closed user group
                                5. Phone security
                                6. Change access codes
                                
                                0<-------""")
    match security_settingg:
        case "0":
            settings()


def settings():
    setting = input("""
                            1. Call settings
                            2. Phone settings
                            3. Security settings
                            4. Restore factory settings

                            0<------""")
    match setting:
        case "0":
            mainMenu()
        case "1":
            call_settings()
        case "2":
            phone_settings()
        case "3":
            security_setting()
        case "4":
            print("Restore Factory Settings")


def games():
    mainMenu()


def calculator():
    add_number = input("""
    Press any of the option to calculate:
    
    1. add
    2. subtract
    3.  multiply
    4.  division
    
    
    """)
    match add_number:
        case "0":
            mainMenu()
        case "1":
            add()
        case "2":
            subtract()
        case "3":
            multiply()

        case "_":
            print("invalid input, please try again")


def add():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(f"The Sum of {number1} + {number2} ={number1 + number2}")

    back = input("""Click 0 to go back to the main menu 
                    or
                    Click 1 to go back to the previous option""")
    match back:
        case "0":
            print(mainMenu())
        case "1":
            print(calculator())
        case "_":
            print("invalid, please try again")


def subtract():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(f"The Subtraction of {number1} - {number2} ={number1 - number2}")

    back = input("""Click 0 to go back to the main menu 
                        or
                        Click 1 to go back to the previous option""")
    match back:
        case "0":
            print(mainMenu())
        case "1":
            print(calculator())
        case "_":
            print("invalid, please try again")


def multiply():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(f"The Multiplication of {number1} * {number2} ={number1 * number2}")

    back = input("""Click 0 to go back to the main menu 
                            or
                            Click 1 to go back to the previous option""")
    match back:
        case "0":
            mainMenu()
        case "1":
            calculator()
        case "_":
            print("invalid, please try again")


def reminder():
    mainMenu()


def clock():
    mainMenu()


def profiles():
    mainMenu()


def sim_services():
    mainMenu()


def messages():
    message = input("""
                1. Write messages
                2. Inbox
                3. Outbox
                4. Picture messages
                5. Templates
                6. Smileys
                7. Message settings
                8. Info service
                9. Voice mailbox number
                10. Service command editor
                0. <-- """)
    match message:
        case "0":
            mainMenu()
        case "1":
            print("1. Write messages")
        case "2":
            print("2. Inbox")
        case "3":
            print("3. Outbox")
        case "4":
            print("4. Picture messages")
        case "5":
            print("5. Templates")
        case "6":
            print("6. Smileys")
        case "7":
            message_settings()


def message_settings():
    message_set = input("""1. Set
                               2. Common


                                Click 0 to go back to Menu""")
    match message_set:
        case "0":
            message_settings()
        case "1":
            print("""
        1. Message centre number
        2. Messages sent as
        3. Message validity
        """)
        case "2":
            print("""
                1. Delivery reports
                2. Reply via same centre
                3. Character support
                """)
        case "_":
            print("Invalid input")


mainMenu()
