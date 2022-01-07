# 69 marks total
# 45 marks will likely be 100%
# Start with the first 6 questions of the main program then you can start coding the functions.
# You are still welcome to start with the functions.
# As the functions signatures are given, it is possible to use (call) the functions prior to coding them.
#


# (5 marks)
# Write the following function: n <- calculateCoursePar(lPar)
# It receives a list of 18 integer and returns the sum of the integers.
#
def calculateCoursePar(lPar):
    return sum(lPar)

# (5 marks)
# Write the following function: n <- getNumberOfPars(lPar,lScore)
# It receives a list of Pars (an integer that represents the ideal number of strokes to play a hole)
# and a list of scores (an integer that indicates the actual number of strokes a player took to play a hole)
# The function the number of times the player shot par.
# as an example
# if   lPar =   [4,5,3,5,3,4,4,3,5,5,4,3,4,5,3,5,3,4]
# and  lScore = [5,6,5,4,4,4,3,4,6,5,4,3,5,3,3,5,3,4]
1, 1, 2, -1, 1, 1, -2,
# the function returns 8
def getNumberOfPars(lPar,lScore):
    times=0
    for i in range(0,18):
        if lPar[i]==lScore[i]:
            time=+1
    return times

# (4 marks )
# Write the following functions:
# n <- getNumberOfBirdies(lPar,lScore):
# n <- getNumberOfEagles(lPar,lScore):
# n <- getNumberOfBogeys(lPar,lScore):
# n <- getNumberOfDoubleBogeys(lPar,lScore):
#
# a Birdie is Par - 1
# a Bogey is Par + 1
# a Double Bogey is Par + 2
# an eagle is Par -2
def getNumberOfBirdies(lPar,lScore):
    times = 0
    for i in range(0, 18):
        if lPar[i] - lScore[i]== 0:
            time = +1
    return times
def getNumberOfEagles(lPar,lScore):
    times = 0
    for i in range(0, 18):
        if lPar[i] - lScore[i] == -1:
            time = +1
    return times
def getNumberOfBogeys(lPar,lScore):
    times = 0
    for i in range(0, 18):
        if lPar[i] - lScore[i] == -2:
            time = +1
    return times
def getNumberOfDoubleBogeys(lPar,lScore):
    times = 0
    for i in range(0, 18):
        if lPar[i] - lScore[i] == 2:
            time = +1
    return times
# (2 marks)
# Write the following function: n <- caculateTotalScore(lScore)
# It receives a list of 18 integer and returns the sum of the integers.
#
def caculateTotalScore(lScore):
    return sum(lScore)

# (5 marks)
# Write the following function: lB <- getListOfBirdies(lPar,lScore):
# Given the scorecard (lPar) and the scores (lScore)
# the function returns a list of hole numbers where the player scored a Birdie
# as an example
# if   lPar =   [4,5,3,5,3,4,4,3,5,5,4,3,4,5,3,5,3,4]
# and  lScore = [5,6,5,4,4,4,3,4,6,5,4,3,5,3,3,5,3,4]
# the function returns [4,7]
def getListOfBirdies(lPar,lScore):
    listBirdies = []
    for i in range(0, 18):
        if lPar[i] - lScore[i] == 1:
            listBirdies.append(i+1)
    return listBirdies

# (5 marks)
# Write the followinmg function:  (Winner,WinningScore) <- defineWinner(lDictionaries)
#
# The function receives a list of Dictionaries and returns a tuple that contains the name
# of the winner and the winning score.
#
# for an example of lDictionaries see 5. in the main program below.
def defineWinner(lDictionaries):
    lscore = [];
    lname = [];
    for i in lDictionaries:
        lscore.append(calculateCoursePar(i['score']))
        lname.append(i['player'])
    winningScore= min(lscore)
    winner = lname[lscore.index(winningScore)]
    return (winner,winningScore)

# (5 marks)
# Write the followinmg function:  n <- averageScore(hole,lDictionaries)
#
# The function receives an integer representing a hole number and a list of Dictionaries
# and returns the average score for that hole.
#
# for an example of lDictionaries see 5. in the main program below.
def averageScore(hole,lDictionaries):
    avgScore = 0;

    for i in lDictionaries:
        avgScore+= i['score'][hole]

    return avgScore / len(lDictionaries)

# (5 marks)
# Write the followinmg function:  lAvgScores <- listOfAvgScores(lDictionaries)
#
# The function receives  a list of Dictionaries
# and returns of the average scores on the 18 holes.
#
# for an example of lDictionaries see 5. in the main program below.
def listOfAvgScores(lDictionaries):
    score = 0
    for i in range (0,18):
        score += averageScore(i,lDictionaries)
    return score/18


######## Main Program ############

str = "4,5,3,5,3,4,4,3,5,5,4,3,4,5,3,5,3,4,Marshes"


# 1. (2 marks) Write python statement(s) code that converts this string into the following list
#
# l = ['4', '5', '3', '5', '3', '4', '4', '3', '5', '5', '4', '3', '4', '5', '3', '5', '3', '4', 'Marshes']
l = str.split(",")

# 2. (3 marks) Write python statement(s) code that converts the previous list into the following dictionary
# d = {"scorecard":[4,5,3,5,3,4,4,3,5,5,4,3,4,5,3,5,3,4],"Name":"Marshes"}
#
#NOTE:
# [4,5,3,5,3,4,4,3,5,5,4,3,4,5,3,5,3,4] the list represents the ideal number of strokes to play a hole.
# Hole 1 this number called the par is 4, Hole 2 it is 5, Hole 3 it is 3 etc... until Hole 18 which is 4
d = {"scorecard": l[0:18], "Name": l[18]}


# 3. (3 marks) Write python statement(s) to open the file "input.txt" and then store each line as
#  an entry into the list listOfLines:
#
# listOfLines = [
#        ['4', '5', '3', '5', '3', '4', '4', '3', '5', '5', '4', '3', '4', '5', '3', '5', '3', '4', 'Marshes\n'],
#        ['5', '6', '5', '4', '4', '4', '3', '4', '6', '5', '4', '3', '5', '3', '3', '5', '3', '4', 'Bob\n'],
#        ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', 'Jack\n'],
#        ['5', '6', '5', '4', '4', '4', '3', '4', '6', '5', '4', '3', '5', '3', '3', '5', '3', '4', 'Jill\n'],
#        ['6', '5', '4', '4', '4', '3', '4', '6', '5', '4', '3', '5', '3', '3', '5', '3', '4', '5', 'Marg']]

with open('input.txt', 'r') as f:
    # list=f.read()
    listOfLines = []
    for row in f:
        x = row
        listOfLines.append(x.split(','))
        if f.readline()=="":
            break

# 4. (1 mark) Write python statements to store the first line of listOfLines as a dictionatiary called dName.
#
# dName = {"scorecard":[4,5,3,5,3,4,4,3,5,5,4,3,4,5,3,5,3,4],"Name":"Marshes"}

dName = {"scorecard":listOfLines[0][0:18],"Name":listOfLines[0][18].strip('\n')}

# 5. (4 marks)Write python statements to store the last 4 lines of listOfLines as a list of dictionaries
# called  lPlayers.
#
# lPlayers = [
#    {'score': [5, 6, 5, 4, 4, 4, 3, 4, 6, 5, 4, 3, 5, 3, 3, 5, 3, 4], 'Player':'Bob' },
#    {'score': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'Player':'Jack' },
#    {'score': [5, 6, 5, 4, 4, 4, 3, 4, 6, 5, 4, 3, 5, 3, 3, 5, 3, 4], 'Player':'Jill' },
#    {'score': [6, 5, 4, 4, 4, 3, 4, 6, 5, 4, 3, 5, 3, 3, 5, 3, 4, 5], 'Player':'Marg' },
#]
#
# NOTE:
# [5, 6, 5, 4, 4, 4, 3, 4, 6, 5, 4, 3, 5, 3, 3, 5, 3, 4]  the list represents the score of the Player on the different holes
# Hole 1 Bob scored 5, Hole 2 Bob scored 6, Hole 3 Bob scored 5 etc... until Hole 18 Bob scored 4

lPlayers = [
    {'score': listOfLines[1][0:18], 'Player':listOfLines[1][18].strip('\n') },
    {'score': listOfLines[2][0:18], 'Player':listOfLines[2][18].strip('\n') },
    {'score': listOfLines[3][0:18], 'Player':listOfLines[3][18].strip('\n') },
    {'score': listOfLines[4][0:18], 'Player':listOfLines[4][18].strip('\n') },
    ]



# 6. (10 marks) Write the Python statements so that each entry of the list of Dictionaries also include the
# following statistics:

# Total: 76             (Total Score)
# PlusMinus: +4         (Total Score - Par of the course)
# Birdies: 2            (Number of birdies)
# Pars: 8               (Number of pars)
# Eagles: 1             (Number of eagles)
# Bogeys: 6             (Number of bogeys)
# Doubles: 1            (Number of doubles)
for i in lPlayers:
    i.update({"Total": caculateTotalScore(list(map(int,i['score'])))})
    i.update({"PlusMinus": caculateTotalScore(list(map(int,i['score']))) - calculateCoursePar(list(map(int,d['scorecard'])))})
    i.update({"Birdies": getNumberOfBirdies(list(map(int,d['scorecard'])),list(map(int,i['score'])))})
    i.update({"Pars": getNumberOfPars(list(map(int,d['scorecard'])),list(map(int,i['score'])))})
    i.update({"Eagles": getNumberOfEagles(list(map(int,d['scorecard'])), list(map(int,i['score'])))})
    i.update({"Bogeys": getNumberOfBogeys(list(map(int,d['scorecard'])), list(map(int,i['score'])))})
    i.update({"Doubles": getNumberOfDoubleBogeys(list(map(int,d['scorecard'])), list(map(int,i['score'])))})





# 7. (10 marks) Write the Python code that creates an HTML table with the Results
#    of the game then save this table into a HTML file.
#
#   Course | Par
#   --------------
#   Player | Score
#   Player | Score
#   Player | Score
out = open("myfile.html", "w")

out.write("<table>")
out.write("<tr><td>Course</td> <td>|</td><td>Par</td>")
for i in lPlayers:
    out.write("<tr><td>{}</td> <td>|</td><td>{}</td><tr>".format(i['Player'],caculateTotalScore(list(map(int,i['score'])))))
out.write("</table>")
out.close()