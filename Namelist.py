def Script():
    nameList = []
    while True:
        userAnswer = input('Hi and welcome, please enter a name (or press Enter to stop): ')
        if userAnswer == '':
            break
        nameList.append(userAnswer) 
    
    
    print(f'The entered names were: {nameList}')
    

Script()
