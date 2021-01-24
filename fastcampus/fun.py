def filter(string) :
    if 'skip' in string :
        print('SKIP')
        return 

user_input = ''
while user_input != 'quit' :
    user_input = input('Input = ')
    filter(user_input)
