# Calculating student grades
# Mar 11 2022
# CTI-110 P3HW1 - Debugging
# Akil Duncan
#

def main ():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is: C')
            else:
                if score >= D_score:
                    print('Your grade is: D')
                else:
                    if score >= F_score or score <= F_score:
                        print('Your grade is: F')

main()                
        
