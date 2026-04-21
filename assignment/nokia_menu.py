def main_menu():
    print(f"""  MAIN MENU 
                1. Phone book
                2. Messages
                3. Chat
                4. Call register
                5. Tones
                6. Settings
                7. Call divert
                8. Games
                9. Calculator
               10. Reminders
               11. Clock
               12. Profiles
               13. SIM services
                0. Exit
                """)
def phone_book():
    print(f""" PHONE BOOK
                1. Search
                2. Service No
                3. Add name	
                4. Erase
                5. Edit
                6. Assign tone
                7. Send b'card
                8. Options
                9. Speed dials
               10. Voice tags
                0. Back
                """)
def messages():  
    print(f"""  Messages
                1. Write messages
                2. Inbox
                3. Outbox
                4. Picture messages
                5. Templates
                6. Smileys
                7. Message settings
                8. Info service
                9. Voice service
                10. Service command editor
                0. Back
                """)
def messaging_settings():
    print(f"""  Message settings:
                1. Set 1
                2. Common
                0. Back
                """)

def set_1():
    printf(f""" Set 1:
                1. Message center number
                2. Message sent as
                3. Message validity
                0. Back
                """)
def common():
    print(f"""  Common:
                1. Delivery reports
                2. Reply via same center
                3. Character support
                0. Back
                """)
def chat():
    print(f"""  Chat
                0. Back
                """)
def call_register():
    print(f"""  Call Register
                1. Missed calls
                2. Received calls
                3. Dialed numbers
                4. Erase recent call list
                5. Show call duration
                6. Show call costs
                7. Call cost settings
                8. Prepaid credit
                """)

def show_call_duration():
    print(f"""  Show call duration:
                1. Last call
                2. All calls
                3. Received
                4. Dialled
                5. Clear timers
                """)
def show_call():
    print(f"""  Show call costs:
                1. Last cost
                2. All cost
                3. Clear counters
                """)
def call_cost_settings():
    print(f"""  Call cost settings:
                1. Call cost limit
                2. Show costs in    
                """)

def tones():
    print(f"""  Tones
                1. Ringing tone
                2. Ringing volume
                3. Incoming call alert
                4. Composer
                5. Message alert tone
                6. Keypad tones
                7. Warning and game tones
                8. Vibrating alert
                9. Screen saver
                """)
def settings():
    print(f"""  Settings
                1. Call settings
                2. Phone settings
                3. Security settings
                4. Restore factory settings
                """)
def call_settings():
    print(f"""  Call settings:
                1. Redial
                2. Speed dial
                3. Call waiting
                4. Own number
                5. Line use
                6. Auto answer
                """)
def phone_settings():
    print(f"""  Phone settings:
                1. Language
                2. Cell info
                3. Welcome note
                4. Network selection
                5. Lights
                6. Confirm SIM actions  
                """)

def security_settings():
    print(f"""  Security settings:
                1. PIN request
                2. Call barring
                3. Fixed dialing
                4. Closed user group
                5. Phone security
                6. Change 
                """)
def call_divert():
    print(f"""  Call divert
                0. Back
                """)
def games():
    print(f"""  Games
                0. Back
                """)
def calculator():
    print(f"""  Calculator
                0. Back
                """)
def reminders():
    print(f"""  Reminders
                0. Back
                """)
def clock():
    print(f"""  Clock
                1. Alarm clock
                2. Clock settings
                3. Date settings
                4. Stopwatch
                5. Countdown timer
                6. Auto update
                """)
def profiles():
    print(f"""  Profiles
                0. Back
                """)
def sim_services():
    print(f"""  Sim services
                0. Back
                """)


main_menu()
main_menu_choice = int (input("Enter number")) 
match main_menu_choice:
    case 1:
        phone_book()
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
        call_diverts()
    case 8:
        games()
    case 9:
        calculator()
    case 10:
        reminders()
    case 11:
        clock()
    case 12:
        profiles()
    case 13:
        sim_service()
    case _:
        print("Invalid Entry!")       
        
    
    
