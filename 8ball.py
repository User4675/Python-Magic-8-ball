import random


name = ""

question = ""

answer = ""

random_number = random.randint(1, 10)

# print(random_number)  ---  Testing the random number function

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidely so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Potato"
else:
  answer = "Error"

if question == "":
  print("WHAT DO YOU WANT TO KNOW")
elif question != "" and name != "":
  print(name + " asks " + question)
  print("Magic 8-Ball's answer: " + answer)
elif question != "" and name == "":
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
