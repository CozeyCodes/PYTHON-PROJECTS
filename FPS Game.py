

print("\n\t β€οΈβπ©Ή Mission: Undead Siege!π§\n")

ask = input("Would you like to start?πΊ->>> ").upper()
if "Y" in ask:
    pass
else:
    exit()

print("Welcome To The Gulag!π")
print("If You Survive, You Earn Your Freedom!ποΈ")

name = input("Your Name ->>> ").title()
age = int(input("Your Age ->>> " ))

health = 20

def game():

    print("Be Careful... You're Teleported To A Haunted Place...")
    print("You'll Have Some Course of Action To Proceed With!")
    print("Wisely Choose Your Decisions & Avoid Getting Killed!")
    teleport = input("You Are Now Inside Gulag!πΊ \nHere's Your First Choice: (Left\Right)->>> ").upper()
    if "R" in teleport:
        print("Well Done! You Are Now At The Control Room!ποΈ")
        
        gun = input("You Have Full Acess To Any Gun You Want!π₯\nType Your Gun Selection! ->>> ").upper()
        print(f"Good Job! Use Your Fav {gun} Wisely To Slay Down Enemies!β οΈ\nDon't Do Anything Stupid!β Stay Alert!β οΈ")

        uav = input("You Have Two Types of UAV To Choose Between!πΊοΈ\nNormal UAV ->>> Shows Enemy Location on The Map!β\nCounter UAV ->>> Hides Your Location on Enemy Map!β\nYour Choice ->>> ").upper()

        if "C" in uav:
            print("Ah SH#T! The Enemy Has Spotted The UAV!π₯Ά\nDon't Be Scared! They Can't Know Your Location!π\nRun Away From Here As Fast As You Can!πββοΈπ¨")
            
            run_choose = input("You Are Now Out of Gulag!π₯Ά\nBecareful This Place is Haunted!β οΈ\nWould you like to Head towards East or West?π§­\nYour Choice ->>> ").upper()

            if "W" not in run_choose:

                landmines = input("Oh No!π§You Entered A Place With Full of Land Mines!π£\nWould You Like To Hide Here or Risk Your Life?β οΈ\nYour Choice --> ").upper()

                if "H" in landmines:
                    print("Well, You Tried To Hide But The Enemies Killed You...π΅")
                
                else:
                    ziz = input("Be Careful This is Full of Danger!β\nWould you like to go straight into the Land Mines Area or walk away in a ZigZag pattern?\n Your Choice ->>> ").upper()

                    if "Z" in ziz:
                        print("Thank God!ποΈ You Got Lucky & Passed The Mine Path!πͺ\nBut you got your knee fractured while jumping around and lost 5 Health!β")
                    
                        runorheal = input("The Enemies Might Still Be Chasing You!π§\n And Your Radar is now Visible!π\nThey Might Be Tracking You!\nWould you like to go North towards the Oceanπ or hide in a Warehouse at South!πΊοΈ(North/South)\nYour Choice ->>> ").upper()

                        if runorheal == "NORTH":
                            print("Well, you ran too close to the ocean and the tsunami got you dead β οΈ")
                        
                        else:
                            sneak = input(f"You Are Now Hiding On A Warehouse But Unfortunately It's the Enemey's Base!π₯Ά\nWould you like to Kill them with your {gun} or sneak away from here?πββοΈπ¨ (Kill/Sneak)\nYour Choice ->>> ").upper()

                            if sneak == "KILL":
                                ammo = ("Well Done! You Killed 3 of Your Enemies!π\nYou Lost 5 Healthπ° & You Are Out Of Ammo!β Would you like to fight them with your barehands?\nYour Choice ->>> ").upper()
                                
                                if "Y" in ammo:
                                    jump = input("That's Great!π You Managed To Kill All of the Enemies!β\nBut The Main Boss is still somewhere in this Warehouse!π§\nOh No! He Has Shot A Bulled Towards You!π₯Ά\nYou Have To Dodge The Bullet! You Got Only One Chance! Jump Towards Left or Right\n Your Choice ->>> ").upper()

                                    if jump == "LEFT":

                                        point = input("Congrats!π₯³ You Jumped To The Left & Got A Gun!π\nYou Are Now Pointing It To His Face!π\nType [shoot] to Shoot The Head of that BITCH!π\n ->>> ").upper()

                                        if point == "SHOOT":

                                            print("Mission Accomplished Good Work!ππ")
                                else:
                                    print("Not Fighting Was A Really Bad Choice!π\nThey Showed No Mercy on You!\nThey Tied You Up And Burried You Alive!β οΈ")
                            
                            else:
                                print("You Tried To Sneak Out But They Saw And Shot You!β οΈ")

                    else:
                        print("Oops! You Stepped On A Mine & Your Body Exploded...π΅")
            
            else:
                print("You Ran Towards West! But Got Killed in a Truck Accident!β οΈππ")



        else:
            print("Holy Jeez! The Enemy Has Traced Your Location!π₯Ά\nWould You Like To Run or Fight With The Enemies?")
            run_fight = input("Your Choice ->>> ").upper()
            
            if "F" in run_fight:
                print("Well, You Fought With The Enemies But They Were Too Strong!πͺ\n You Got Killed...")
            
            else: 
                print("Well, You Tried To Run But The Enemies Shot You On Your Legs!π¦΅\nYou Lost 10 Health!β\nDon't Worry! You Still Have 10 Health Left!π°")

                run_heal = input("Oh No! The Enemies Might Still Be Chasing You!π₯Ά\nYou're Bleeding Badly! Would You Like To Hide & Heal π or Run?πββοΈπ¨\nYour Choice ->>> ").upper()
                 
                if "R" in run_heal:
                    print("Your Tried To Run But Died From Over-Bleeding... π©Έ")

                else:
                    print("The Enemies Didn't Spot You!β\nBut You Got Bitten By A Snake!π\nYou Have 5 Health Left! There is a Hospital Nearby!π₯\nWould you like to Treat Yourselfπ° or Keep on Hiding Here?π₯Ά")

                    aid_hide = input("Your Choice ->>> ").upper()

                    if "H" in aid_hide:
                        print("The Vemon of Snake Was Really Poisonous!π€’\nYou Died...π΅")
                    
                    else: 
                        print(f"The Hospital Was Attacked By Your Enemies!π₯Ά\nYou Tried To Kill Them With Your {gun}!π‘οΈ\nBut They Were Too Powerful.πͺ You Were Killed...πͺ¦")


    else:
        print("Oops!π΅ You Got Shot By A Pyscho Killer...")
        print(f"Your Health ->>> 0")
    

if age >= 18:
    print(f"Captain {name.split().pop(0)}, You're Ready To Slayy!π")
    game()
elif age >=13:
    print(f"Aw OH! {name.split().pop(0)}, You're Quite Young!\nPlease, Play With Supervision!π₯Ά")
    game()
else:
    print(f"{name.split().pop(0)}, Sorry You Are Too Young To Slay!πΆπΌ")



    
