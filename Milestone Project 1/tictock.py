symb1='X'
symb2='O'
turn=1
win=False
dictionary= {1 : ' ', 2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
cells=[1,2,3,4,5,6,7,8,9]

''' this serve as a guid for players to now the number of each cell'''
numLine="  1 |  2 |  3  \n"
numLine2="  4 |  5 |  6 \n"
numLine3="  7 | 8  |  9 \n"
row="----|----|----\n"
guidedBoard= numLine+row+numLine2+row+numLine3
print("Guided Board\n",guidedBoard)


''' Draw board after each turn '''

def drawBoard(symb,num):
    dictionary[num]=symb
    i=0
    board=""
    for x in range(9):
        board+='  '+dictionary[x+1]+' |'
        i+=1
        if i==3:
            board+="\n----|----|----|\n"
            i=0
    '''board+='    |    |    |' '''
    print(board)
            
''' To check in each turn if player has won or now'''
def check(symb):
    if dictionary[1]==symb and dictionary[2]==symb and dictionary[3]==symb:
        print("Congrats team {}, you won !!!".format(symb)) 
        return True
    if dictionary[4]==symb and dictionary[5]==symb and dictionary[6]==symb:
        print("Congrats team {}, you won !!!".format(symb)) 
        return True
    if dictionary[8]==symb and dictionary[7]==symb and dictionary[9]==symb:
        print("Congrats team {}, you won !!!".format(symb)) 
        return True
    if dictionary[1] == symb and dictionary[5]==symb and dictionary[9]==symb:
        print("Congrats team {}, you won !!!".format(symb)) 
        return True
    if dictionary[3] == symb and dictionary[5]==symb and dictionary[7]==symb:
        print("Congrats team {}, you won !!!".format(symb)) 
        return True
    if dictionary[1]==symb and dictionary[4]==symb and dictionary[7]==symb:
        print("Congrats team {}, you won !!!".format(symb))
        return True
    if dictionary[3]==symb and dictionary[6]==symb and dictionary[9]==symb:
        print("Congrats team {}, you won !!!".format(symb))
        return True
    return False


'''  check if cell is empty '''

def isEmpty(num):
    if dictionary[num]=='X' or dictionary[num]=='O':
        return False
    return True



'''loop until one user is won or the cells are filled '''


while not (win):
    if (turn==1):
        nb = int(input('1st player please choose a number to place X: '))
        symb=symb1
        if(nb<=9 and nb>0):
            if(isEmpty(nb)):
                bd=drawBoard(symb,nb)
                win=check('X')
                turn=2
                cells.remove(nb)
            else:
                print('cell is full !! please enter an empty cell number ')
        else:
            print('number is not in range (1,9)')

    elif turn==2:
        nb =int(input('2st player please choose a number to place O: '))
        symb=symb2
        if(nb<=9 and nb>0):
            if(isEmpty(nb) and nb<=9 ):
                bd=drawBoard(symb,nb)
                win=check('O')
                turn=1
                cells.remove(nb)

            else:
                print('cell is full !! please enter an empty cell number ')
        else:print('number is not in range (1,9)')

    if len(cells)==0 and not win:
        print("Oh!! GAME OVER none of you won !")
        break
            
        
