number1 = input('adad 1 : ')
number2 = input('adad 2 : ')
alamat = input('yek alamat (+,-,*,/): ')


if alamat == '+':
    answer = int(number1) + int(number2)
    print('javabe shoma : '+str(answer))
elif alamat == '-':
    answer = int(number1) - int(number2)
    print('javabe shoma : ' + str(answer))
elif alamat == '*':
    answer = int(number1) * int(number2)
    print('javabe shoma : ' + str(answer))
elif alamat == '/':
    answer = int(number1) / int(number2)
    print('javabe shoma : ' + str(answer))
else:
    print('alamat eshtebah ast.')
