# Sample project with solution
# Create text-based Adventure Game using a single player to demonstrate the usage of decision-based flow control in Python.
# This text-based adventure game is an application that consists of a series of questions or riddles. The user has to enter his name to begin the game or play as “Guest” with three lifelines at hand. The user must answer the questions in either Yes/ No or True/ False.
# (Note: You may try implementing the program with different answers and choices). If the user answers all answers correctly in any of the three lifelines, then he wins. Otherwise, he loses the game.

# Solution: 

import time
print("You have only 3 lifelines to answer all questions correct and win!!")
lifeline =3
#Storing the user's name. If no name given then assume Guest.
username = input("\nEnter your name?")       
if username=="":
    username="Guest"
print ("\nWelcome, " +  username +", \nGame Rule : You can give answer as True/False or Yes/No.")
time.sleep(3)   # sleep(3) pauses the program for 3ms.
while(lifeline>=1):
    print("Your current Lifeline Number is : ", lifeline)
    true_ans = ["T", "t", "True", "Yes", "y", "yes", "Y"]
    false_ans = ["F", "f", "False", "No", "no", "N", "n"]
    correct = 0 #Storing the correct answers
    print("\n...........................The game begins.............................")
    print("\nHere is the first Question.")
    time.sleep(3)
    print ("\nCanberra is the captial of Australia?")
    choice = input("Type your Answer Here : ")
    if choice in true_ans:
      correct += 1 #If correct, the user gets one point
    else:
      correct += 0 #If incorrect, 0 is awarded for that answer 
      
    print ("\nThe islands of Seychelles are located in Pacific Ocean?")
    choice = input("Type your Answer Here : ")
    if choice in false_ans:
      correct += 1
    else:
      correct += 0  

    print ("\nA normal Human has 210 bones?")
    choice = input("Type your Answer Here : ")
    if choice in false_ans:
      correct += 1
    else:
      correct += 0 
      
    print ("\n Did Dmitri Mendeleev designed Periodic table in Chemistry?")
    choice = input("Type your Answer Here : ")
    if choice in true_ans:
      correct += 1
    else:
      correct += 0  
      
    print ("\nIf speed of a moving car and distance travelled by it is given, can we calculate time taken for this journey?")
    choice = input("Type your Answer Here : ")
    if choice in true_ans:
      correct += 1
    else:
      correct += 0
      
    print ("Sun rises from the West?")
    choice = input("Type your Answer Here : ")
    if choice in false_ans:
      correct += 1
    else:
      correct += 0
        
    print("\nTask over, " + username +". You got", correct, "out of 6 correct.")
    # Check if correct answers are equal to 6 or not.
    # If all correct answers then exit the loop else keep continuing the game.
    if correct == 6:
        print("Congratulations!!You won the Game!!")
        break
    else:
        print("Warning : You Lost the Game. Your lifeline Number ",lifeline," is over!!")
        lifeline = lifeline - 1
else:
    print("!! Game Over !! Better Luck Next Time !!")
