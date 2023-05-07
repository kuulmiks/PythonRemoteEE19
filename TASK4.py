while True:

    firstnumber = float(input('Please insert the first number: \n'))
    user_input = input('Please select one of the following actions: A for addition, S for subtraction, M for multiplication, D for the division \n')
    while True:
        if user_input.lower() == 'a':
            break
        if user_input.lower() == 's':
            break
        if user_input.lower() == 'm':
            break
        if user_input.lower() == 'd':
            break
        else:
            print('Wrong action.')
            continue

    secondnumber = float(input('Please insert the second number: \n'))

    print('Your result is: \n')
    if user_input.lower() == 'a':
                result1 = firstnumber+secondnumber
                print(result1)
    if user_input.lower() == 's':
                result2 = firstnumber-secondnumber
                print(result2)
    if user_input.lower() == 'm':
                result3 = firstnumber * secondnumber
                print(result3)
    if user_input.lower() == 'd':
                result4 = firstnumber/secondnumber
                print(result4)

    user_input2 = input('Do you want to do more actions? Y for yes, N for no \n')
if user_input.lower() == 'y':
    continue
if user_input.lower() == 'n':
    break
else:
        print('Wrong action.')