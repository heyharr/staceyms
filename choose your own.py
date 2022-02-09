name = input("Type your name: ")
print("Welcome to the Boiling Isles,", name, "!")

answer = input("You are a human who has been sucked through a portal to another dimension. You choice: GIVE UP or FIND A WAY HOME. Which do you choose? ").lower()
if answer == "give up":
    print("A demon comes and eats you.")
        
elif answer == "find a way home":
    answer = input("You walk around the town. Suddenly a fairy is chasing you and wanting your skin. Do you HIDE or RUN? ").lower()
        
    if answer == "hide":
        answer = input("You hide and eventually the fairy gives up on you. You see a mysterious house in the distance. Do you ASK FOR A RIDE or RIDE A DEMON or WALK? ").lower()

        if answer == "ask for a ride":
            print("They tell you to get lost. But you hear them talking about a witch named Eda, the Owl Lady. You walk instead.")
            answer = input("You knock on the door and it opens. The door opens and behind the door is Eda the Owl Lady. She says you can go home if you give her human good. YES or NO? ")
            
            if answer == "no":
                print("Eda kicks you out and you get stepped on by a giraffe. Your adventure is over.")
            elif answer == "yes":
                print("You give her a couple of mints you have in your pocket and she sends you home through the portal. You survived!")   
                     
        elif answer == "ride a demon":
            print("You ride the demon and it eats you.")
        elif answer == "walk":
            print("You reach the house.")
            answer = input("You knock on the door and it opens. The door opens and behind the door is Eda the Owl Lady. She says you can go home if you give her human good. YES or NO? ")
            
            if answer == "no":
                print("Eda kicks you out and you get stepped on by a giraffe. Your adventure is over.")
            elif answer == "yes":
                print("You give her a couple of mints you have in your pocket and she sends you home through the portal. You survived!")
        else:
            print("Not a valid option. You lose")
                
    elif answer == "run":
        answer = input("The fairy has wings; you can't outrun it. You need to choose JUMP INTO LAKE or KEEP RUNNING. Which will you choose? ").lower()
            
        if answer == "keep running":
            print("The fairy catches you and takes your skin. Your adventure is over.")  
        elif answer == "jump into lake":
            answer = input("You stay under for a while. Do you STAY DOWN or LOOK to see if the fairy is gone? Which do you choose? ").lower()
                      
            if answer == "stay down":
                print("You lose air and drown. Your adventure is over.")
            elif answer == "look":
                answer = input("The fairy is gone. You get out of the water. You see a mysterious house in the distance. Do you ASK FOR A RIDE or RIDE THE DEMON or WALK? ").lower()
                
                if answer == "ask for a ride":
                    print("They tell you to get lost. But you hear them talking about a witch named Eda, the Owl Lady. You walk instead.")
                    answer = input("You knock on the door and it opens. The door opens and behind the door is Eda the Owl Lady. She says you can go home if you give her human goods. YES or NO? ")
            
                    if answer == "no":
                        print("Eda kicks you out and you get stepped on by a giraffe. Your adventure is over.")
                    elif answer == "yes":
                        print("You give her a couple of mints you have in your pocket and she sends you home through the portal. You survived!")   
                     
                elif answer == "ride a demon":
                    print("You ride the demon and it eats you.")
                elif answer == "walk":
                    print("You reach the house.")
                    answer = input("You knock on the door and it opens. The door opens and behind the door is Eda the Owl Lady. She says you can go home if you give her human goods. YES or NO? ")
            
                    if answer == "no":
                        print("Eda kicks you out and you get stepped on by a giraffe. Your adventure is over.")
                    elif answer == "yes":
                        print("You give her a couple of mints you have in your pocket and she sends you home through the portal. You survived!")
                    else:
                        print("Not a valid option. You lose")
                
                else:
                    print("Not a valid option. You lose")
                    
            else:
                print("Not a valid option. You lose")
        
        else:
            print("Not a valid option. You lose")  
    
    else:
        print("Not a valid option. You lose")     
else:
    print("Not a valid option. You lose")