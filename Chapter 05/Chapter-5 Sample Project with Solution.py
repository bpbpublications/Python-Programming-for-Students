# Sample project with solution
# Create a Typing Tester to display the user’s typing speed in Characters per second/ minute and Words per second/ minute, along with the total time taken for typing and accuracy score.
# The code is given as follows:


import random  # Used to call random()
import time    # Used to calculate time

class Project:
    def __init__(self):  # Constructor
        self.sent_para = ""  # Initialise empty strings
        self.typed_para = ""

    def readtext(self):  # To read text from file
        f = open('D:/BPB Publications/input.txt').read()
        self. sentences = f.split('\n')
        self. sent_para = random.choice(self. sentences)

    def error_rate(self, sent_para, typed_para):
  # To calculate error rate by matching read string with typed string
        error_count = 0
        length = len(self. sent_para)
        for character in range(length):
            try:
                if sent_para[character] != typed_para[character]:
                    error_count += 1

            except:
                error_count += 1

        error_percent = error_count/length * 100
        return error_percent

    def calc(self):
 # Allow user tobtype the string read from file and calculate accuracy score
        print("Type below paragraph with a few or no mistakes: \n")
        print(self.sent_para)
        start_time = time.time()
        self.typed_para = input("Write above text here : ")
        if self.typed_para == "":
            print("Empty String not Allowed!!. Try Again.")
            self.readtext()
            self.calc()
        else:
            end_time = time.time()
            time_taken = end_time - start_time
            error_percent = self.error_rate(self.sent_para, self.typed_para)
            print("\n")
            accuracy_score = 100 - error_percent
            if accuracy_score < 50:
                print(f"Your accuracy rate {accuracy_score} is less than 50%. Try again to find for typing speed!!.")
            else:
                speed = len(obj1.typed_para) / time_taken
                print("******YOUR SCORE REPORT******")
                print(f"Your speed is {speed} words/sec")
                print(f"The error rate is {error_percent}")
                print(f"The accuracy score is {accuracy_score}")
obj1 = Project()
obj1.readtext()
obj1.calc()
