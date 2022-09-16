
#controls the loop
x = True

#runs while x is true 
while x:
    
    #as the user for the remainder when their number is divided by 3
    rem_div_3 = int(input('What is the remainder when your number is divided by 3 ?'))
    
    if rem_div_3 >= 3: #execute if the value is too large
        print('The value entered must be less than 3')
    elif rem_div_3 < 0: #execute if the value is too small
        print('The value entered must be 0 or greater')
    else: #execute if the value is between 0 and 2 inclusive
        
        print()
        #ask the user for the remainder of the number when divided by 5
        rem_div_5 = int(input('What is the remainder when your number is divided by 5 ?'))
        
        print()
        #ask the user for the remaidner of their number when divided by 7
        rem_div_7 = int(input('What is the remainder when your number is divided by 7 ?'))

        '''find the number between 0 and 100 (inclusive) that has the correct remainder when
            divided by 3, 5, and 7'''
        for i in range(0,101):
            if i % 3 == rem_div_3 and i % 5 == rem_div_5 and i % 7 == rem_div_7:
                print(f'Your number was {i}')

        #ask the user if they would like to play again
        while True: #runs while the loop is True 
            option = input('Do you want to play agian? Y to continue, N to quit ==> ')

            #if they say no, set x to False and break out of this loop
            if option == 'N':
                x = False
                break
            #if they say yes, just break out of this loop
            elif option == 'Y':
                break
        



