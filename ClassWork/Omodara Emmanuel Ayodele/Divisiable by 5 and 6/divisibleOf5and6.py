#create a funtion 'divisible_by_five_and_six' to check number that are divisible by 5 and 6, and another function 'divisible_by_five_Or_six'that checks number that are divisible by 5 or 6.
#prompt user to input an integer number and store user input.
#check if user input is divisable by 5 or 6 using function (divisible_by_five_and_six) return and 'True' if it divisible by 5&6 else return 'false' if number is not.
#check user input again if it is divisable by 5 or 6 using function (divisible_by_five_Or_six) and return 'True' if number is true or 'False' if number is not either of them.
#check user input again if it is divisable by 5 or 6 but not both using function (divisible_by_five_Or_six) and return 'True' if number is true or 'False' if number is not either of them.



import calculator

user_Input = int (input('Enter a number: '))
result = (calculator.divisible_by_five_and_six(user_Input))
result_Two = (calculator.divisible_by_five_Or_six(user_Input))
result_Three = (calculator.divisible_by_five_Or_six(user_Input))
print(f'Is {user_Input} divisable by 5 and 6? {result}.')
print(f'Is {user_Input} divisable by 5 or 6? {result_Two}.')
print(f'Is {user_Input} divisable by 5 or 6, but not both? {result_Three}.')
