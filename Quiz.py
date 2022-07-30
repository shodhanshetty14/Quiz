print("WELCOME to My Quiz Game.")
print("For each correct answers you will get 2 points, And for Wrong answers you will loose 1 point each")

start = input("Do you wish to Play the game? ")
if start.lower() != 'yes':
    quit()
name = input("Enter Your Name: ")
score = 0

# The Quiz Questions Start from here
ques1 = input("1. Which is the Capital of India?\n")
if ques1.lower() == 'delhi' or 'new delhi':
    print('You got the correct Answer. ')
    score += 2
else:
    print('Sorry Incorrect!')
    score -= 1

ques2 = input("2. Which city is called the silicon city in India?\n")
if ques2.lower() == 'bengaluru' or 'bangalore' or 'bengaluru':
    print('You got the correct Answer. ')
    score += 2
else:
    print('Sorry Incorrect!')
    score -= 1

ques3 = input("3. Which is the National Animal of India?\n")
if ques3.lower() == 'tiger':
    print('You got the correct Answer. ')
    score += 2
else:
    print('Sorry Incorrect!')
    score -= 1

ques4 = input("4. Which is the National Bird of India?\n")
if ques4.lower() == 'peacock':
    print('You got the correct Answer. ')
    score += 2
else:
    print('Sorry Incorrect!')
    score -= 1

ques5 = input("5. What does CPU stand for?\n")
if ques5.lower() == 'central processing unit':
    print('You got the correct Answer. ')
    score += 2
else:
    print('Sorry Incorrect!')
    score -= 1

ques6 = input("6. Who is called the Father Of Modern Computer?\n")
if ques6.lower() == 'alan turing':
    print('You got the correct Answer. ')
    score += 2
else:
    print('Sorry Incorrect!')
    score -= 1
    
# printing the Results
print(f'{name} your total score is {score}/12')
if score == 12:
    print('Well done You have Scored a perfect score.')
elif 6 <= score < 12:
    print('You have a got an average Score Better luck Next Time.')
else:
    print("You Need to work On your General Knowledge!!")
