print('**** Welcome to the LAB grade calculator! ****\n')
name = input('Who are we calculating grades for? ==> ')
print()

lab_g = float(input('Enter the LABS grade? ==> ')) #lab grades need to be between 0 and 100
if lab_g > 100: #check/correction for lab input greater than 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
    lab_g = 100
elif lab_g < 0 : #check/correction for lab input less than 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
    lab_g = 0
print()

exam_g = float(input('Enter the EXAMS grade? ==> ')) #exam grades also need to be between 0 and 100
if exam_g > 100: #check/correction for exam input greater than 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
    exam_g = 100
elif exam_g < 0: #check/correction for exam input less than 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
    exam_g = 0

print()
atten_g = float(input('Enter the Attendance grade? ==> '))
if atten_g > 100: #check/correction for attendance input greater than 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
    atten_g = 100
elif atten_g < 0: #chack/correction for attendance input less than 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
    atten_g = 0
print()

#calculates weighted grade based off of values in lab assignment
weight_g = (lab_g * .7) + (exam_g * .2) + (atten_g * .1)

#will print the name the user inputed above and round the weighted grade calculation to the tens place
print(f'The weighted grade for {name} is {round(weight_g, 1)}')

if 90 <= weight_g: #checks/prints for a grade between 90% and a 100% (inclusive)
    print(f'{name} has a letter grade of A')
elif 80 <= weight_g < 90: #checks/prints for a grade between 80% and 90%
    print(f'{name} has a letter grade of B')
elif 70 <= weight_g < 80: #checks/prints for a grade between 70% and 80%
    print(f'{name} has a letter grade of C')
elif 60 <= weight_g < 70: #checks/prints for a grade between 60% and 70%
    print(f'{name} has a letter grade of D')
else: #Prints if the grade is below 60%
    print(f'{name} has a letter grade of F')
print()
print('**** Thanks for using the Lab grade calculator ****')
