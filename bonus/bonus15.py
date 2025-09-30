import json

with open("../files/questions.json", "r") as f:
    contents = f.read()

data = json.loads(contents)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(alternative)
    answer = int(input("Your answer: "))
    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['answer']}")

print(score, "/", len(data))