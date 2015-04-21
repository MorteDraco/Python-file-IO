# anoying quiz 1
import random, time, string, collections
questions = 0
score = 0

def intro():#define the intro
    '''introduction'''
    print('welcome to the impossible quiz!')

def play():
    '''play'''
    play = str(input('would you like to play?\n(yes / no)\n'))#take user input to check if they want to play again.
    if play == 'yes' or play == 'y': #user inputs yes
        quiz2()
    else:  #player reutrns no
        print('Dont take '+ play + ' as an answer... play quiz!!!')
        play2()
def play2():
    play()
def quiz(): #part 1 of the quiz
    '''quiz'''
    global questions, score
    userinput = input().lower()
    answer = 'hello'
    
    if userinput == answer:
        print('correct')
        questions = questions + 1 #add question number 
        score = int(score)
        score=score + 1
        score = str(score)#convert to string to read

    elif userinput != answer:
        questions = questions + 1
        print('wrong, answer was: '+answer+' duh!!')



def quiz2(): #part 2 of the quiz
    '''quiz2'''
    global questions, score
    while questions <= 9: #check if questions are below 10
        quiz() #play the question

    score = str(score)
    print('your score was '+score+'/10\n ')
    name = input("Enter your name: ").rstrip() # make "foo" == "foo "

    with open("testAppend.txt","a+") as f: # a+ will allow us to read and will also create the file if it does not exist
        scores_list = f.readlines()
         # if scores_list is empty this is our first run
        if not scores_list:
            f.write("{}:{}\n".format(name, score))
        else:
            # else check for name and update score
            new_names = []
            for ind, line in enumerate(scores_list):
                # if name exists update name and score
                if name.rstrip() in line.split(":"):
                    scores_list[ind] = "{}:{}\n".format(line.rstrip(), score)
                    break # break so we don't add existing name to new names
            else:
                # else store new name and score
                new_names.append("{}:{}\n".format(name, score))


            # all scores updated so open and overwrite
            with open("highscores.txt","w") as scores_file:
                 scores_file.writelines(scores_list + new_names)
    start()

def scores1():
    print('\nPeople who have taken quiz:\n')
    with open('testAppend.txt', 'r') as r:
        for line in sorted(r): # sort linies 
            print(line, end='') # end the list of names

def stats():
    print('\nHigh scores\n')
    with open("testAppend.txt") as f:

        d = {}

        for line in f:
            column = line.split(":") # split when read an ':'
            names = column[0]  #assgin to colum
            scores = int(column[1].strip())

            count = 0
            while count < 3:
                d.setdefault(names, []).append(scores)
                count = count + 1

        averages=[]
        for name, v in d.items():
            average = (sum(v[-3:])/len(v[-3:]))
            averages.append((name, average))

        for name, average in sorted(averages, key=lambda a: a[1], reverse=True):
            print(name, average)

def lastT():
    with open("testAppend.txt", mode="r",encoding="utf-8") as fp:
            count = collections.defaultdict(int)
            rev = reversed(fp.readlines())
            rev_out = []

            for line in rev:
                name, value = line.split(':')
                if count[name] >= 3:
                    continue
                count[name] += 1
                rev_out.append((name, value))

    out = list(reversed(rev_out))
    print (out)

def menu():
    choice=input(str('What would you like? a / p / n / T\n'))
    if  choice == 'p':
        play()
    elif choice == 'a':
        scores1()
    elif choice == 'n':
        stats()
    elif choice == 'T':
        lastT()
        

def start(): # start menu
    '''start'''
    intro()
    menu()

start()
   
