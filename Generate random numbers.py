import  random


def generate_two():
    while True:
        total_number = int(input('Enter the largerst number: '))
        
        random_num1 = random.randint(1,total_number)
        random_num2 = random.randint(1,total_number)
        
        print(f'{random_num1} and {random_num2}')
        
        while True:
            ask = input('Do you want to continue, Y or N?: ')
            if ask.upper() == 'Y':
               generate_two()
            elif ask.upper() == 'N':
                quit()
                
            else:
                print('Wrong input try again')
        
    
    
    
generate_two()