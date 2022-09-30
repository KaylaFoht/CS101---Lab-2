########################################################################
##
## CS 101 Lab
## Program # 5
## Name Kayla Foht
## Email kkfzbf@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################



# import statements
import string
import math

#functions
def get_school(school):
    #checks which school the student is from
    if school[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif school[5] == '2':
        return 'School of Law'
    elif school[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'

def get_grade(grade):
    #checks which grade the student is in
    if grade[6] == '1':
        return 'Freshman'
    if grade[6] == '2':
        return 'Sophomore'
    if grade[6] == '3':
        return 'Junior'
    if grade[6] == '4':
        return 'Senior'
    if grade[6] == '5':
        return 'Invalid Grade'

def get_check_digit(check):
    #calculates the check digit

    #this set calculates the integer value of the first five letters and assigns them to variables
    f_alpha = string.ascii_uppercase.index(check[0])
    s_alpha = string.ascii_uppercase.index(check[1])
    t_alpha = string.ascii_uppercase.index(check[2])
    fo_alpha = string.ascii_uppercase.index(check[3])
    fi_alpha = string.ascii_uppercase.index(check[4])

    #first_five is the addition of the integer values of the first five letters multiplied by their position in the card number
    first_five = (f_alpha*1) + (s_alpha*2) + (t_alpha*3) + (fo_alpha*4) + (fi_alpha*5)

    #the next set will calculate the value of the integers
    global int_list #int_list is assigned to a global variable because it is used in verify_check_digit
    int_list = [] #the list where I will put the integers of the string
    count = 0 #used to make sure we only pull digits after the 4th index (earlier should all be letters)

    for i in check: #'for i in the card number, 
        if count >= 5: #if the index is greater than 5, 
            int_list.append(int(i)) #append int_list with the integer data type of that number
        count += 1 #increment count by 1

    #num is the addition of the integers in int_list multiplid by their position in the card number
    num = (int_list[0]*6) + (int_list[1]*7) + (int_list[2]*8) + (int_list[3]*9)

    #check digit is the remaineder of the sum of all of the values of the card number when divided by ten
    check_digit = (first_five + num) % 10

    return check_digit
        

def verify_check_digit(valid):

    #checks the length of the card number
    if len(valid) != 10:
        return False, "The length of the number given must be 10"

    #check that the first five characters are letters
    count = 0
    for i in valid:
        if i.isdigit() and count <= 4:
            return False, "The first 5 characters must be A-Z, the invalid character is at {} is {}".format(count, valid[count])
            break
        count += 1

    #checks that 7-9 are numbers
    num_count = 0
    for i in valid:
        if i.isalpha() and num_count >= 7:
            return False, "The last 3 characters must be 0-9, the invalid character is at {} is {}".format(num_count, valid[num_count])
        num_count+=1

    #checks that the sixth character is 1, 2, or 3 (school)
    if int(valid[5]) > 3 or int(valid[5]) < 1:
        return False, "The sixth character must be 1 2 or 3"

    #checks that the seventh character is 1, 2, 3, or 4 (grade)
    if int(valid[6]) > 4 or int(valid[6]) < 1:
        return False, "The seventh character must be 1 2 3 or 4"

    #checks that the check digit matches the final number in the library card
    check_digit = get_check_digit(valid)
    if check_digit != int_list[-1]:
        return False, "Check Digit {} does not match calculated value {}.".format(int_list[-1], check_digit)

    #returns if valid card number
    return True, ""

if __name__ == "__main__":

    # main program
    print("Main Program") #this was here; I left it alone
    x = True #runs the while loop
    
    while x == True:
        print()
        cardnum = input('Enter Library Card. Hit Enter to Exit ==> ')

        #if they input nothing, break from the while loop and set it to false
        if cardnum == '':
            x == False
            break

        #if verify_check_digit returns False, print the reason why and loop back for another input
        t_f, reason = verify_check_digit(cardnum)
        if t_f == False:
            print(reason)
            continue

        #if verify_check_digit returns true, tell the user it is true, which school the student is from, and which gradae the student is in
        #BUT still ask the student for another card number by not ending the loop. Loop until they just press enter.
        else:
            print('Library card is valid.')
            print(f'The card belongs to a student in {get_school(cardnum)}')
            print(f'The card belongs to a {get_grade(cardnum)}')
    















    
            
    

