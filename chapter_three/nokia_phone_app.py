def options():
    option = int(input("""
                    8. Options
                     1. Type of view
                     2. Memory status

                     Click 0 to go back to PhoneBook Menu"""))
    match option:
        case 0:
            phonebook()
        case 1:
            back = int(input("""
                                        1. Type of view
                                        
                                        0. click 0 to go back
                                        """))
            if back == 0:
                options()


def mainMenu():
    pass


def phonebook():
    phoneBook = int(input("""                     
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
                    0. <--"""))

    match phoneBook:
        case 0:
            menu()
        case 1:
            print("Search")
        case 2:
            print("Service Nos")
        case 3:
            print("Add Name")
        case 4:
            print("Erase")
        case 5:
            print("Edit")
        case 6:
            print("Assign tone")
        case 7:
            print("Send b' Card")
        case 8:
            options()
        case 9:
            print("Speed dials")
        case 10:
            print("Voice tags")
        case 0:
            mainMenu();


def messages():
    pass


def chat():
    pass


def show_call_duration():
    call_duration = int(input("""
    5. Show call duration
         1. Last call duration
         2. All calls' duration
         3. Received calls duration
         4. Dialled calls duration
         5. Clear timers
                                    
         0<----"""))
    match call_duration:
        case 0:
            menu()


def show_call_cost():
   show_call = int(input("""
                                1. Show call costs
                                    1. Last call cost
                                       2. All calls' cost
                                       3. Clear counters
                                       
                                       
                                       0<-----"""))
   match show_call:
       case 0:
           call_register()


def call_cost_settings():
    call_cost_settings = int(input("""
     7. Call cost settings
                1. Call cost limit
                2. Show costs in
                                       
                0<-----"""))

    match call_cost_settings:
        case 0:
            mainMenu()


def call_register():
    register = int(input("""
                            1. Missed calls
                            2. Received calls
                            3. Dialled numbers
                            4. Erase recent call lists
                            5. Show call duration
                            6. Show call costs
                            7. Call cost settings
                            8. Prepaid credit
                            
                            
                            Click 0 to go back"""))
    match register :
        case 0:
            mainMenu()
        case 1:
            print("I. Missed calls")
        case 2:
            print("2. Received calls")
        case 3:
            print(" 3. Dialled numbers")
        case 4:
            print(" 4. Erase recent call list")
        case 5:
            show_call_duration()
        case 6:
            show_call_cost()
        case 7:
            call_cost_settings()
        case 8:
            print("Prepaid Credit")




def tones():
    pass


def call_divert():
    pass


def settings():
    pass


def games():
    pass


def calculator():
    pass


def reminder():
    pass


def clock():
    pass


def profiles():
    pass


def sim_services():
    pass


def menu():
    menu = int(input("""
        1. Phone book
        2. Messages
        3. Chat
        4. Call register
        5. Tones
        6. Settings
        7.  Call Divert
        8. Games
        9. Calculator
        10. Reminders
        11. Clock
        12. profiles
        13. SIM services
        """))

    match menu:

        case 1:
            phonebook()
        case 2:
            messages()
        case 3:
            chat()
        case 4:
            call_register()
        case 5:
            tones()
        case 6:
            settings()
        case 7:
            call_divert()
        case 8:
            games()
        case 9:
            calculator()
        case 10:
            reminder()
        case 11:
            clock()
        case 12:
            profiles()
        case 13:
            sim_services()


def message_settings():
    pass


def messages():
    message = int(input("""
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
                0. <-- """))
    match message:
        case 0:
            menu()
        case 1:
            print("1. Write messages")
        case 2:
            print("2. Inbox")
        case 3:
            print("3. Outbox")
        case 4:
            print("4. Picture messages")
        case 5:
            print("5. Templates")
        case 6:
            print("6. Smileys")
        case 7:
            message_settings()


def message_settings():
    message_set = int(input("""1. Set
                               2. Common


                                Click 0 to go back to Menu"""))
    match message_set:
        case 0:
            message_settings()
        case 1:
            print("""
        1. Message centre number
        2. Messages sent as
        3. Message validity
        """)
        case 2:
            print("""
                1. Delivery reports
                2. Reply via same centre
                3. Character support
                """)
            case_: print("Invalid input")




menu()
