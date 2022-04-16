# Organizing score list
# April 16, 2022
# CTI-110 P5HW1 - Score List
# Akil Duncan
#

# Function to display the Menu
def displayMenu():
    print("---------------MENU--------------------")
    print("1) Create Score List")
    print("2) Display results")
    print("3) Exit")
    print("---------------------------------------")

# Get the menu choice from the user
def getMenuChoiceFromUser():    
    validChoice = False
    while validChoice == False:
        userChoice = input("Enter your choice: ")
        if userChoice in ['1', '2', '3']:
            validChoice = True
        else:
            print("Invalid choice entered.Enter a vaid choice")
            displayMenu()
            validChoice = False
    return userChoice
        
# Function to check if the input entered by user is a number
def ValidNumber(number):
    try:
        number = int(number)
        return True
    except ValueError:
        print("Enter a numeric value")
        return False
    
# Creates the score list and returns it
def createScoreList():
    scoreList = []
    validScoreCount = False
    while validScoreCount == False:    
        scoreCount = input("How many scores would you like to enter?: ")  
        if ValidNumber(scoreCount):
            scoreCount = int(scoreCount)
            if scoreCount > 0:            
                validScoreCount = True
            else:
                print("INVALID ENTRY!")
                validScoreCount = False
        else:
            validScoreCount = False
    
    # Get the scores from the user
    validScore = False
    for i in range(scoreCount):
        validScore = False
        while validScore == False:
            score = input("Enter the #{} score: ".format(i+1))
            if ValidNumber(score):
                score = float(score)
                if (score >=0 and score <= 100):
                    validScore = True                    
                    scoreList.append(score)
                else:
                    print("Invalid Score Entered.Valid score is a number between 0 and 100")
                    validScore = False
            else:
                validScore = False
    # Return the score List
    return scoreList

# Function to evaluate the Score List
def evaluateScoreList(scoreList):
    lowestScore = float("Inf")
    for score in scoreList:
        if score <= lowestScore:
            lowestScore = score
    # Remove the lowest score from the list
    scoreList.remove(lowestScore)    
    # Get the average of the scores entered
    averageScore = sum(scoreList) / len(scoreList)
    # Round the average to two decimals
    averageScore = round(averageScore, 2)    
    # Get the grade letter for the score
    gradeLetter = ""
    # Score between 0 and 35 grade letter if F
    if averageScore >= 0 and averageScore <= 35:
        gradeLetter = "F"
    # Score between 36 and 50 grade letter if E
    elif averageScore > 35 and averageScore <= 50:
        gradeLetter = "E"
    # Score between 50 and 60 grade letter if D
    elif averageScore > 50 and averageScore <= 60:
        gradeLetter = "D"
    # Score between 60 and 70 grade letter if C
    elif averageScore > 60 and averageScore <= 70:
        gradeLetter = "C"
    # Score between 70 and 80 grade letter if B
    elif averageScore > 70 and averageScore <= 80:
        gradeLetter = "B"
    # Score between 80 and 90 grade letter if A
    elif averageScore > 80 and averageScore <= 90:
        gradeLetter = "A"
    # Score greater than 90 grade letter if A+
    elif averageScore > 90:
        gradeLetter = "A+"
    # Return the scoreList, lowestScore, averageScore and gradeLetter
    return scoreList, lowestScore, averageScore, gradeLetter
            
userEnteredScoreList = []
exitProgram = False            
while (exitProgram == False):
    displayMenu()
    choice = getMenuChoiceFromUser()    
    if choice == '1':        
        userEnteredScoreList = createScoreList()        
    elif choice == '2':        
        if len(userEnteredScoreList) > 0:    
            modifiedScorelist, lowScore, avgScore, gradeLtr = evaluateScoreList(userEnteredScoreList)
            print("Score list after removing the lowest score is: {}".format(userEnteredScoreList))
            print("Lowest Score entered is: ", lowScore)
            print("Average of score entered is: ", avgScore)
            print("Letter Grade is: ", gradeLtr)
        else:
            print("No Score Entered. Enter a score to display the results")
    elif choice == '3':
        # Print exit message when choice 3 is entered        
        print("Program exited.")
        exitProgram = True
