# CTI-110
# P4HW1 - Score List
# Akil Duncan
# March 25, 2022
#

#declare variable for number of scores
numofscores = int(input("How many scores would you like to enter? "))

#creating an empty list to store scores
scoreslist = []

#create for loop for input of scores
for i in range(1, numofscores+1):
    while True:
        try:
            score = int(input("Enter score #{}: ".format(i)))
            
            if score >= 0 and score<=100:
                scoreslist.append(score)
                break
            else:
                print("INVALID score entered!!")
        except:
            continue
        
#display list
print("-----Results-----")
print(scoreslist)

#display lowest score entered
lowestscore = min(scoreslist)
print("\nLowest Score: {}".format(lowestscore))

#display modified list
scoreslist.remove(lowestscore)
print("\nModified List: ")
print(scoreslist)

#display average of modified scoreslist
avgofscoreslist = sum(scoreslist)/len(scoreslist)
print("\nScores Average: {}".format(avgofscoreslist))

#display letter grade
if avgofscoreslist>80 and avgofscoreslist<=100:
    print("Letter grade: A")
elif avgofscoreslist>60 and avgofscoreslist<=80:
    print("Letter grade: B") 
elif avgofscoreslist>40 and avgofscoreslist<=60:
    print("Letter grade: C")
elif avgofscoreslist>20 and avgofscoreslist>=40:
    print("Letter grade: D")
else:
    print("Letter grade: E")
