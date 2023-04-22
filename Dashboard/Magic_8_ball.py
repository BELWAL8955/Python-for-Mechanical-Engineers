# import modules
import random, csv, sys


class magic9ball:
    def __init__(self, name):
        self.__name = name
        self.__mQuestion = []
        self.__start_game()

    def __start_game(self):
        mResponse = ["It is certain", "You may rely on it", "As I see it"]

        lQuestions = True
        print("Welcome to the Game" + self.__name)
        while lQuestions:
            mQues = input("Please enter a Question: ")
            mRespond = mResponse[random.randint(0, 2)]
            if mQues == "":
                print("Thank you for playing")
                sys.exit()
            else:
                print(mRespond)
    def __write_questions(self):
        f = open("magic_questions.csv", "a", newline="")
        wrt = csv.writer(f)
         for q in self.__mQuestion:
             wrt.writerow([q])
         f.close()
