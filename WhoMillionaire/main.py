import time  # Imports time and dyd for text delay, and system exit
import sys

fiftyfifty_counter = 1
# 50/50 variable
phone_a_friend_counter = 1  # Phone a friend is call the computer!!!
# phone a friend variable
asktheaudience_counter = 1
# ask the audience variable  #  These Variables are equal to 1 from the start meaning the lifelines can be used, but
# when equal to zero means lifeline can't be used
# Variables for amount of money, question number, answers, and lifelines.
question_counter = 1  # Keeps track of what question user is at for lifelines
money_counter = '0'  # Counter that keeps track of money user is able to withdraw
money_received = '0'  # Keeps track of money user has secured
q1call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop " \
         "I think the answer is" + "\033[92m" + " b!" + "\033[94m"  # Variable for Question 1 Call the Computer,
# Continues for every question
q1answer = 'b'  # Answer for question used by Lifelines, and wrong/right statements
q1ask = 'The audience says:' + "\033[92m" + ' a.25%  b.55%  c.8%  d.12%' + "\033[94m"  # Statement for Ask the Audience
q1askx = 'The audience says:' + "\033[92m" + ' a = 21% b = 79%' + "\033[94m"  # Ask the Audience After 50/50
q1fiftyfifty = 'Alright. Here are your new answer options:' + "\033[92m" + ' a. 6   b. 7' + "\033[94m"  # Statment for fifty fifty
q2fiftyfifty = 'Alright. Here are your new answer options:' + "\033[92m" + \
               ' a. Lake Ontario  d.Lake Superior' + "\033[94m"
q2call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop" \
         " I think the answer is" + "\033[92m" + " d!" + "\033[94m"
q2ask = 'The Audience says:' + "\033[92m" + 'a.35%  b.15%  c.5%  d.45%' + "\033[94m"
q2askx = 'The audience says:' + "\033[92m" + ' b.25%  d.75%' + "\033[94m"
q2answer = 'd'
q3fiftyfifty = 'Alright. Here are your new answer options:' + "\033[92m" + ' c.Vatican City  d.San Marino' + "\033[94m"
q3call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop" \
         " I think the answer is" + "\033[92m" + " c!" + "\033[94m"
q3ask = 'The Audience says:' + "\033[92m" + ' a.45%  b.10%  c.40%  d.5%' + "\033[94m"
q3askx = 'The Audience says:' + "\033[92m" + ' c.90%  d.10%' + "\033[94m"
q3answer = 'c'
q4fiftyfifty = 'Alright. Here are your new answer options:' + "\033[92m" + \
               ' a. Mississippi River  b. Nile River' "\033[94m"
q4call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop" \
         " I think the answer is " + "\033[92m" + " b!" + "\033[94m"
q4ask = 'The Audience says:' + "\033[92m" + ' a.30%  b.40%  c.25%  d.5%' + "\033[94m"
q4askx = 'The Audience says:' + "\033[92m" + ' c.40%  d.60%' + "\033[94m"
q4answer = 'b'
q5fiftyfifty = 'Alright, here are your new answer options:' + "\033[92m" + 'a. Canberra  c.Perth' + "\033[94m"
q5call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop " \
         "I think the answer is " + "\033[92m" + "a!" + "\033[94m"
q5ask = 'The Audience says: ' + "\033[92m" + 'a.30% b.25% c.15% d.30%' + "\033[94m"
q5askx = 'The Audience says: ' + "\033[92m" + 'a.70% b.30%' + "\033[94m"
q5answer = 'a'
q6fiftyfifty = 'Alright, here are your new answer options:' + "\033[92m" + ' a. Nevada  c.California' + "\033[94m"
q6call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop" \
         " I think the answer is" + "\033[92m" + " b!" + "\033[94m"
q6ask = 'The Audience says:' + "\033[92m" + ' a.20% b.35% c.25% d.20%' + "\033[94m"
q6askx = 'The Audience says:' + "\033[92m" + ' b.65% c.35%' + "\033[94m"
q6answer = 'b'
q7fiftyfifty = 'Alright, here are your new answer options: c. Indian Sea d. Philippine Sea'
q7call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop" \
         " I think the answer is " + "\033[92m" + "d!" + "\033[94m"
q7ask = 'The Audience says:' + "\033[92m" ' a.29% b.19% c.18% d.34%' + "\033[94m"
q7askx = 'The Audience says:' + "\033[92m" + ' a.43% d.57%' + "\033[94m"
q7answer = 'd'
q8fiftyfifty = 'Alright, here are your new answer options:' + "\033[92m" + 'b. Brazil d. Peru' + "\033[94m"
q8call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop" \
         " I think the answer is" + "\033[92m" + "d!" + "\033[94m"
q8ask = 'The audience says:' + "\033[92m" + ' a.25%  b.20%  c.15%  d.40%' + "\033[94m"
q8askx = 'The audience says:' + "\033[92m" + ' b.20%  c.80%' + "\033[94m"
q8answer = 'd'
q9fiftyfifty = ' Alright, here are your new options:' + "\033[92m" + ' a. 14 b. 11' + "\033[94m"
q9call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop" \
         " I think the answer is" + "\033[92m" + " b!" + "\033[94m"
q9ask = 'The audience says:' + "\033[92m" + ' a.27%  b. 23%  c.26%  d.24%' + "\033[94m"
q9askx = 'The audience says:' + "\033[92m" + ' a.55%  b. 45%' + "\033[94m"
q9answer = 'a'
q10fiftyfifty = 'Alright, here are your new options:' + "\033[92m" + ' b. Faraday c. Köppen' + "\033[94m"
q10call = "Ok, lets call the computer and hear what he has to say!.............. Beep Boop Beep Boop " \
          "I think the answer is" + "\033[92m" + " c!" + "\033[94m"
q10ask = "The audience says:" + "\033[92m" + " a.22%  b. 30%  c.28%  d.20%" + "\033[94m"
q10askx = 'The audience says:' "\033[92m" + ' b.51%  c. 49%' + "\033[94m"
q10answer = 'c'
print("\033[94m" + "------------------------------------------------------------")
y = [("Welcome to who wants to be a millionaire, Geography edition!"
      "(Created by Max P and Gavin C)"), "I’m your host, Joseph Joestar", "What is your name?:"]  # asks for users name


def delay(u):
    for i in u:
        print(i)
        sys.stdout.flush()
        time.sleep(0)


#  Function that creates text delay to be more appealing
delay(y)


def easteregg(yotus):
    if yotus == 'pawel':
        return " Please mark our assignment well♥" \
               " Are you ready?!"
    else:
        return 'Are you ready?!'


#  function for when my teacher tests this assignment!


name = input().lower()
x = ["Nice to meet you, " + str(name) + "\033[91m", "There are 10 questions,"
                                                    " all multiple choice. Please type in the letter corresponding to your answer, whiile inputting it.",
     "You have 3 lifelines: 50/50, Call the Computer, and ask the audience. Use them by typing it in as the answer!",
     'If you wish to withdraw make sure to type in "Withdraw"!' + str(easteregg(name)), "\033[94m"]
#  List of print statements for delay function

delay(x)


def ready():
    ready1 = "notready"
    while ready1 != "Yes" and ready1 != "yes":
        ready1 = input("Type 'Yes' when you're ready to start: ").lower()
        if ready1 == 'no':
            return sys.exit("Ok, please come back when you're ready!")
    return "Okay, let’s get started!"


#  Function that starts program if user is ready
print(ready())


def phoneafriend(n, b):  # PHONE A FRIEND WAS WHAT WE HAD BEFORE CALL THE COMPUTER**
    # Phone a friend in the code refers to call the computer
    global phone_a_friend_counter
    phone_a_friend_counter = 0  # sets phone_a_friend_counter to zero not allowing it to be used again
    print(n)
    ze = input('Input your Answer: ').lower()
    if ze == b:
        return "\033[92m" + "That's Correct!" + "\033[94m"
    elif ze == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif ze == '50/50' and question_counter == 1:  # allows fifty fifty to be used after phone a friend
        return fiftyfifty(q1fiftyfifty, q1answer)
    elif ze == '50/50' and question_counter == 2:
        return fiftyfifty(q2fiftyfifty, q2answer)
    elif ze == '50/50' and question_counter == 3:
        return fiftyfifty(q3fiftyfifty, q3answer)
    elif ze == '50/50' and question_counter == 4:
        return fiftyfifty(q4fiftyfifty, q4answer)
    elif ze == '50/50' and question_counter == 5:
        return fiftyfifty(q5fiftyfifty, q5answer)
    elif ze == '50/50' and question_counter == 6:
        return fiftyfifty(q6fiftyfifty, q6answer)
    elif ze == '50/50' and question_counter == 7:
        return fiftyfifty(q7fiftyfifty, q7answer)
    elif ze == '50/50' and question_counter == 8:
        return fiftyfifty(q8fiftyfifty, q8answer)
    elif ze == '50/50' and question_counter == 9:
        return fiftyfifty(q9fiftyfifty, q9answer)
    elif ze == '50/50' and question_counter == 10:
        return fiftyfifty(q10fiftyfifty, q10answer)
    elif ze == 'ask the audience' and question_counter == 1:  # allows ask the audience to be used after phone a friend
        return asktheaudience(q1ask, q1answer)
    elif ze == 'ask the audience' and question_counter == 2:
        return asktheaudience(q2ask, q2answer)
    elif ze == 'ask the audience' and question_counter == 3:
        return asktheaudience(q3ask, q3answer)
    elif ze == 'ask the audience' and question_counter == 4:
        return asktheaudience(q4ask, q4answer)
    elif ze == 'ask the audience' and question_counter == 5:
        return asktheaudience(q5ask, q5answer)
    elif ze == 'ask the audience' and question_counter == 6:
        return asktheaudience(q6ask, q6answer)
    elif ze == 'ask the audience' and question_counter == 7:
        return asktheaudience(q7ask, q7answer)
    elif ze == 'ask the audience' and question_counter == 8:
        return asktheaudience(q8ask, q8answer)
    elif ze == 'ask the audience' and question_counter == 9:
        return asktheaudience(q9ask, q9answer)
    elif ze == 'ask the audience' and question_counter == 10:
        return asktheaudience(q10ask, q10answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' + b +
              "\033[91m" + "! you made it to question number", str(question_counter), "and left with",
              str(money_received), "dollars")
        return sys.exit()  # wrong answer will end program


def asktheaudience(v, p):  # same as ask the computer
    global asktheaudience_counter
    asktheaudience_counter = 0  # when the function is called the variable fiftyfifty_counter is set to 0
    # not allowing it to be used again
    print(v)
    ee = input('Input your Answer: ').lower()
    if ee == p:
        return "\033[92m" + 'You are Correct!' + "\033[94m"
    elif ee == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif ee == '50/50' and question_counter == 1:  # allows fiftyfifty to be used after ask the audience
        return fiftyfifty(q1fiftyfifty, q1answer)
    elif ee == '50/50' and question_counter == 2:
        return fiftyfifty(q2fiftyfifty, q2answer)
    elif ee == '50/50' and question_counter == 3:
        return fiftyfifty(q3fiftyfifty, q3answer)
    elif ee == '50/50' and question_counter == 4:
        return fiftyfifty(q4fiftyfifty, q4answer)
    elif ee == '50/50' and question_counter == 5:
        return fiftyfifty(q5fiftyfifty, q5answer)
    elif ee == '50/50' and question_counter == 6:
        return fiftyfifty(q6fiftyfifty, q6answer)
    elif ee == '50/50' and question_counter == 7:
        return fiftyfifty(q7fiftyfifty, q7answer)
    elif ee == '50/50' and question_counter == 8:
        return fiftyfifty(q8fiftyfifty, q8answer)
    elif ee == '50/50' and question_counter == 9:
        return fiftyfifty(q9fiftyfifty, q9answer)
    elif ee == '50/50' and question_counter == 10:
        return fiftyfifty(q10fiftyfifty, q10answer)
    elif ee == 'call the computer' and question_counter == 1:  # allows call the computer to be used after phone a friend
        return phoneafriend(q1call, q1answer)
    elif ee == 'call the computer' and question_counter == 2:
        return phoneafriend(q2call, q2answer)
    elif ee == 'call the computer' and question_counter == 3:
        return phoneafriend(q3call, q3answer)
    elif ee == 'call the computer' and question_counter == 4:
        return phoneafriend(q4call, q4answer)
    elif ee == 'call the computer' and question_counter == 5:
        return phoneafriend(q5call, q5answer)
    elif ee == 'call the computer' and question_counter == 6:
        return phoneafriend(q6call, q6answer)
    elif ee == 'call the computer' and question_counter == 7:
        return phoneafriend(q7call, q7answer)
    elif ee == 'call the computer' and question_counter == 8:
        return phoneafriend(q8call, q8answer)
    elif ee == 'call the computer' and question_counter == 9:
        return phoneafriend(q9call, q9answer)
    elif ee == 'call the computer' and question_counter == 10:
        return phoneafriend(q10call, q10answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' + p +
              "\033[91m" + "! you made it to question number", str(question_counter), "and left with",
              str(money_received), "dollars")
        return sys.exit()


def fiftyfifty(t, r):  # fifty fifty function
    global fiftyfifty_counter
    fiftyfifty_counter = 0
    print(t)
    global hi
    hi = input('Input Answer: ').lower()
    if hi == r:
        return "\033[92m" + 'You got it right!' + "\033[94m"
    elif hi == 'Withdraw' or hi == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif hi == 'ask the audience' and question_counter == 1:  # allows ask the audience to be used after 50/50
        return asktheaudience(q1askx, q1answer)
    elif hi == 'ask the audience' and question_counter == 2:
        return asktheaudience(q2askx, q2answer)
    elif hi == 'ask the audience' and question_counter == 3:
        return asktheaudience(q3askx, q3answer)
    elif hi == 'ask the audience' and question_counter == 4:
        return asktheaudience(q4askx, q4answer)
    elif hi == 'ask the audience' and question_counter == 5:
        return asktheaudience(q5askx, q5answer)
    elif hi == 'ask the audience' and question_counter == 6:
        return asktheaudience(q6askx, q6answer)
    elif hi == 'ask the audience' and question_counter == 7:
        return asktheaudience(q7askx, q7answer)
    elif hi == 'ask the audience' and question_counter == 8:
        return asktheaudience(q8askx, q8answer)
    elif hi == 'ask the audience' and question_counter == 9:
        return asktheaudience(q9askx, q9answer)
    elif hi == 'ask the audience' and question_counter == 10:
        return asktheaudience(q10askx, q10answer)
    elif hi == 'call the computer' and question_counter == 1:  # allows call the computer to be used after 50/50
        return phoneafriend(q1call, q1answer)
    elif hi == 'call the computer' and question_counter == 2:
        return phoneafriend(q2call, q2answer)
    elif hi == 'call the computer' and question_counter == 3:
        return phoneafriend(q3call, q3answer)
    elif hi == 'call the computer' and question_counter == 4:
        return phoneafriend(q4call, q4answer)
    elif hi == 'call the computer' and question_counter == 5:
        return phoneafriend(q5call, q5answer)
    elif hi == 'call the computer' and question_counter == 6:
        return phoneafriend(q6call, q6answer)
    elif hi == 'call the computer' and question_counter == 7:
        return phoneafriend(q7call, q7answer)
    elif hi == 'call the computer' and question_counter == 8:
        return phoneafriend(q8call, q8answer)
    elif hi == 'call the computer' and question_counter == 9:
        return phoneafriend(q9call, q9answer)
    elif hi == 'call the computer' and question_counter == 10:
        return phoneafriend(q10call, q10answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' + r +
              "\033[91m" + "! you made it to question number", str(question_counter), "and left with",
              str(money_received), "dollars")
        return sys.exit()


def lifelines_remaining(w, e, r):  # tells the user how many life lines they have left
    if w == 1 and e == 1 and r == 1:
        return 'You have 50/50, Call the Computer, and Ask the Audience remaining'
    elif w != 1 and e == 1 and r == 1:
        return 'You have Call the Computer and Ask the Audience remaining'
    elif w != 1 and e != 1 and r == 1:
        return 'You have Ask the Audience remaining'
    elif w != 1 and e == 1 and r != 1:
        return 'You have Call the Computer remaining'
    elif w == 1 and e != 1 and r == 1:
        return 'You have 50/50 and Ask the Audience remaining'
    elif w == 1 and e == 1 and r != 1:
        return 'You have 50/50 and Call the Computer remaining'
    elif w == 1 and e != 1 and r != 1:
        return 'You have 50/50 remaining'
    else:
        return 'You have no lifelines remaining'


def q1():  # question 1 function
    print("For $1,000")
    print("Question 1: How many Continents are there?")
    print('a : 6     b : 7')
    print('c : 5     d : 8')
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    # Prevents unboundlocal error by making global
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    q1input = input('Please Type in Your Answer: ').lower()
    if q1input == 'b' or q1input == '7':
        return "\033[92m" + "That's correct! What a great start!"  # Correct answer will end fuction leading to next question
    elif q1input == 'withdraw':
        print("We're sorry you don't wish to play the game! Please come back when you are ready, we'll be waiting!")
        return sys.exit()  # allows user to withdraw with currenrt money
    elif q1input == '50/50':
        fiftyfifty_counter -= 1
        return fiftyfifty(q1fiftyfifty, q1answer)  # calls 50/50 function
    elif q1input == 'call the computer':
        phone_a_friend_counter -= 1
        return phoneafriend(q1call, q1answer)  # calls phone a friend funtion
    elif q1input == 'ask the audience':
        asktheaudience_counter -= 1
        return asktheaudience(q1ask, q1answer)  # calls ask the audience function
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' + "b: 7" +
              "\033[91m" + "! you made it to question number", str(question_counter), "and left with",
              str(money_received), "dollars")
        return sys.exit()  # wrong answer will end the program


print(q1())  # calls the question 1 funtion

money_counter = '1,000'  # tells the user current prize money
print("\033[94m" + "You are now at", str(money_counter), "! Here's the next question for 3,000...")


def q2():
    print('Question 2: Which Lake is the largest of all the Great lakes in Canada')
    print('a : Lake Ontario     b : Lake Erie')
    print('c : Lake Huron       d : Lake Superior')
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter,
                              asktheaudience_counter))  # tells the user number of life lines left
    question_counter += 1
    q2input = input('Please Type in Your Answer: ').lower()
    if q2input == 'lake superior' or q2input == 'd':
        return "\033[92m" + 'Correct Again!'
    elif q2input == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q2input == '50/50' and fiftyfifty_counter != 1:  # if the 50/50 variable is equal to zero they will not be able to use it again
        print('No more 50/50 remaining!')
        return q2()
    elif q2input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q2fiftyfifty, q2answer)
    elif q2input == 'call the computer' and phone_a_friend_counter != 1:  # if the phone a friend variable is equal to zero they will not be able to use it again
        print('No more Call the Computer Remaining!')
        return q2()
    elif q2input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q2call, q2answer)
    elif q2input == 'ask the audience' and asktheaudience_counter != 1:  # if the ask the audience variable is equal to zero they will not be able to use it again
        print('No more Ask The Audience Remaining!')
        return q2()
    elif q2input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q2ask, q2answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' +
              "d: Lake Superior" + "\033[91m" + "! you made it to question number", str(question_counter),
              "and left with", str(money_received), "dollars")
        return sys.exit()


print(q2())

money_counter = '3,000'
print("\033[94m" + "You are now at ", str(money_counter), "! Here's the next question for 6,000...")


def q3():
    print('Question 3: What is the smallest country in the world')
    print('a : Marshall Islands   b : Monaco')
    print('c : Vatican City       d : San Marino')
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    question_counter += 1
    q3input = input('Please Type in Your Answer: ').lower()
    if q3input == 'vatican city' or q3input == 'c':
        return "\033[92m" + "That's the correct answer!"
    elif q3input == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q3input == '50/50' and fiftyfifty_counter != 1:
        print('No more 50/50 remaining!')
        return q3()
    elif q3input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q3fiftyfifty, q3answer)
    elif q3input == 'call the computer' and phone_a_friend_counter != 1:
        print('No more Call the Computer remaining')
        return q3()
    elif q3input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q3call, q3answer)
    elif q3input == 'ask the audience' and asktheaudience_counter != 1:
        print('No more Ask the Audience Remaining!')
        return q3()
    elif q3input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q3ask, q3answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' +
              "c: Vatican City" + "\033[91m" + "! you made it to question number", str(question_counter),
              "and left with", str(money_received), "dollars")
        return sys.exit()


print(q3())
money_counter = '6,000'
print("\033[94m" + "You are now at ", str(money_counter), "! Here's the next question for 15,000...")


def q4():
    print('Question 4: What is the longest river in the world?')
    print('a : Mississippi River   b : Nile River')
    print('c : Amazon River        d : Yangtze')
    print("You're doing great so far " + name + " 👍")
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    question_counter += 1
    q4input = input('Please Type in Your Answer: ').lower()
    if q4input == 'nile river' or q4input == 'b':
        return "\033[92m" + 'Right again!'
    elif q4input == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q4input == '50/50' and fiftyfifty_counter != 1:
        print('No more 50/50 remaining!')
        return q4()
    elif q4input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q4fiftyfifty, q4answer)
    elif q4input == 'call the computer' and phone_a_friend_counter != 1:
        print('No more Call the Computer remaining!')
        return q4()
    elif q4input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q4call, q4answer)
    elif q4input == 'ask the audience' and asktheaudience_counter != 1:
        print('No more Ask The Audience remaining!')
        return q4()
    elif q4input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q4ask, q4answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' +
              "b: Nile River" + "\033[91m" + "! you made it to question number", str(question_counter),
              "and left with", str(money_received), "dollars")
        return sys.exit()


print(q4())
money_counter = '15,000'
print("\033[94m" + "You are now at ", str(money_counter), "! Here's the next question for 30,000...")


def q5():
    print('Question 5: What city is the capital of Australia?')
    print('a : Canberra            b : Melbourne')
    print('c : Perth               d : Sydney')
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    question_counter += 1
    q5input = input('Please Type in Your Answer: ').lower()
    if q5input == 'canberra' or q5input == 'a':
        return "\033[92m" + 'Corrrrrrect!~'
    elif q5input == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q5input == '50/50' and fiftyfifty_counter != 1:
        print('No more 50/50 remaining!')
        return q5()
    elif q5input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q5fiftyfifty, q5answer)
    elif q5input == 'call the computer' and phone_a_friend_counter != 1:
        print('No more Call the Computer remaining!')
        return q5()
    elif q5input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q5call, q5answer)
    elif q5input == 'ask the audience' and asktheaudience_counter != 1:
        print('No more Ask The Audience remaining!')
        return q5()
    elif q5input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q5ask, q5answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' +
              "a: Canberra" + "\033[91m" + "! you made it to question number", str(question_counter), "and left with",
              str(money_received), "dollars")
        return sys.exit()


print(q5())
money_received = '30,000'
money_counter = '30,000'
print(
    "\033[94m" + "You have now secured 30,000 dollars for yourself! Well done! If you were to get any question wrong from 6-10 you will still leave with 30,000. Lets keep going for 60,000...")


def q6():
    print('Question 6: In which U.S. state is Death Valley?')
    print('a : Arizona             b : California')
    print('c : Nevada              d : West Virginia')
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    question_counter += 1
    q6input = input('Please Type in Your Answer: ').lower()
    if q6input == 'b' or q6input == 'california':
        return "\033[92m" + 'Corrrrrrect!~'
    elif q6input == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q6input == '50/50' and fiftyfifty_counter != 1:
        print('No more 50/50 remaining!')
        return q6()
    elif q6input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q6fiftyfifty, q6answer)
    elif q6input == 'call the computer' and phone_a_friend_counter != 1:
        print('No more Call the Computer remaining!')
        return q6()
    elif q6input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q6call, q6answer)
    elif q6input == 'ask the audience' and asktheaudience_counter != 1:
        print('No more Ask The Audience remaining!')
        return q6()
    elif q6input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q6ask, q6answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' +
              "b: California" + "\033[91m" + "! you made it to question number", str(question_counter),
              "and left with", str(money_received), "dollars")
        return sys.exit()


print(q6())

money_counter = '60,000'
print("\033[94m" + "You are now at 60,000 dollars! Well done! Lets keep going for 125,000...")


def q7():
    print('Question 7: Apart from the five oceans, which is the largest sea in the world?')
    print('a : Mediterranean Sea       b : Dead Sea')
    print('c : Indian Sea              d : Philippine Sea')
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    global money_received
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    question_counter += 1
    q7input = input('Please Type in Your Answer: ').lower()
    if q7input == 'd' or q7input == 'philippine sea':
        return "\033[92m" + 'Corrrrrrect!~'
    elif q7input == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q7input == '50/50' and fiftyfifty_counter != 1:
        print('No more 50/50 remaining!')
        return q7()
    elif q7input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q7fiftyfifty, q7answer)
    elif q7input == 'call the computer' and phone_a_friend_counter != 1:
        print('No more Call the Computer remaining!')
        return q7()
    elif q7input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q7call, q7answer)
    elif q7input == 'ask the audience' and asktheaudience_counter != 1:
        print('No more Ask The Audience remaining!')
        return q7()
    elif q7input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q7ask, q7answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' +
              "d: Philippine Sea" + "\033[91m" + "! you made it to question number", str(question_counter),
              "and left with", str(money_received), "dollars")
        return sys.exit()


print(q7())

money_counter = '125,000'
print("\033[94m" + "You are now at 125,000 dollars! Well done! Lets keep going for 250,000...")


def q8():
    print('Question 8: In which Country is Machu Picciu located in?')
    print('a : Chile        b : Brazil')
    print('c : Argentina    d : Peru')
    print("Hmmm.. take your time for this one")
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    global money_counter
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    question_counter += 1
    q8input = input('Please Type in Your Answer: ').lower()
    if q8input == 'peru' or q8input == 'd':
        return "\033[92m" + "You're right again!"
    elif q8input == 'withdraw':
        print('You have withdrawn ', str(money_counter), ' dollars at question ', str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q8input == '50/50' and fiftyfifty_counter != 1:
        print('No more 50/50 remaining!')
        return q8()
    elif q8input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q8fiftyfifty, q8answer)
    elif q8input == 'call the computer' and phone_a_friend_counter != 1:
        print('No more Call the Computer remaining!')
        return q8()
    elif q8input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q8call, q8answer)
    elif q8input == 'ask the audience' and asktheaudience_counter != 1:
        print('No more Ask The Audience remaining!')
        return q8()
    elif q8input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q8ask, q8answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' +
              "d: Peru" + "\033[91m" + "! you made it to question number", str(question_counter),
              "and left with", str(money_received), "dollars")
        return sys.exit()


print(q8())

money_counter = '250,000'
print("\033[94m" + "You are now at ", str(money_counter), "! Here's the next question for 500,000...")


def q9():
    print('Question 9: How many Countries Border Russia?')
    print('a : 14        b : 11')
    print('c : 12        d : 10')
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    question_counter += 1
    q9input = input('Please Type in Your Answer: ').lower()
    if q9input == '14' or q9input == 'a':
        return "\033[92m" + "Outstanding! Correct again!"
    elif q9input == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q9input == '50/50' and fiftyfifty_counter != 1:
        print('No more 50/50 remaining!')
        return q9()
    elif q9input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q9fiftyfifty, q9answer)
    elif q9input == 'call the computer' and phone_a_friend_counter != 1:
        print('No more Call the Computer remaining!')
        return q9()
    elif q9input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q9call, q9answer)
    elif q9input == 'ask the audience' and asktheaudience_counter != 1:
        print('No more Ask The Audience remaining!')
        return q9()
    elif q9input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q9ask, q9answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' + "a: 14" +
              "\033[91m" + "! you made it to question number", str(question_counter),
              "and left with", str(money_received), "dollars")
        return sys.exit()


print(q9())
money_counter = '500,000'
print("\033[94m" + "You are now at ", str(money_counter), "! The next question is the million dollar question!!!")


def q10():
    print('Question 10, and the million dollar question!:'
          ' Which method is used to determine the climate of a country or a region?')
    print('a : Meitner   b : Faraday')
    print('c : Köppen    d : Kepler')
    print("Make sure to really take your time on this...")
    global fiftyfifty_counter
    global phone_a_friend_counter
    global asktheaudience_counter
    global question_counter
    print(lifelines_remaining(fiftyfifty_counter, phone_a_friend_counter, asktheaudience_counter))
    question_counter += 1
    q10input = input('Please Type in Your Answer: ').lower()
    if q10input == 'köppen' or q10input == 'c' or q10input == 'koppen':
        return "\033[92m" + "Outstanding! That's Correct!"
    elif q10input == 'withdraw':
        print('You have withdrawn ' + str(money_counter) + ' dollars at question ' + str(question_counter) +
              ', thank you for playing Who wants to be a Millionaire!')
        return sys.exit()
    elif q10input == '50/50' and fiftyfifty_counter != 1:
        print('No more 50/50 remaining!')
        return q10()
    elif q10input == '50/50' and fiftyfifty_counter == 1:
        fiftyfifty_counter -= 1
        return fiftyfifty(q10fiftyfifty, q10answer)
    elif q10input == 'call the computer' and phone_a_friend_counter != 1:
        print('No more Call the Computer remaining!')
        return q10()
    elif q10input == 'call the computer' and phone_a_friend_counter == 1:
        phone_a_friend_counter -= 1
        return phoneafriend(q10call, q10answer)
    elif q10input == 'ask the audience' and asktheaudience_counter != 1:
        print('No more Ask The Audience remaining!')
        return q10()
    elif q10input == 'ask the audience' and asktheaudience_counter == 1:
        asktheaudience_counter -= 1
        return asktheaudience(q10ask, q10answer)
    else:
        print("\033[91m" + "That's the wrong answer! Game over :( The correct answer was: " + '\033[92m' +
              "c: Köppen" + "\033[91m" + "! you made it to question number", str(question_counter),
              "and left with", str(money_received), "dollars")
        return sys.exit()


print(q10())
money_counter = '1,000,000'
print("\033[94m" + "Congratulations " + name + "!!! You are now a *virtual* Millionaire~~ Thank you for playing :) ")
