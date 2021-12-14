import time
import sys
import random #import libs we need to use

################this section for daniels boss battle###########
health=3                  #our hp for dans boss battle
karenhealth=3             #karens hp for dans boss battle
basket = [                #basket of items-list for dans boss battle
        "beans",
        "beans",
        "milk",
        "banana",
        "banana",
        "cheese",
        "egg",
        "egg",
        "egg",
        "egg",
        "egg",
        "egg",
        "melon"
        ]

def start_game():     #this function will run first every time the game is started/restarted
    print("Welcome \n")
    time.sleep(1)
    print("To \n")
    time.sleep(1)
    print("""\033[3;33;41m
​
                                            )                                      (                        
                                        ( /(                               (      )\ )        (            
                                        )\())        (        )        )   )\    (()/(   (    )\ )     (   
                                        ((_)\    (    )(      (      ( /(  ((_)    /(_))  )\  (()/(    ))\  
                                        _((_)   )\  (()\     )\  '  )(_))  _     (_))   ((_)  /(_))  /((_) 
                                        | \| |  ((_)  ((_)  _((_))  ((_)_  | |    | |     (_) (_) _| (_))   
                                        | .` | / _ \ | '_| | '  \() / _` | | |    | |__   | |  |  _| / -_)  
                                        |_|\_| \___/ |_|   |_|_|_|  \__,_| |_|    |____|  |_|  |_|   \___|                                                                 
                                                        
    \033[0;0m""")    #title screen ascii produced by graham
    time.sleep(2)
    input("Press Enter to wake up \n")
    bed()

def game_over(): #game over function and ascii
    print("""\n  .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....                  GAME
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....                   OVER
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................""")
    time.sleep(2)
    game_over2()

def game_over2():  #2nd game over ascii, split the function for user input purposes, so wrong answer wouldn't reprint everything else
    global basket  #daniel also added his list repopulation and stat renewal values here so they would reset when you restarted the game 
    global health
    global karenhealth
    print("\nWould you like to try again?")
    answer1=input("Type \033[1;32;40myes\033[0;0m or \033[1;31;40mno\033[0;0m: \n") #red and green used as colors for yes and no
    while "yes" in answer1.lower():                                                 #this will be a recurring theme throughout the game
        health=3                                                                    #for UX purposes
        karenhealth=3
        basket = [
        "beans",
        "beans",
        "milk",
        "banana",
        "banana",
        "cheese",
        "egg",
        "egg",
        "egg",
        "egg",
        "egg",
        "egg",
        "melon"
        ]
        start_game()
    while "no" in answer1.lower():
        print("You have left the game.")
        sys.exit()

def bed(): #opening function after start game, gives the user a random reason for waking up, making for a roguelike quality
    bedanswer=random.randint(1,8) #randomizes a number between 1 and 8, and picks an answer accordingly
    if bedanswer ==1:
        print("You are awoken by the sound of somebody using electric hedgetrimmers...\n")
        time.sleep(3.5)
        bed2()
    elif bedanswer ==2:
        print("You are awoken by the sound of somebody beeping their car horn repeatedly...\n")
        time.sleep(3.5)
        bed2()
    elif bedanswer ==3:
        print("You are awoken by the sound of your neighbour's jacuzzi clean cycle...\n")
        time.sleep(3.5)
        bed2()
    elif bedanswer ==4:
        print("You are awoken by the clatter of wheelie bins outside...\n")
        time.sleep(3.5)
        bed2()
    elif bedanswer ==5:
        print("You are awoken by the sound of screaming children outside...\n")
        time.sleep(3.5)
        bed2()
    elif bedanswer ==5:
        print("You are awoken by the sound of a wailing car alarm...\n")
        time.sleep(3.5)
        bed2()
    elif bedanswer ==5:
        print("You are awoken by the sound of ambulance sirens...\n")
        time.sleep(3.5)
        bed2()
    else: 
        bedanswer ==8
        print("You are awoken by the incessant barking of a neighbour's dog...\n")
        time.sleep(3.5)
        bed2()

def bed2(): #typically all the functions will be written in this format
    print("Would you like to get out of bed?\n") #Question
    time.sleep(1.5) #Simulate Delay
    answer2=input("Type \033[1;32;40myes\033[0;0m or \033[1;31;40mno\033[0;0m: \n") #Input for response, color coded for UX
    while "yes" in answer2.lower(): #While loops reduce the need for user error control, for text anyway
        drink()                     #The loops simply won't be allowed to continue if an input is incorrect
    while "no" in answer2.lower():  #answer.lower translates all answers to lowercase inputs, more error correction
        spider()
    else:
        bed()

def drink():
    print("\nYou let out a large yawn...\n")
    time.sleep(1.5)
    print("stretch out your arms...\n")
    time.sleep(1.5)
    print("...and immediately knock over the glass of\033[2;33;40m orange juice\033[0;0m that was sitting on your bedside table.\n")
    time.sleep(2)
    drink2()

def drink2():
    print("Would you like to clean up the\033[2;33;40m orange juice\033[0;0m ?\n")
    time.sleep(1)
    answer3=input("Type \033[1;32;40myes\033[0;0m or \033[1;31;40mno\033[0;0m: \n")
    while "yes" in answer3.lower():
        dog_towel()
    while "no" in answer3.lower():
        ants() #most functions call 1 of 2 other functions at the end of the loop, here goes to ants
    else:
        drink2() #here restarts the initial question in case user inputs wrong too many times and loses the text off the screen

def dog_towel():
    print("\nWhat would you like to use to clean up the\033[2;33;40m orange juice\033[0;0m ?\n") #use of orange to color orange juice
    time.sleep(1.5)
    print("\033[38;5;207mTowel\033[0;0m? \n")
    time.sleep(1)
    answer4=input("Or \033[38;5;202mDog\033[0;0m? \n")
    while "towel" in answer4.lower():
        print("\nYou mop up the\033[2;33;40m orange juice\033[0;0m with a nearby towel, congratulations, your towel now smells of carpet and\033[2;33;40m orange juice\033[0;0m. \n")
        time.sleep(6)
        toast()
    while "dog" in answer4.lower():
        print ("\nYou use your dog to mop up the\033[2;33;40m orange juice\033[0;0m \n")
        time.sleep(2)
        print ("The dog deems this use of his temporary existence acceptable..\n")
        time.sleep(2.5)
        print ("..and wags his tail...\n")
        time.sleep(1.5)
        print ("...joyfully...\n")
        time.sleep(2)
        toast()

def spider():
    print("\nYou decide that staying in bed might be the wiser decision, on this particular day..\n")
    time.sleep(3)
    print("You rub your feet together under your duvet\n")
    time.sleep(2)
    print("...and let out a long yawn...\n")
    time.sleep(2)
    print("              (")
    print("               )")
    print("              (")
    print("        /\  .-----.  /\\")
    print("       //\\/  ,,,  \//\\")
    print("       |/\| ,;;;;;, |/\|")
    print("       |/\| ,;;;;;, |/\|")
    print("       //\\\;-----; |/\|")
    print("      //  \/   .   \/  \\")
    print("     (| ,-_| \ | / |_-, |)")
    print("       //`__\.-.-./__`\\")
    print("      // /.-(() ())-.\ \/")
    print("      // /.-(() ())-.\ \\")
    print("     (\ |)   '---'   (| /)")
    print("     (\ |)   '---'   (| /)")
    print("      ` (|           |) `")
    print("      ` (|           |) `")
    print("        \)           (/")
    print("A spider, promptly falls into your open mouth..\n")
    time.sleep(3)
    spider2()

def spider2():
    print("\n\033[38;5;105mSpit\033[0;0m the spider out?\n")
    time.sleep(1)
    answer5=input("Or \033[1;31;40mswallow\033[0;0m the spider? \n")
    while "spit" in answer5.lower():
        print("\nYou spit the spider out in disgust\n")
        time.sleep(2.5)
        print("                             :            :")
        print("                             :            :")
        print("                             :            :")
        print("                             :            :")
        print("                            .'            :")
        print("                            .'            :")
        print("                    _.- .                 '.")
        print("    ..__...____...-.                       :")
        print("   : \_\                                    :")
        print("   :    .--.                                 :")
        print("   `.__/  .-. _                               :")
        print("      /  /  ,. ,-                            .'")
        print("     (_)(`,(_,'L_,_____       ____....__   _.'")
        print("      ,' ,             .......          ...          ")
        print("It runs under your duvet, freaking you out, and forcing you to evacuate your bed in such a way that you also stub your toe on your bedside table.. \n")
        time.sleep(6)
        toast() 
    while "swallow" in answer5.lower():
        print("You swallow the spider\n")
        time.sleep(1.5)
        print("Mmmmmm...\n")
        time.sleep(1)
        print("Chewy...\n")
        time.sleep(1)
        print("Poisonous...\n")
        time.sleep(1)
        print("You died as a result of spider venom\n")
        time.sleep(2.5)
        game_over()
    else:
        spider2()

def ants():
    print("\nYou leave the juice soaking into the carpet..\n")
    time.sleep(2)
    print("A large colony of Ants appear..\n")
    time.sleep(2)
    print("They devour the juice before swarming over you..\n")
    time.sleep(2)
    print("You are eaten alive..\n")
    time.sleep(2)
    print("..by Ants\n")   #play the game wrong results in death, it's that simple, there are several instances of this throughout
    time.sleep(1.5)        #the game. Used as a mechanic to make the user think more carefully about the situations they encounter
    game_over()         

def toast():
    print("\nYou decide to make some breakfast \n")
    time.sleep(1.5)
    print("You put some bread into the toaster and turn the kettle on \n")
    time.sleep(2)
    print("What setting would you like to put the toaster on?")
    time.sleep(1.5)
    while True:             #This true loop was used as a way to combat user text input instead of entering a number
        try:
            question = int(input("Enter a number from 1-6 \n"))
            break
        except:
            print("That's not a valid option! \n")
    while question >0 and question <=3:          #used to 'if else' a user integer input so they cant type text in and error out the game
        tea()
    while question <=6:
        smoke_alarm()
    else:
        toast()   #force the question again in case of user inputting wrong answer and losing original question

def smoke_alarm():
    print("\nOh dear..\n")
    time.sleep(1)
    print("The toast has become stuck in the toaster, burnt and set off the smoke alarm.\n")
    time.sleep(3)
    smoke_alarm2()

def smoke_alarm2():
    print("\nWould you like to try and remove the toast with a fork? You have a 50/50 chance of electrocuting yourself.. \n")
    answer6=input("Type \033[1;32;40myes\033[0;0m or \033[1;31;40mno\033[0;0m: \n")
    while "yes" in answer6.lower():       
        fork()
    while "no" in answer6.lower():
        print("\nYou leave the toast in the toaster and it, inevitably, ends up on fire, and burns your house down with you in it.\n")
        time.sleep(5)
        print("Unlucky...\n") #this function written as a random chance to kill the player, goes to next function fork to roll dice
        time.sleep(1)
        game_over()
    else:
        smoke_alarm2()

def fork():
    print("\nYou jam a fork into the toaster in an attempt to remove the burning toast..\n")
    time.sleep(4)
    print("\033[3;37;40mThat's strange...you could have sworn you just heard somebody rolling a dice...?\033[0;0m \n")
    time.sleep(4)
    answer7=random.randint(1,6)
    if answer7 >0 and answer7 <=3: #first dice roll function, added as a dnd element similar to rpg
        print("Phew...\n")         #this is where i first learned to randomize outcomes
        time.sleep(1)
        print("..you survived..\n")
        time.sleep(1)
        tea()
    else: 
        answer7 <=6
        print("Unfortunately, the odds didn't roll in your favour...\n")
        time.sleep(2)
        print("You have suffered death by\033[1;36;40m electrocution\033[0;0m \n")
        time.sleep(2)
        game_over()

def tea():
    print("\nCongratulations!\n")
    time.sleep(1)
    print("The toast appears to be edible.\n")
    time.sleep(2)
    print("You go to make some tea...\n")
    time.sleep(2)
    print("""                   (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /;                             ;
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     -------.....______.....-------     _.'
          `""--..,,_____            _____,,..--""`
                        `----------`
​
""")
    print("...but, you don't have any milk...\n")
    time.sleep(3)
    tea2()

def tea2(): #this function was made to give the user no choice at all, both paths lead the same way
    print("\nWould you like to drink your tea without milk?\n") #one of many lessons in futility
    time.sleep(2.5)
    print("Like some kind of freak?\n")
    time.sleep(2)
    answer8=input("Type \033[1;32;40myes\033[0;0m or \033[1;31;40mno\033[0;0m: \n")
    while "yes" in answer8.lower():
        blacktea()
    while "no" in answer8.lower():
        pavement()
    else:
        tea2()

def blacktea():
    print("\nYou decide to drink the tea without milk..\n")
    time.sleep(3)
    print("...it isn't very nice...\n")
    time.sleep(2)
    pavement()

def dice_roll():       #dice roll function refined for a further encounter
    num=random.randint(1,6)
    print("\nIf the dice rolls 1-3, you win\n")
    time.sleep(2)
    print("If the dice rolls 4-6, you lose\n")
    time.sleep(2)
    if num >0 and num <=3:
        print(f"The dice rolled a {num}\n")
        time.sleep(2)
        print("You have succeeded in persuading the man to never come between a person and their milk..\n")
        time.sleep(4)
        shop()
    else:
        num <=6
        print("Oh dear...\n")
        time.sleep(1)
        print(f"The dice rolled a {num}\n")
        time.sleep(2)
        print("You have succumbed to the mans furious thrashing\n")
        time.sleep(2)
        game_over()

def fight_flight():
    print("\033[1;31;40mFight?\033[0;0m")
    time.sleep(0.5)
    answer9=input("or \033[1;34;40mFlight?\033[0;0m\n")
    while "fight" in answer9.lower():
        print("\nYour attempt to subdue the individual has a 50/50 chance of success. Maybe you should have ran away...\n")
        time.sleep(5)
        dice_roll()
    while "flight" in answer9.lower():
        print("\nYou made the very wise decision to simply circumvent this particular obstacle, and run away towards your original objective\n")
        time.sleep(5)
        shop()
    else:
        fight_flight()

def pavement(): #originally this was one massive function with loops within loops but caused too many issues so had to be split into 
    print("\nYou have decided to walk to the shop to buy milk\n") #smaller chunks
    time.sleep(3)    
    print("As you walk along the pavement, towards the supermarket, you can see a man approaching you in the distance..\n")
    time.sleep(4)
    print("He is 100 meters away\n")
    time.sleep(1)
    answer10=input("In an attempt to avoid the man, would you like to move \033[2;33;40mleft\033[0;0m or \033[38;5;105mright\033[0;0m? \n")
    while "left" in answer10.lower():
        print("\nYou have moved to the left.\n")
        time.sleep(1)
        print("The man has moved to the right, he is now 50 meters away.\n")
        time.sleep(2.5)
        pavement_left()
    while "right" in answer10.lower():
        print("\nYou have moved to the right.\n")
        time.sleep(1)
        print("The man has moved to the left, he is now 50 meters away.\n")
        time.sleep(2.5)
        pavement_right()

def pavement_left():
    print("In a further attempt to avoid the man, would you like to move back to your right? \n")
    answer11=input("Type \033[1;32;40myes\033[0;0m or \033[1;31;40mno\033[0;0m: \n")
    while "yes" in answer11.lower():
        print("\nYou have moved back to the right")
        time.sleep(1)
        print("The man has moved back to the left, he is now stood directly in your way, obstructing your path.\n")
        time.sleep(2.5)
        print("Typically, he's one of these types who seems set on ruining another person\'s day...\n")
        time.sleep(2.5)
        fight_flight()
    while "no" in answer11.lower():
        print("\nYou are resolute in your decision to continue moving forwards, hoping the oncoming individual will step aside and let you pass..\n")
        time.sleep(4)
        print("....he doesn't....\n")
        time.sleep(1)
        fight_flight()

def pavement_right():
    print("In a further attempt to avoid the man, would you like to move back to your left? \n")
    answer12=input("Type \033[1;32;40myes\033[0;0m or \033[1;31;40mno\033[0;0m: \n")
    while "yes" in answer12.lower():
        print("\nYou have moved back to the left.\n")
        time.sleep(1)
        print("The man has moved back to the right, he is now stood directly in your way, obstructing your path.\n")
        time.sleep(2.5)
        print("Typically, he's one of these types who seem set on ruining another person\'s day...\n")
        time.sleep(2.5)
        fight_flight()
    while "no" in answer12.lower():
        print("\nYou are resolute in your decision to continue moving forwards, hoping the oncoming individual will step aside and let you pass..\n")
        time.sleep(4)
        print("...he doesn't...")
        time.sleep(1)
        fight_flight()

def shop():
    print("You arrive at the supermarket, there doesn't seem to be a queue..\n")
    time.sleep(2)
    print("You take some milk from the nearby fridge and head towards the checkout\n")
    time.sleep(3)
    print("""                      .&dkl`,ivne._
                      sRfkgvc+rsnmGBND.
                    aHBNLbni+.irumLGNMms
                    NRIr`'+dLKNMFb`'iNQr
                   `ANWM7    `+lM0.  `'^Kl
                   iNWL*_;=e.     Y._,_ ON
                   aRNm   _.l,    j^ _` Bq,
                   eNL:,l=N0`.   ls`N0> ibK
                   XHZu!       _(c      kPBN
                    'CD   .     `      tK7KX
                      'f     _&zrc_.  .Y
 ,                      v,   `ta.="  ,V
7q. 6%                   ^l     =   .r
f'noib. +                `d+   .._a7                     t
k+RD6 L.dr                h'  `*+iPb                  .f adI`
dj+Ggr 4NJb            .,dT     `'KJc                 _ir+4b .
  `cl^ ._ tk.   .,&;:rf"t&;       'yIKbr;.         dp` luhrZti
     `~.  ^_T `ysf'      " n,     7     *lkr,.   i7k._m.JKiV"
        J  .H dY   `"-              ._``    "VK,4=   . Kdj`
        K   K B               -s&.            eJ+  .ys7^`
        T   lLj                               (C' .4
        P   'y    .,                      .   +j  7""")
    print("A WILD KAREN HAS APPEARED!\n")
    time.sleep(3.5)
    print('Without hesistation or consideration, "Karen", interjects herself between you and the cashier\n')
    time.sleep(4)
    print("You realise she's trying to return an inflatable mattress she purchased several months ago..\n")
    time.sleep(4)
    print("and no...\n")
    time.sleep(1)
    print("she doesn't have a receipt..\n")
    time.sleep(2)
    print("...nor is the cashier convinced that they ever sold inflatable mattresses...\n")
    time.sleep(3)
    print("You politely interject yourself into the ensuing conversation and ask \'Karen\' if she wouldnt mind just letting you pay for your milk...\n")
    time.sleep(6)
    print("Unreceptive, she turns back and continues her tirade towards the cashier...\n")
    time.sleep(2.5)
    typing_print("You feel a sudden and violent rage begin to overwhelm you from within..\n")
    time.sleep(3)
    boss_fight()

def boss_fight():
    print('''                                        ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (  /_L\.
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /               BOSS
                   \/`  `,   `   ,`  | /__,.-`    _,   `\                 FIGHT!
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \.
                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \.
              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\ V   V, /`     /
   ,--\(        ,     <_/`\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-` \n''')
    time.sleep(3)
    print("\n\033[3;37;40m'Cue Music...'\033[0;0m \n") #use of italics to break the fourth wall, this happens a few times
    time.sleep(2)                                      #in this instance, to make you think of boss level music
    karen()

def karen():
    print("You attempt to push in front of Karen in a final, desperate, effort to pay for your milk...\n")
    time.sleep(3.5)
    print("This violation of Karen\'s personal space redirects her frenzy towards you...\n")
    time.sleep(3)
    input("Press Enter to fight for your milk.. \n")
    attack_split()
    

def attack_split(): #this randomizes one of 2 possible boss fight scenarios wrtitten separately by dan and jamie
    num=random.randint(1,6)
    if num >0 and num <=3:
        typing_print("\n\033[3;37;40mThinking..\033[0;0m") #italics to break fourth wall and give illusion of system being in control
        print("\n\033[3;37;40m...AI has chosen Jamie's, autoscroller, boss fight scenario\033[0;0m") 
        time.sleep(1)
        attack1()
    else:
        num <=6
        typing_print("\n\033[3;37;40mThinking..\033[0;0m")
        print("\n\033[3;37;40m...AI has chosen Daniel's, interactive, boss fight scenario\033[0;0m")
        time.sleep(1)
        dan_boss()

def attack1(): #the start of jamie's boss fight, each attack leads to another, specific attack based on score
    num=random.randint(1,6) #the first to 3 hits, karen or user, wins the game
    if num >0 and num <=3: #there is a flowchart i created to show how the attacks interact with each other
        print("\nKaren lands the first attack, a textbook slap to the face...\n")
        time.sleep(3)
        print("You prepare to retaliate..\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack3()
    else:
        num <=6
        print("\nKaren misses her first attack, and is left open for retalliation...\n")
        time.sleep(3.5)
        print("You land your first blow, a crunching right hook into her lower abdomen...\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack2()

def attack2():
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Karen lands her first attack, a textbook slap to the face...\n")
        time.sleep(2.5)
        print("You prepare to retaliate..\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack8()
    else:
        num <=6
        print("Karen doubles over in pain from being whacked in the stomach...\n")
        time.sleep(2.5)
        print("You issue a follow up attack, a swift kick to the shins.. \n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack5()

def attack3():
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Karen laughs at you... \n")
        time.sleep(2.5)
        print("Mockingly, she exclaims how much weaker you are than her nephew,\'Kyle\'... \n")
        time.sleep(3.5)
        print("You feel utterly demoralised...\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack4()
    else:
        num <=6
        print("Karen attempts to mock you by exclaiming how much weaker you are than her nephew,\'Kyle\'... \n")
        time.sleep(4.5)
        print("You land your first blow, a crunching right hook into her lower abdomen\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack8()

def attack4():
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Karen raises her purse in the air...\n")
        time.sleep(2)
        print("And brings it crashing down onto your skull.\n")
        time.sleep(2.5)
        print("You didn't stand a chance..")
        time.sleep(2.5)
        print("You collapse in agony..")
        time.sleep(2)
        lose()
    else:
        num <=6
        print("Karen attempts to hit you with her purse...\n")
        time.sleep(2.5)
        print("You deftly sidestep the attack..\n")
        time.sleep(2.5)
        print("And administer an almighty slap to the back of her head.\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack7()

def attack5():
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Karen lands a whirling elbow, directly into your cranium.. \n")
        time.sleep(3.5)
        print("You prepare to retaliate..\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack9()
    else:
        num <=6
        print("Karen is simply flailing around aimlessly...\n")
        time.sleep(2.5)
        print("It would seem that she doesn't know how to fight..\n")
        time.sleep(2.5)
        print("...at all...\n")
        time.sleep(1.5)
        print("You grab Karen by the hair, and slam her face down into the counter.\n")
        time.sleep(3.5)
        print("She slithers down on to the floor, utterly defeated.\n")
        time.sleep(3)
        print("Both you and the cashier throw your arms towards the sky in victory!\n")
        time.sleep(3.5)
        win()  

def attack7():
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Unperturbed by your intial aggression, Karen quickly spins around... \n")
        time.sleep(3.5)
        print("Using the momentum of the spin...\n")
        time.sleep(2)
        print("She smashes her purse into the side of your face...\n")
        time.sleep(2.5)
        print("You collapse in agony..\n")
        time.sleep(2)
        lose()
    else:
        num <=6
        print("You're trading blow for blow!\n")
        time.sleep(2)
        print("You send a punch back towards Karens right eye..\n")
        time.sleep(2.5)
        print("..it connects...dramatically...\n")
        input("Press Enter to continue.. \n")
        attack10()

def attack8():
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Karen isn't taking that lightly...\n")
        time.sleep(1.5)
        print("She directs a kick towards your gentlemen\'s vegetables..\n")
        time.sleep(3)
        print("It connects..\n")
        time.sleep(1.5)
        print("...with a crunch..\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack7()
    else:
        num <=6
        print("You're on a roll!\n")
        time.sleep(1.5)
        print("You follow up with a flying knee directed towards Karen\'s sternum...\n")
        time.sleep(2.5)
        print("...it connects, satisfyingly...\n")
        time.sleep(2)
        print("...she gasps for air..\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack9()

def attack9():
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Karen isn't ready to throw the towel in just yet..\n")
        time.sleep(2.5)
        print("She ripostes by jabbing a finger into your left eye..\n")
        time.sleep(3.5)
        print("...her brightly painted and freshly manicured fingernail breaks off...\n")
        time.sleep(3.5)
        print("...and remains attached to your eyeball...\n")
        time.sleep(2)
        input("Press Enter to continue.. \n")
        attack10()
    else:
        num <=6
        print("You seize the opportunity to end the fight..\n")
        time.sleep(2.5)
        print("You bring your elbow down on to the top of Karen\'s head.\n")
        time.sleep(3.5)
        print("She slithers down on to the floor, utterly defeated.\n")
        time.sleep(3.5)
        print("Both you and the cashier throw your arms towards the sky in victory!\n")
        time.sleep(2.5)
        win()

def attack10():
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("You start to feel dazed and confused.. \n")
        time.sleep(2)
        print("Karen grabs the cashiers nearby pricing gun and hurls it towards your face..\n")
        time.sleep(4.5)
        print("Unable to judge the distance or speed at which this object is flying towards you...\n")
        time.sleep(4)
        print("..the pricing gun smashes fully into your nose.\n")
        time.sleep(2.5)
        print("You collapse in agony..\n")
        time.sleep(2)
        lose()
    else:
        num <=6
        print("Unfazed by Karen\'s aggression...\n")
        time.sleep(1.5)
        print("You begin windmilling your arms around, wildly...\n")
        time.sleep(2.5)
        print("Your fists connect several times in succession to various parts of Karen\'s head and anatomy..\n")
        time.sleep(4.5)
        print("She slithers down on to the floor, utterly defeated.\n")
        time.sleep(3)
        print("Both you and the cashier throw your arms towards the sky in victory!\n")
        time.sleep(3.5)
        win()

def lose(): #if you a boss fight, this function
    time.sleep(0.5)
    typing_print2("\033[38;5;196mYOU LOSE!\033[0;0m \n")
    game_over()

def win(): #if you win a boss fight, this, then takes you to credits
    time.sleep(0.5)
    typing_print2("\033[38;5;46mYOU WIN!\033[0;0m \n")
    credits()

def credits():
    typing_print("A game developed by:")
    print("""\033[1;32;40m                                                                                                                                      
                                                                                                                                            
                                __.....__           __.....__        _..._                            __.....__               __  __   ___    
        .--./)            .-''         '.     .-''         '.    .'     '.                      .-''         '.            |  |/  `.'   `.  
        /.''\\   .-,.--.  /     .-''"'-.  `.  /     .-''"'-.  `. .   .-.   .               .|   /     .-''"'-.  `.          |   .-.  .-.   ' 
        | |  | |  |  .-. |/     /________\   \/     /________\   \|  '   '  |             .' |_ /     /________\   \    __   |  |  |  |  |  | 
        \`-' /   | |  | ||                  ||                  ||  |   |  |           .'     ||                  | .:--.'. |  |  |  |  |  | 
        /("'`    | |  | |\    .-------------'\    .-------------'|  |   |  |          '--.  .-'\    .-------------'/ |   \ ||  |  |  |  |  | 
        \ '---.  | |  '-  \    '-.____...---. \    '-.____...---.|  |   |  |             |  |   \    '-.____...---.`" __ | ||  |  |  |  |  | 
        /'""'.\ | |       `.             .'   `.             .' |  |   |  |             |  |    `.             .'  .'.''| ||__|  |__|  |__| 
        ||     ||| |         `''-...... -'       `''-...... -'   |  |   |  |             |  '.'    `''-...... -'   / /   | |_                
        \'. __// |_|                                             |  |   |  |             |   /                     \ \._,\ '/                
        `'---'                                                  '--'   '--'             `'-'                       `--'  `"                                \033[0;0m""")
    typing_print("                                                                                                    Jamie, Daniel, Ugo and Graham")
    time.sleep(10)
    game_over2()

def typing_print2(text): #these next 2 functions were used to create slow typing text, used in several instances
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.3)

def typing_print(text): #this one types faster than typing print2, lower values=faster typing
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def dan_boss():
    print("\nYou look down at a nearby basket of items and choose one to throw at Karen...")
    time.sleep(2)
    answer=input(f"Pick an item to throw from the basket: \n{basket}\n")
    if "beans" in answer.lower(): #this chunk of code and entire last section is daniel's boss fight scenario
        beans_item()           #essentially a bunch of if else checks to allow the player to throw items from the basket defined earlier
    if "milk" in answer.lower(): #both you and karen have 3 hit points, the first to lose all 3 loses the game
        milk_item()
    if "banana" in answer.lower():
        banana_item()
    if "cheese" in answer.lower():
        cheese_item()
    if "egg" in answer.lower():
        egg_item()
    if "melon" in answer.lower():
        melon_item()
    else: 
        dan_boss()

def beans_item():
    global basket
    if "beans" in basket :
        print("\nYou launch a tin of beans at Karen..") 
        basket.remove("beans") # removes list item so it can't be thrown again
        hit_miss()
    else:
        print("\nYou can only choose items from the basket...")
        print("Have another go...")
        dan_boss()

def milk_item():
    global basket
    if "milk" in basket :
        print("\nYou hurl a carton of milk at Karen..")
        basket.remove("milk")
        hit_miss()
    else:
        print("\nYou can only choose items from the basket...")
        print("Have another go...")
        dan_boss()

def banana_item():
    global basket
    if "banana" in basket :
        print("\nYou nonchalantly cast a banana towards Karen's face")
        basket.remove("banana")
        hit_miss()
    else:
        print("\nYou can only choose items from the basket...")
        print("Have another go...")
        dan_boss()

def cheese_item():
    global basket
    if "cheese" in basket :
        print("\nYou lob a hunk of cheddar towards Karen...") 
        basket.remove("cheese")
        hit_miss()
    else:
        print("\nYou can only choose items from the basket...")
        print("Have another go...")
        dan_boss()

def egg_item():
    global basket
    if "egg" in basket :
        print("\nYou fling a large, free range, egg in Karen's direction...")
        basket.remove("egg")
        hit_miss()
    else:
        print("\nYou can only choose items from the basket...")
        print("Have another go...")
        dan_boss()

def melon_item():
    global basket
    if "melon" in basket :
        print("\nYou let fly a Honeydew Melon towards Karen's head...") 
        basket.remove("melon")
        hit_miss()
    else:
        print("\nYou can only choose items from the basket...")
        print("Have another go...")
        dan_boss()

def stat_health(): #this would be the function that checks your own hp and decides whether you live or die
    global health
    if health >0:
        return True
    else:
        print("You collapse in agony...")
        time.sleep(2)
        print("Karen has defeated you.")
        time.sleep(1)
        lose()

def karen_health_chack(): #same thing as above but for karen
    global karenhealth
    if karenhealth >0:
        return True   
    else:
        print("You have defeated Karen! Both you and the cashier throw your arms towards the sky in victory!\n")
        time.sleep (2)
        you_win_through()

def you_win_through(): #another reset for all stats and basket, but for a win condition instead of lose
    global basket
    global health
    global karenhealth
    health=3
    karenhealth=3
    basket = [
        "beans",
        "beans",
        "milk",
        "banana",
        "banana",
        "cheese",
        "egg",
        "egg",
        "egg",
        "egg",
        "egg",
        "egg",
        "melon"
        ]
    win()

def remove_karen_helath(): #if an item hits, karen loses a hit point
    global karenhealth
    karenhealth-=1
    karen_health_chack()
    print(f"Karen has lost a hit point, she now has {karenhealth} hit points remaining") #displays karens hit points
    karen_through()

def remove_helath(): #if an item hits you, you lose a hit point
    global health
    health-=1
    stat_health()
    print(f"You have lost a hit point, you now have {health} hit points remaining") #diplays your current hit points
    dan_boss()

def karen_through():  #dan means throw, sometimes spelling is an issue but at least consistent
    global basket
    if not basket: #refills the basket if the odds are ridiculous and both of you constantly missed
        print("\n..you refill your basket with more items from the shelves...") 
        basket.append ("egg")
        basket.append ("beans")
        basket.append ("melon")
        basket.append ("melon")
        basket.append ("egg")
        basket.append ("egg")
        basket.append ("cheese")
        basket.append ("cheese")
        basket.append ("banana")
        basket.append ("banana")
        basket.append ("milk")
        basket.append ("milk")
    time.sleep(1.5)    
    print("\nKaren throws an item back at you in retaliation...")
    karen_hit_miss()

def hit_miss(): #diceroll to determine whether karen's item hits you
    time.sleep(1.5)
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Direct hit! You have weakened Karen.")
        time.sleep(1.5)
        remove_karen_helath()
    else:
        num <=6
        print("You missed..")
        time.sleep(1.5)
        karen_through()

def karen_hit_miss(): #diceroll to determine whether your item hits karen
    time.sleep(1.5)
    num=random.randint(1,6)
    if num >0 and num <=3:
        print("Karen's item hits...")
        time.sleep(1)
        print("You have been weakened.")
        time.sleep(1.5)
        remove_helath()
    else:
        num <=6
        print("Karen missed...")
        time.sleep(1.5)
        dan_boss()

def chack_item_in_basket(): #if else check to correct user input error
    global basket
    if "beans" in basket:
        return True
    if "milk" in basket:
        return True
    if "banana" in basket:
        return True
    if "cheese" in basket:
        return True
    if "egg" in basket:
        return True
    if "melon" in basket:
        return True
    else:
        print("You can only pick items in your basket...")
        print("Have another go...")
        dan_boss()

start_game()

#hope you enjoyed our game - daniel, jamie, graham, ugo <3

