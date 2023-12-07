while True:
    a = int(input("Enter the Choice: "))
    s = input("Enter the string: ")

    if a == 1:
        print(s.upper())
    elif a == 2:
        print(s.lower())
    elif a == 3:
        print(s.swapcase())
    elif a == 4:
        print(s[::-1])
    elif a == 5:
        print(len(s))
    elif a == 6:
        print(s.title())
    elif a == 7:
        print(s.isalpha())
    elif a == 8:
        print(s.islower())
    elif a == 9:
        print(s.isupper())
    elif a == 10:
        print(s.istitle())
    else:
        print('Enter a valid option')

    rep = input('Do you want to continue? (Yes/No): ')
    if rep.lower() != 'yes':
        break