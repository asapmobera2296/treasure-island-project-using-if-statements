print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first = input("You're at a cross-road, where do you want to go? Left or Right? \n").lower()

if first == "left":
  second = input("\nYou have come across a lake, do you want to wait for a boat or swim? Type wait or swim. \n").lower()
  
  if second == "wait":
    third = input("\nYou have arrived at the island unharmed. There are 3 doors. One red, one yellow, and one blue. Which color do you choose? \n").lower()
    
    if third == "yellow":
      print("\nYou win the game by escaping to Narnia!")
      
    elif third == "red":
      print("\nYou were mauled to death by a pack of wolves. Game Over.")
      
    elif third == "blue":
      print("\nYou were beaten over the head by a World of Warcraft nerd. Game Over.")

    else:
      print("\nYou chose a door that doesn\'t exist. Game Over.")
      
  else:
    print("\nYou drowned trying to swim across the pacific. Game Over.")
    
else:
  print("\nGame Over.")