# Calculating the score average
# Feb 25 2022
# CTI-110 P2HW2 - Score Average
# Akil Duncan
#

#declare variable for score
score_list = []
score1 = float(input("Enter score #1: "))
score_list.append(score1)
score2 = float(input("Enter score #2: "))
score_list.append(score2)
score3 = float(input("Enter score #3: "))
score_list.append(score3)
score4 = float(input("Enter score #4: "))
score_list.append(score4)
score5 = float(input("Enter score #5: "))
score_list.append(score5)
score6 = float(input("Enter score #6: "))
score_list.append(score6)
score7 = float(input("Enter score #7: "))
score_list.append(score7)

#display list
print("-----Team Scores-----")
print(score_list)

#remove the lowest score
lowest = min(score_list)
score_list.remove(lowest)
print(score_list)
total = sum(score_list)

#print(total)
length = len(score_list)

#print(length)
average = total/length

print("Lowest Score: ", lowest)
print("Modified List: ", score_list)
print("Average: ", round(average, 2))





