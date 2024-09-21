# Simple quiz python program

#Questions

questions = {"Capital of India?": "New Delhi",
             "Capital of Uttar Pradesh": "Lucknow",
             "Capital of Madhya Pradesh": "Bhopal",
             "Capital of Rajasthaan": "Jaipur"}

#options

options = ["1. New Delhi\n2. Dhaka\n3. Non",
           "1. Shrinagar\n2. Lucknow\n3. Bhopal",
           "1. Bhopal\n2. Jaipur\n3. Gandhinagar",
           "1. Bhopal\n2. Jaipur\n3. Gandhinagar"]

#correct answers

correct_answers = [1,2,1,2]

score = 0

for i, (question, answer) in enumerate(questions.items()):
    print(question)
    print(options[i])
    
    user = int(input("Enter (1,2,3):"))
    if user == correct_answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!. The correct answer is ", answer)
        
print(f"Quiz completed. Your score is {score} out of {len(questions)}")