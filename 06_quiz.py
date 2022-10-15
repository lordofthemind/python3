quiz = {
    "Question1": {
        "question": "what is the capital of France?",
        "answer": "Paris"
    },
    "Question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "Question3": {
        "question": "what is the capital of Italy?",
        "answer": "Rome"
    },
    "Question4": {
        "question": "what is the capital of Spain?",
        "answer": "Madrid"
    },
    "Question5": {
        "question": "what is the capital of portugal?",
        "answer": "Lisbon"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        score = score +1
        print("Correct")
        print("Your Score is: " + str(score))

    else:
        print("Wrong....")
        print("The answer is: " + value['answer'])
        print("Your Score is: " + str(score))

print('You got ' + str(score) + " out of Five questions correctly")
print("Your percentage is " + str(int(score/5 * 100)) + "%")