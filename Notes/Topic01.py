#Sequential
print('This is sequential')
conditional = False
#conditional
if(conditional):
    #statements below here
    print('We are in the if branch') #if branch
elif(not conditional):
    print('We are in the else if branch.')
else:
    print('We are in the else branch') #else branch

#Back to sequential
print('This always happens since it is not indented.')

age = 17
movie = 'r'
if (age < 17 and age > 10 and movie == 'r'):
    print('age below 17.')