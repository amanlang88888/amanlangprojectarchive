from time import sleep
import random
import time
import sys
import os
import threading
from wizard_animation import wizard
from wizard_animation import wizard2
from wizard_animation import wizard3
from wizard_animation import wizard4
from wizard_animation import wizard5
from wizard_animation import wizard6
from wizard_animation import wizard7
from wizard_animation import wizard8
from wizard_animation import wizard9
from wizard_animation import wizard10
from wizard_animation import wizard11
from wizard_animation import wizard12
from wizard_animation import wizard13
from wizard_animation import wizard14
from wizard_animation import wizard15
from wizard_animation import wizard16
from wizard_animation import trader_event_transmission_end
from wizard_animation import shop1
from wizard_animation import shop_transmission



###COLOURS AND TEXT###
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[36m",  # Cyan
    "\033[37m",  # White
]

RED = "\033[91m"
RESET_COLOUR = "\033[0m"  

def print_bold(text):
    print(f"\033[1m{text}\033[0m")

def print_rainbow_line(text):
    for char in text:
        color = random.choice(COLORS)  
        print(f"{color}{char}{RESET_COLOUR}", end='')
    print()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')  

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def typingPrintcinematic(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)

def typingPrintwizard(text):
    yellow = "\033[33m"  
    reset = "\033[0m"    

    for character in text:
        sys.stdout.write(yellow + character + reset)
        sys.stdout.flush()
        time.sleep(0.067)

def typingPrintwizardmad(text):
    red = "\033[91m"  
    reset = "\033[0m"    

    for character in text:
        sys.stdout.write(red + character + reset)
        sys.stdout.flush()
        time.sleep(0.08)

def typingPrintshop(text):
    cyan = "\033[36m"
    reset = "\033[0m"  

    for character in text:
        sys.stdout.write(cyan + character + reset)
        sys.stdout.flush()
        time.sleep(0.067)

def typingPrintshop2(text):
    violet = "\033[35m"
    reset = "\033[0m"  

    for character in text:
        sys.stdout.write(violet + character + reset)
        sys.stdout.flush()
        time.sleep(0.077)


###INITIAL VARIABLES###
taucannon = False
rolls_of_silk = 200
keralite_silver = 10000
andalusian_oxen = 20
diplomacy = 50
luck = 50
strength = 50





###START SEQUENCE BEGINS HERE###
typingPrint("""Command Module initializing...           
            """)

sleep (0.8)

def start_game():
    clear_console()
    print("""         
    Date: 08/12/3281
    Coordinates: Galactic Longitude (94.5°), Galactic Latitude (5.2°).
    Orbiting Jupiter. 
    Localised Travel: OFFLINE
    """)
    choice = input("""
    SHIP:
    [Cargo]
    [Decree]
    [Ship Status]
    [Set Course]
                   
    Input:""")
    if choice == 'Cargo':
        cargocheck()
    elif choice == 'cargo':
        cargocheck()
    elif choice == 'Decree':
        Decree()
    elif choice == 'decree':
        Decree()
    elif choice == 'Ship Status':
        shipstatus()
    elif choice == 'ship status':
        shipstatus()
    elif choice == 'Ship status':
        shipstatus()
    elif choice == 'Set Course':
        setcourse()
    elif choice == 'set course':
        setcourse()
    elif choice == 'Set course':
        setcourse()
    elif choice == 'devtest':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnscreenstart_game()

def returnscreenstart_game():
    choice = input("""
    Input: """)
    if choice == 'Cargo':
        cargocheck()
    elif choice == 'cargo':
        cargocheck()
    elif choice == 'Decree':
        Decree()
    elif choice == 'decree':
        Decree()
    elif choice == 'Ship Status':
        shipstatus()
    elif choice == 'ship status':
        shipstatus()
    elif choice == 'Ship status':
        shipstatus()
    elif choice == 'Set Course':
        setcourse()
    elif choice == 'Set course':
        setcourse()
    elif choice == 'set course':
        setcourse()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnscreenstart_game()

        

def cargocheck():
    clear_console()
    print(f"""
    {rolls_of_silk} katis Keralite silver
    {rolls_of_silk} rolls Tashkent silk 
    {andalusian_oxen} embryos Andalusian oxen 
    """)
    choice = input("""
    [Return]
    Input:""")
    if choice == 'Return':
        start_game()
    elif choice == 'return':
        start_game()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returncargocheck()

def returncargocheck():
    choice = input("""
    Input:""")
    if choice == 'Return':
        start_game()
    elif choice == 'return':
        start_game()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returncargocheck()

def Decree():
    clear_console()
    typingPrint("""
    Royal Decree
          
    By the decree of His Exuberance, Grand Vizier Seraph, Regent of His Majesty, Emperor Angkasa of the 3rd Dynasty, of the Qiang Al-Wijayya Empire,
    This ship shall travel under no degree of hinderance nor encumberance of any foreign parties, in accordance with Galactic Law,
    That it may reach the destination of Aramiz on diplomatic mission swiftly.
    
    Signed,
    
    الوزير الأعظم سيراف""")
    choice = input("""
    [Return]
    Input:""")
    if choice == 'Return':
        start_game()
    elif choice == 'return':
        start_game()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnDecree()

def returnDecree():
    choice = input("""
    Input:""")
    if choice == 'Return':
        start_game()
    elif choice == 'return':
        start_game()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnDecree()  

def shipstatus():
    clear_console()
    print("""      
    M CLASS BAOCHUAN EXPLORERᵀᴹ - QIANG AL-WIJAYYA ENGINEERING Ltd.
           
    >> Fusion Core - Healthy
    >> Engine - Healthy
    >> Hull - Healthy
    >> Maneuvering Thrusters - Healthy""")
    choice = input("""
    [Return]
    Input:""")
    if choice == 'Return':
        start_game()
    elif choice == 'return':
        start_game()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnshipstatus()

def returnshipstatus():
    choice = input("""
    Input:""")
    if choice == 'Return':
        start_game()
    elif choice == 'return':
        start_game()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnshipstatus()

def setcourse():
    clear_console()
    print("""
    Set Course for:

          

    [1] XINGMEN 星门 STARGATE
    
    """)
    choice = input("""
    [1]
    [Return]
    Input:""")
    if choice == 'Return':
        start_game()
    elif choice == 'return':
        start_game()
    elif choice == '1':
        stargate()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnsetcourse()

def returnsetcourse():
    choice = input("""
    Input:""")
    if choice == 'Return':
        start_game()
    elif choice == 'return':
        start_game()
    elif choice == '1':
        stargate()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnsetcourse()   

def stargate():
    clear_console()
    typingPrint("""
    Engaging Fusion Core ...""")

    sleep (3.5)
    
    typingPrint("""
    Engaging Engine ...""")

    sleep (3.5)
    
    typingPrint("""
    Engaging Maneuvering Thrusters ...""")

    sleep (3.5)

    choice = input("""
                   
    [Proceed]
    [Cancel]
    Input:""")
    if choice == 'Proceed':
        proceed()
    elif choice == 'proceed':
        proceed()
    elif choice == 'Cancel':
        clear_console()
        typingPrint("""
    Disengaging Fusion Core ...""")
        
        sleep (3.5)

        typingPrint("""
    Disengaging Engine ...""")
        
        sleep (3.5)

        typingPrint("""
    Disengaging Maneuvering Thrusters ...""")
        
        sleep (3.5)

        typingPrint("""
    Redirecting ...               
                    """)
        start_game()
    elif choice == 'cancel':
        clear_console()
        typingPrint("""
    Disengaging Fusion Core ...""")
        
        sleep (3.5)

        typingPrint("""
    Disengaging Engine ...""")
        
        sleep (3.5)

        typingPrint("""
    Disengaging Maneuvering Thrusters ...""")
        
        sleep (3.5)

        typingPrint("""
    Redirecting ...               
                    """)
        start_game()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnstargate()

def returnstargate():
    choice = input("""
    Input:""")
    if choice == 'Proceed':
        proceed()
    elif choice == 'proceed':
        proceed()
    elif choice == 'Cancel':
        clear_console()
        typingPrint("""
    Disengaging Fusion Core ...""")
        
        sleep (3.5)

        typingPrint("""
    Disengaging Engine ...""")
        
        sleep (3.5)

        typingPrint("""
    Disengaging Maneuvering Thrusters ...""")
        
        sleep (3.5)

        typingPrint("""
    Redirecting ...""")
        start_game()
    elif choice == 'cancel':
        clear_console()
        typingPrint("""
    Disengaging Fusion Core ...""")
        
        sleep (3.5)

        typingPrint("""
    Disengaging Engine ...""")
        
        sleep (3.5)

        typingPrint("""
    Disengaging Maneuvering Thrusters ...""")
        
        sleep (3.5)

        typingPrint("""
    Redirecting ...               
                    """)
        start_game()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnstargate() 

def proceed():
    clear_console()
    print("""
    Entering: XINGMEN 星门 STARGATE""")

    sleep (2.5)

    print_rainbow_line("""
    One house, one world, one universe divine,""")
    
    sleep (3.5)
    
    print_rainbow_line("""
    Where countless orbs through countless systems shine;""")
    
    sleep (3.5)

    print_rainbow_line("""
    Systems, which view'd throughout the circuit wide,""")
    
    sleep (3.5)

    print_rainbow_line("""
    Or lost, or scarce the pointed sight abide,""")
    
    sleep (3.5)

    print_rainbow_line("""
    Through space immense with diminution seen""")
    
    sleep (3.5)

    print_rainbow_line("""
    Yet boundless to those worlds that roll within;""")
    
    sleep (3.5)

    print_rainbow_line("""
    Each world as boundless to its native race,""")
    
    sleep (3.5)

    print_rainbow_line("""
    That range and wanton through its ample space,""")
    
    sleep (3.5)

    print_rainbow_line("""
    Frequent, through fields, through clouds of fragrance stray,""")
    
    sleep (3.5)

    print_rainbow_line("""
    Or skim the wat'ry or ethereal way.""")
    
    sleep (3.5)

    print_bold("""
    -Henry Brooke""")

    sleep (3.5)

    typingPrint("""
    Engaging localised travel...         
                """)

    choice = input("""
    [Proceed]
    Input:""")
    if choice =='Proceed':
        proximastartgame()
    elif choice =='proceed':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnproceed()

def returnproceed():
    choice = input("""
    Input:""")
    if choice =='Proceed':
        proximastartgame()
    elif choice =='proceed':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnproceed()



###THE ACTUAL GAME BEGINS HERE###

###Change variables###

def update_luck(amount):
    global luck
    luck += amount

def update_diplomacy(amount):
    global diplomacy
    diplomacy += amount

def update_silk(amount):
    global rolls_of_silk
    rolls_of_silk += amount






#Sets genie event to false initially

event_flags ={
    "Trader Event": False
}

#Global variables to hold the current location
localised_location = "XINGMEN 星门 STARGATE EXIT SPHERE"
previous_location = None

#Define locations and their transitions
locations = {
    "XINGMEN 星门 STARGATE EXIT SPHERE": {
        "Nadir": "Ulari Fight",
        "Ram": "Slaver Vessel",  
        "Zenith": "Empty Space",  
        "Starboard": "Trader Room done"   
    },
    "Ulari Fight": {
        "Ram": "XINGMEN 星门 STARGATE EXIT SPHERE",
        "Nadir": "Empty Space", 
        "Zenith": "Empty Space",  
        "Starboard": "Empty Space"    
    },
    "Slaver Vessel": {
        "Ram": "Empty Space",  
        "Nadir": "XINGMEN 星门 STARGATE EXIT SPHERE", 
        "Zenith": "Empty Space",  
        "Starboard": "Empty Space"    
    },
   
    "Empty Space": {
        "Starboard": "XINGMEN 星门 STARGATE EXIT SPHERE",
        "Zenith": "Empty Space",  
        "Nadir": "Empty Space",
        "Ram": "Empty Space"
    },

    "Trader Room done": {
        "Zenith": "XINGMEN 星门 STARGATE EXIT SPHERE",
        "Nadir": "Empty Space",
        "Ram": "Empty Space",
        "Starboard": "Empty Space"
    },

}

def proximastartgame():
    clear_console()
    print(f"""
    Date:08/12/3281                                                                                             
    Coordinates: Galactic Longitude (280.2°), Galactic Latitude (-29.0.°).                                     
    Orbiting Proxima Centauri.                  
    Localised Travel: ONLINE
    Location: {localised_location}
    """)

    choice = input("""
    SHIP:
    [Cargo]
    [Decree]
    [Ship Status]
                   
    TRAVEL: 
    ↑ [Nadir] 
    ↓ [Ram]
    → [Zenith]
    ← [Starboard]   
                           
    Input:""")

    #Handle movement based on localised location
    if choice in locations.get(localised_location, {}):
        update_location(locations[localised_location][choice])
    if choice == 'Cargo':
        proximacargocheck()
    elif choice == 'cargo':
        proximacargocheck()
    elif choice == 'Decree':
        proximadecree()
    elif choice == 'decree':
        proximadecree()
    elif choice == 'Ship Status':
        proximashipstatus()
    elif choice == 'Ship status':
        proximashipstatus()
    elif choice == 'ship status':
        proximashipstatus()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnscreenproximastartgame()

def returnscreenproximastartgame():
    choice = input("""          
    Input:""")

    if choice in locations.get(localised_location, {}):
        update_location(locations[localised_location][choice])
    if choice == 'Cargo':
        proximacargocheck()
    elif choice == 'cargo':
        proximacargocheck()
    elif choice == 'Decree':
        proximadecree()
    elif choice == 'decree':
        proximadecree()
    elif choice == 'Ship Status':
        proximashipstatus()
    elif choice == 'Ship status':
        proximashipstatus()
    elif choice == 'ship status':
        proximashipstatus()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnscreenproximastartgame()  

def update_location(new_location):
    global localised_location, previous_location
    previous_location = localised_location
    localised_location = new_location
    
    
    if localised_location == "Trader Room done":
        if not event_flags["Trader Event"]:
            trader_event_transmission()
        else:
            proximastartgame()

    elif localised_location == "Slaver Vessel":
        shop()

    #Checks if the new location is "Empty Space" and handle accordingly
    elif localised_location == "Empty Space":
        empty_space_menu()
    else:
        proximastartgame()

def empty_space_menu():
    clear_console()
    print(f"""{RED}
                                                                                            
                                                                                        
                ░░░░                                                                    
                                                                                        
                                            ██                                          
                                          ██░░██                                        
  ░░          ░░                        ██░░░░░░██                            ░░░░      
                                      ██░░░░░░░░░░██                                    
                                      ██░░░░░░░░░░██                                    
                                    ██░░░░░░░░░░░░░░██                                  
                                  ██░░░░░░██████░░░░░░██                                
                                  ██░░░░░░██████░░░░░░██                                
                                ██░░░░░░░░██████░░░░░░░░██                              
                                ██░░░░░░░░██████░░░░░░░░██                              
                              ██░░░░░░░░░░██████░░░░░░░░░░██                            
                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          
                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          
                          ██░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░██                        
                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                        
                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      
                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      
                      ██░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██                    
        ░░            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    
                        ██████████████████████████████████████████                      
                                                                                        
                                                                                        
                                                                                        
                                                                                        
    ================================              ░░                                                                    
    *** WARNING : UNSTABLE SPACE ***
    ================================{RESET_COLOUR}
    """)

    choice = input("""
    [Return]
    Input: """)

    if choice == 'Return':
        update_location(previous_location)
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        empty_space_menu_return()

def empty_space_menu_return():
    choice = input("""
    Input: """)

    if choice == 'Return':
        update_location(previous_location)
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        empty_space_menu_return()


###PROXIMA LEVEL CARGO CHECK###
def proximacargocheck():
    clear_console()
    print(f"""
    {rolls_of_silk} katis Keralite silver
    {rolls_of_silk} rolls Tashkent silk 
    {andalusian_oxen} embryos Andalusian oxen 
    """)
    choice = input("""
    [Return]
    Input:""")
    if choice == 'Return':
        proximastartgame()
    elif choice == 'return':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnproximacargocheck()

def returnproximacargocheck():
    choice = input("""
    Input:""")
    if choice == 'Return':
        proximastartgame()
    elif choice == 'return':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnproximacargocheck()

###PROXIMA LEVEL DECREE###
def proximadecree():
    clear_console()
    typingPrint("""
    Royal Decree
          
    By the decree of His Exuberance, Grand Vizier Seraph, Regent of His Majesty, Emperor Angkasa of the 3rd Dynasty, of the Qiang Al-Wijayya Empire,
    This ship shall travel under no degree of hinderance nor encumberance of any foreign parties, in accordance with Galactic Law,
    That it may reach the destination of Aramiz on diplomatic mission swiftly.
    
    Signed,
    
    الوزير الأعظم سيراف""")
    choice = input("""
    [Return]
    Input:""")
    if choice == 'Return':
        proximastartgame()
    elif choice == 'return':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnproximadecree()

def returnproximadecree():
    choice = input("""
    Input:""")
    if choice == 'Return':
        proximastartgame()
    elif choice == 'return':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnproximadecree()  

def proximashipstatus():
    clear_console()
    print("""      
    M CLASS BAOCHUAN EXPLORERᵀᴹ - QIANG AL-WIJAYYA ENGINEERING Ltd.
           
    >> Fusion Core - Healthy
    >> Engine - Healthy
    >> Hull - Healthy
    >> Maneuvering Thrusters - Healthy""")
    choice = input("""
    [Return]
    Input:""")
    if choice == 'Return':
        proximastartgame()
    elif choice == 'return':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnproximashipstatus()

def returnproximashipstatus():
    choice = input("""
    Input:""")
    if choice == 'Return':
        proximastartgame()
    elif choice == 'return':
        proximastartgame()
    else:
        print(f"""{RED}
    ***INVALID INPUT***{RESET_COLOUR}""")
        returnproximashipstatus()


###TRADER EVENT BEGINS HERE###

###TRANSMISSION MESSAGE###
def trader_event_transmission():
    clear_console()
    sleep (0.6)
    print_bold(
        r"""
      ========================        
      *** NEW TRANSMISSION ***
      ========================         
         __________________        
        |\                /|        
        | \              / |         
        | /\____________/\ |         
        |/                \|         
        |__________________|    
        """
    )
    time.sleep(2.0)
    clear_console()
    print_bold(
        r""" 
      ========================             
      *** NEW TRANSMISSION ***
      ========================                
            ____________
           /     _.'\   \\
          /   _.'    \   \\
         /_.-'        \___\\
        |\_\ ``   .-   \ _/|
        |  _\___________.  | 
        | /              \ | 
        |/                \| 
        |__________________|    
        """
    )
    time.sleep(2.0)
    clear_console()
    print_bold(
        r""" 
      ========================       
      *** NEW TRANSMISSION ***
      ========================         
         __________________        
        |\                /|        
        | \              / |         
        | /\____________/\ |         
        |/                \|         
        |__________________|    
        """
    )
    time.sleep(2.0)
    clear_console()
    print_bold(
        r"""
      ========================              
      *** NEW TRANSMISSION ***
      ========================                
            ____________
           /     _.'\   \\
          /   _.'    \   \\
         /_.-'        \___\\
        |\_\ ``   .-   \ _/|
        |  _\___________.  | 
        | /              \ | 
        |/                \| 
        |__________________|    
        """
    )
    time.sleep(2.0)
    trader_event_int()


###GENIE APPEARS###
def trader_event_int():
    clear_console()
    wizard()
    typingPrintwizard("""
    "One is great and One is mighty, I hope I did not give you a little fright-y...?" """)
    sleep (1.0)
    choice = input("""
                   
    [1] "Uhhh ... No?"
    [2] "What ... are you?"
    [3] <Recite Decree>
                   
    Response:""")
    if choice  == '1':
        teo1()
    elif choice == '2':
        teo2()
    elif choice == '3':
        teo5() 
    else:
        returntrader_event_int()

def returntrader_event_int():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice  == '1':
        teo1()
    elif choice == '2':
        teo2()
    elif choice == '3':
        teo5()  
    else:
        returntrader_event_int()

###GENIE SPEECH OPTIONS###
def teo1():
    clear_console()
    wizard2()
    typingPrintwizard("""
    "I'm glad to hear that!" """)
    sleep (1.0)
    choice = input(f"""
    
    [1] "What ... are you?"
    [2] <Recite Decree>
    {RED}[3] <Intimidate>{RESET_COLOUR}
                   
    Response:""")
    if choice  == '1':
        teo2() 
    elif choice == '2':
        teo5()
    elif choice == '3':
        teo9()
    else:
        returnteo1()

def returnteo1():
    typingPrintwizard("""
    "Your response eludes me." """)
    choice = input("""
    Response:""")
    if choice  == '1':
        teo2()
    elif choice == '2':
        teo5()
    elif choice == '3':
        teo9()  
    else:
        returnteo1()

def teo2():
    clear_console()
    wizard16()
    typingPrintwizard("""
    "Some may call me genie, and others djinn. What I truly embody transcends the boundaries of human understanding..." """)
    sleep (1.0)
    choice = input(f"""

    [1] "How are you breathing? We are in the vacuum of space!"                              
    [2] "Back in your bottle! I command you!"
    [3] "A genie, eh? Where's my three wishes?"
    [4] <Recite Decree>
    {RED}[5] <Intimidate>{RESET_COLOUR}
                   
    Response:""")
    if choice == '1':
        teo3()
    elif choice == '4':
        teo5()
    elif choice == '2':
        teo7()
    elif choice == '3':
        teo10()
    elif choice =='5':
        teo9()
    else:
        returnteo2()

def returnteo2():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice  == '1':
        teo3()
    elif choice == '4':
        teo5()
    elif choice == '2':
        teo7()
    elif choice == '3':
        teo10()
    elif choice =='5':
        teo9()
    else:
        returnteo2()

def teo3():
    clear_console()
    wizard15()
    typingPrintwizard("""
    "There is no distance between us. No false veils of time or space may intervene." """)
    sleep (1.0)
    choice = input(f"""
    
     [1] "That's certainly cryptic."
     [2] "Back in your bottle! I command you!"
     [3] <Recite Decree>
     {RED}[4] <Intimidate>{RESET_COLOUR} 
                   
    Response:""")
    if choice == '1':
        teo4()
    elif choice == '3':
        teo5()
    elif choice == '2':
        teo7()
    elif choice =='4':
        teo9()
    else:
        returnteo3()

def returnteo3():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice  == '1':
        teo4()
    elif choice == '3':
        teo5()
    elif choice == '2':
        teo7()
    elif choice =='4':
        teo9()
    else:
        returnteo3()

def teo4():
    clear_console()
    wizard()
    typingPrintwizard("""
    "The essence of truth often eludes those who seek clarity in the dim light of understanding." """)
    sleep (1.0)
    choice = input(f"""
    
     [1] "Back in your bottle! I command you!"
     [2] "... Huh?"
     [3] <Recite Decree>
     {RED}[4] <Intimidate>{RESET_COLOUR} 
                   
    Response:""")
    if choice == '1':
        teo7()
    elif choice == '2':
        teo2()
    elif choice == '3':
        teo5()
    elif choice == '4':
        teo9()
    else:
        returnteo4()

def returnteo4():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice == '1':
        teo7()
    elif choice == '2':
        teo2()
    elif choice == '3':
        teo5()
    elif choice == '4':
        teo9()
    else:
        returnteo4()

def teo5():
    clear_console()
    sleep (1.0)
    print_bold("""
    *AHEM*""")
    sleep (0.8)
    clear_console()
    typingPrintcinematic("""
    "Royal Decree.
          
    By the, um, decree of His Exuberance, Grand Vizier Seraph, Regent of His, uh, Majesty, Emperor Angkasa of the third Dynasty, 
    of the Qia-" """)
    clear_console()
    wizard16()
    typingPrintwizard("""
    "Bah! The law and folly of mankind bear no weight upon my existence, for I am untouched by their transient whims." """)
    sleep (1.0)
    choice = input("""

    [1] "Emperor Angkasa could have you executed for such treason!"
    [2] "... Huh?"

    Response:""")
    if choice == '1':
        teo6() 
    elif choice == '2':
        teo2()
    else:
        returnteo5()

def returnteo5():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice == '1':
        teo6()
    elif choice == '2':
        teo2() 
    else:
        returnteo5()

def teo6():
    clear_console()
    wizard4()
    typingPrintwizard("""
    "I have no physical form. Such an act can never transpire." """)
    sleep (1.0)
    choice = input(f"""

    [1] "What ... are you?"
    [2] "... Huh?"
    {RED}[3] <Intimidate>{RESET_COLOUR}

    Response:""") 
    if choice == '1':
        teo2()
    elif choice == '2':
        teo2()
    elif choice == '3':
        teo9()
    else:
        returnteo6()

def returnteo6():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice == '1':
        teo2()
    elif choice == '2':
        teo2()
    elif choice == '3':
        teo9()
    else:
        returnteo6()

def teo7():
    clear_console()
    wizard4()
    typingPrintwizard("""
    "Is that one of your three wishes? This is no bottle, but merely a lamp." """)
    sleep (1.0)
    choice = input(f"""

    [1] "Lemme get my three wishes."
    [2] "Whatever. Save the waffle for the Galactic Poetry Competition."
    [3] "Cram it Shakespeare! This is the 33rd century, not the 13th."
    [4] "O wise one, thou art infinite in thy knowledge and splendour."
    {RED}[5] <Intimidate>{RESET_COLOUR}

    Response:""")
    if choice == '1':
        teo10()
    elif choice == '2':
        teo11()
    elif choice == '3':
        teo8()
    elif choice == '4':
        teo11()
    elif choice == '5':
        teo9()
    else:
        returnteo7()
    
def returnteo7():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice == '1':
        teo10()
    elif choice == '2':
        teo11()
    elif choice == '3':
        teo8()
    elif choice == '4':
        teo11()
    elif choice == '5':
        teo9()
    else:
        returnteo7()

def teo8():
    clear_console()
    wizard2()
    typingPrintwizard("""
    "I thank you for your benevolent words! Though I am no Shakespeare... He lived during the 16th century.
    I exist outside of Time and Space..." """)
    sleep (1.0)
    choice = input(f"""

    [1] "Bard, schmard. Where's my wishes, genie?"
    [2] "O wise one, I thank thee for thy words of enlightenment."
    {RED}[3] <Intimidate>{RESET_COLOUR}

    Response:""")
    if choice == '1':
        teo10()
    elif choice == '2':
        teo11()
    elif choice == '3':
        teo9()
    else:
        returnteo8()

def returnteo8():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice == '1':
        teo10()
    elif choice == '2':
        teo11()
    elif choice == '3':
        teo9()
    else:
        returnteo8()


def teo9():
    clear_console()
    wizard5()
    typingPrintwizardmad("""
    "You have spoken most unwisely." """) 
    sleep (1.0)
    typingPrintwizardmad("""
                      
    "A soft answer turns away wrath, but a harsh word stirs up anger." """)
    sleep (1.0)
    typingPrintwizardmad("""
                      
    "Think upon your actions before you offend a genie." """)
    sleep (2.5)

    update_luck(-10)
    update_diplomacy(-10)
    clear_console()
    wizard6()
    sleep (1.0)
    clear_console()
    wizard7()
    sleep (1.0)
    clear_console()
    wizard8()
    sleep (1.0)
    clear_console()
    wizard9()
    sleep (1.0)
    clear_console()
    wizard10()
    sleep (1.0)
    clear_console()
    wizard11()
    sleep (1.0)
    clear_console()
    wizard12()
    sleep (1.0)
    clear_console()
    wizard13()
    sleep (1.5)
    clear_console()
    sleep (1.5)
    trader_event_transmission_end()
    sleep (1.5)
    event_flags["Trader Event"] = True
    update_location("Trader Room done")

def teo10():
    clear_console()
    wizard14()
    typingPrintwizard("""
    "How about instead of three wishes, I grant you three riddles?" """)
    sleep (1.0)
    choice = input(f"""

    [1] "I don't have a choice, do I?"
    {RED}[2] <Intimidate>{RESET_COLOUR}

    Response:""")
    if choice == '1':
        teo12()
    elif choice == '2':
        teo9()
    else:
        returnteo10()

def returnteo10():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice == '1':
        teo12()
    elif choice == '2':
        teo9()
    else:
        returnteo10()

def teo11():
    clear_console()
    wizard3()
    typingPrintwizard("""
    "You are a rambunctious one! How about instead of three wishes, I test you with three riddles?" """)
    sleep (1.0)
    choice = input(f"""

    [1] "I don't have a choice, do I?"
    [2] "No. I want the wishes."
    {RED}[3] <Intimidate>{RESET_COLOUR}

    Response:""")
    if choice == '1':
        teo12()
    elif choice == '2':
        teo12()
    elif choice == '3':
        teo9()
    else:
        returnteo11()

def returnteo11():
    typingPrintwizard("""
    "Your response eludes me."
                       """)
    choice = input("""
    Response:""")
    if choice == '1':
        teo12()
    elif choice == '2':
        teo12()
    elif choice == '3':
        teo9()
    else:
        returnteo11()


def teo12():
    clear_console()
    wizard15()
    typingPrintwizard("""                     
    "Choice is but an illusion." 
                      """)
    sleep (1.0)
    typingPrintwizard("""
    "I speak without a mouth and hear without ears. I have no body but I come alive with the wind.
    What am I?" """)
    choice = input(""" 
                                    
    Response:""")
    if choice == 'an echo':
        teo13()
    elif choice == 'echo':
        teo13()
    elif choice == 'An echo':
        teo13()
    elif choice == 'ECHO':
        teo13()
    elif choice == 'echoes':
        teo13()
    elif choice == 'the echo':
        teo13()
    elif choice == 'you are an echo':
        teo13()
    else:
        teowronganswer()

def teo13():
    clear_console()
    wizard4()
    typingPrintwizard("""                     
    "You carry the light of insight within. Let us continue." 
                      """)
    typingPrintwizard("""
    "I can fly without wings. I can cry without eyes. Whenever I go, darkness flies.
    What am I?" """)
    choice = input(""" 
                                    
    Response:""")
    if choice == 'a cloud':
        teo14()
    elif choice == 'cloud':
        teo14()
    elif choice == 'CLOUD':
        teo14()
    elif choice == 'clouds':
        teo14()
    elif choice == 'A cloud':
        teo14()
    elif choice == 'the cloud':
        teo14()
    elif choice == 'you are a cloud':
        teo14()
    elif choice == 'A Cloud':
        teo14()
    else:
        teowronganswer()


    

def teo14a():
    clear_console()
    wizard15()
    typingPrintwizard("""                     
    "I pose to you now the final question:" 
    """)
    sleep (1.0)
    typingPrintwizard("""
    "Which club has won the most Premier League titles?" """)
    sleep (1.0)
    choice = input("""

    [1] Manchester United
    [2] Tottenham Hotspur
    [3] Preston North End
                   
    Response:""")
    if choice == '1':
        teo15()
    else:
        teowronganswer()

def teo14b():
    clear_console()
    wizard15()
    typingPrintwizard("""                     
    "I pose to you now the final question:" 
    """)
    sleep (1.0)
    typingPrintwizard("""
    "Who famously missed a penalty in the 1996 Euro semi-final against Germany?" """)
    sleep (1.0)
    choice = input("""

    [1] Steven Gerrard
    [2] David Beckham
    [3] Ricky Gervais
    [4] Sarah Silverman
                   
    Response:""")
    if choice == '2':
        teo15()
    else:
        teowronganswer()

def teo14c():
    clear_console()
    wizard15()
    typingPrintwizard("""                     
    "I pose to you now the final question:" 
    """)
    sleep (1.0)
    typingPrintwizard("""
    "In what year did England win the FIFA World Cup?" """)
    sleep (1.0)
    choice = input("""

    [1] Never gonna happen again, mate
    [2] Have they ever? Can't remember...
    [3] Will they ever win another?
    [4] 1966
    [5] 2788
    [6] It was never coming home...
                   
    Response:""")
    if choice == '4':
        teo15()
    else:
        teowronganswer()


teofinalquestions = [teo14a, teo14b, teo14c]

                      

def teo14():
    selectedteofinalquestion = random.choice(teofinalquestions)
    print(selectedteofinalquestion())

def teo15():
    clear_console()
    wizard2()
    typingPrintwizard("""
    "It seems that fate has favoured you today! I extend my praise to you, O human!" """)
    sleep (1.0)
    choice = input("""

    [1] "Cool. Now where's my wishes."
    [2] "Clock's ticking bozo. Still waiting on them wishes."
    [3] "O wise one, I request of thee my three wishes."
    
    Response:""")
    if choice == '1':
        teorightanswer()
    elif choice == '2':
        teorightanswer()
    elif choice == '3':
        teorightanswer()
    else:
        returnteo15()
    
def returnteo15():
    typingPrintwizard("""
    "Your response brings a delightful air of mystery!"
                       """)
    choice = input("""
    Response:""")
    if choice == '1':
        teorightanswer()
    elif choice == '2':
        teorightanswer()
    elif choice == '3':
        teorightanswer()
    else:
        returnteo15()

def teorightanswer():
    clear_console()
    wizard16()
    typingPrintwizard("""
    "I have no wishes to give, but bestow upon you the Gift of The Gab."
    """)
    sleep (1.0)
    typingPrintwizard("""
    "Well-spoken words are like golden apples in a silver setting." 
    """)
    sleep (1.0)
    typingPrintwizard("""
    "I bid you farewell on your travels!" """)
    sleep (2.0)
    update_diplomacy(+10)
    update_luck(+10)
    teoanswerendsequence()

def teowronganswer():
    clear_console()
    wizard14()
    typingPrintwizard("""
    "It seems that fate has not favoured you today..."
    """)
    sleep (1.0)
    typingPrintwizard("""
    "I bid you farewell on your travels." """)
    sleep (2.0)
    teoanswerendsequence()

def teoanswerendsequence():
    clear_console()
    wizard6()
    sleep (1.0)
    clear_console()
    wizard7()
    sleep (1.0)
    clear_console()
    wizard8()
    sleep (1.0)
    clear_console()
    wizard9()
    sleep (1.0)
    clear_console()
    wizard10()
    sleep (1.0)
    clear_console()
    wizard11()
    sleep (1.0)
    clear_console()
    wizard12()
    sleep (1.0)
    clear_console()
    wizard13()
    sleep (1.5)
    clear_console()
    sleep (1.5)
    trader_event_transmission_end()
    sleep (1.5)
    event_flags["Trader Event"] = True
    update_location("Trader Room done")



###SHOP SEQUENCE###

def shop():
    clear_console()
    shop_transmission()
    clear_console()
    shop1()
    typingPrintshop("""
    "Care to purchase ... or don't. Not really bothered ... innit."
    """)
    typingPrintshop2("""
    "Ignore my partner. We're just simple traders trying to make a living. Feel free to browse."
    """)
    



if __name__ == "__main__":
    start_game()
