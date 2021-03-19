# write a code that reads the sex of the people (Male or Female).
# exemple: insert your sex (M/F):
# if the program recive M or F, its stop and show a messenger 'You are Male/You are Female.'
# But if recive another word will restart the question.

while True:
    response = input('\nInsert your sex (M/F): ')
    if (response.upper() == 'M'):
        print('\nYour sex is Male.')
        break
    elif (response.upper() == 'F'):
        print('\nYour sex is Female.')
        break
    else:
        print(f'\nSelect your sex.')
