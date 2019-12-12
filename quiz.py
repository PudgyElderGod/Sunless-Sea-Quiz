correct_answers = []
incorrect_answers = []

#Intro
print("""#!-----!#Quiz Time#!-----!#
Welcome to the Sunless Sea Fan Quiz! Show us how much you know about the Unterzee!
""")
#QUESTIONS
def question1():
    user_input = input(''' 1. Where does the game start?

                    a. New London
                    b. Venderbight
                    c. Iron Republic
                    d. Khan's Heart

                    Answer: ''')
    correct_answer = "a"
    if user_input == correct_answer:
        correct_answers.append("number 1")
    else:
        incorrect_answers.append("number 1")

def question2():
    user_input = int(input('''2. How many Echoes does the Phorcyd-class Corvette cost?

                    Answer: '''))
    correct_answer = 4000

    if user_input == correct_answer:
        correct_answers.append("number 2")
    else:
        incorrect_answers.append("number 2")

def question3():
    user_input = input('''3. Where is the Vengeance of Jonah?

                    a. The Iron Republic
                    b. Naples
                    c. Venderbight
                    d. Khan's Shadow

                    Answer:''')
    correct_answer = "c"

    if user_input == correct_answer:
        correct_answers.append("number 3")
    else:
        incorrect_answers.append("number 3")

def question4():
    user_input = input('''4. How many sisters are there in Hunter's Keep?

                    a. 2
                    b. 3
                    c. 4
                    d. 5

                    Answer:''')
    correct_answer = "b"

    if user_input == correct_answer:
        correct_answers.append("number 4")
    else:
        incorrect_answers.append("number 4")


def question5():
    user_input = int(input('''5. True or False: You can sacrifice your crew in Kingeater's Castle?

                    1 for true 0 for false

                    Answer: '''
                    ))
    correct_answer = 1
    if user_input == correct_answer:
        correct_answers.append("number 5")
    else:
        incorrect_answers.append("number 5")

def question6():
    user_input = int(input('''6. True or False: The Exile creates The Serpentine for you.

                    1 for true 0 for false

                    Answer:'''))
    correct_answer = 0

    if user_input == correct_answer:
        correct_answers.append("number 6")
    else:
        incorrect_answers.append("number 6")


def question7():
    user_input = input('''7. What goods can you sell in Naples?

                    a. Firkins of Prisoner Honey
                    b. Catch-Boxes of Sunlight
                    c. Sacks of Darkdrop Coffee
                    d. Bottles of Mushroom Wine

                    Answer:''')
    correct_answer = "c"
    if user_input == correct_answer:
        correct_answers.append("number 7")
    else:
        incorrect_answers.append("number 7")

def question8():
    user_input = input('''8. What lies beyond the Avid Horizon?

                    a. Nothing
                    b. Only Ice
                    c. The Gray City
                    d. The Forge of Souls

                    Answer:''')
    correct_answer = "d"
    if user_input == correct_answer:
        correct_answers.append("number 8")
    else:
        incorrect_answers.append("number 8")

def question9():
    user_input = int(input('''9. How many legacies can you pick after you get a Scion?

                    Answer:'''))
    correct_answer = 2
    if user_input == correct_answer:
        correct_answers.append("number 9")
    else:
        incorrect_answers.append("number 9")

def question10():
    user_input = input('''10. What is the source of the Blemmigans?

                    a. Nuncio
                    b. The Uttershroom
                    c. Salt Lions
                    d. Irem

                    Answer: ''')
    correct_answer = "b"
    if user_input == correct_answer:
        correct_answers.append("number 10")
    else:
        incorrect_answers.append("number 10")

def grading():
    if len(correct_answers) > 6:
        print("What an excellent Zailor! You passed the test!")
    else:
        print("The zee shall take you. You did not pass the test.")
#CALLING QUESTION FUNCTIONS
question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
question10()
print("You got these questions correct: " + str(correct_answers))
print("You got these questions incorrect: " + str(incorrect_answers))
grading()
