import json
import random
    
#open json file and load data into questionList
with open("EMT_Quiz_Questions.json", "r") as file:
    questionList = json.load(file)

#put questions in a random order
random.shuffle(questionList)

#create variables to hold number of questions answered and correct answers
questionsAnswered = 0
correctAnswers = 0

#loop to handle each question
for question in questionList:
    #ask the user the question
    print(question["prompt"])

    #shuffle the answer choices for each question by randomizing the order of the answer list
    random.shuffle(question["answerList"])

    #set first answer choice to A using ascii
    ascii_value = 65
    #create an empty dictionary to hold the letter associated with each answer
    answersDict = {}

    #iterate through each question's list of answers
    for answer in question["answerList"]:
        #assign a letter to each answer
        answersDict[str(chr(ascii_value))] = answer

        #print each answer with the letter before it
        print(chr(ascii_value) + " " + answer)

        #increment ascii value so next letter is used for next answer
        ascii_value += 1
    
    #ask user for input, store in variable, increment questionsAnswered
    userAnswer = input()
    questionsAnswered += 1

    #validate user input - user input must be one of the given letter choices
    while not((ord(userAnswer.upper()) >= 65) and (ord(userAnswer.upper()) < (65 + len(question["answerList"])))):
        print("Please enter the letter of a given answer choice.")
        userAnswer = input()

    #determine whether or not user answer is correct
    if answersDict[str(userAnswer.upper())] == question["correctAnswer"]:
        correctAnswers += 1
        print("That's correct!")
    else:
        print("Sorry, that's incorrect.")
        print("The correct answer is: " + question["correctAnswer"])
    
    #print user score
    print("Your score is: " + str(correctAnswers) + "/" + str(questionsAnswered))

    #if there are no more questions, tell the user the quiz is over
    if question == questionList[len(questionList) - 1]:
        print("This is the end of the quiz.")
    else:
        #prompt the user to move to the next question
        print("Enter 'N' to move to the next question")
        userInput = input()

        #validate user input
        while not(userInput.upper() == "N"):
            print("Enter 'N' to move to the next question")
            userInput = input()


    
    
    
