# main function to invoke other function for complete gaming experience "TIC_TAC_TOE
def main():
    while True :
        status=(input('Do You Want To Play GAME(Enter Y/N)  ')).upper()
        if status=='Y':
                 gameplay()
        elif status=='N':
                 print('Thank you for playing')
                 break
        else:
                 print('Enter correct input Y/N   ')
#to print gaming board
from IPython.display import clear_output
def print_board(board):
    clear_output()
    print(' ',board[1],' | ',board[2],' | ',board[3])
    print('________________')
    print(' ',board[4],' | ',board[5],' | ',board[6])
    print('________________')
    print(' ',board[7],' | ',board[8],' | ',board[9])

# to check correct input range
def chkinpt(k):
        if k >=1 and k <=9 :
                return True
        else :
                return f"Wrong Input : Out of Range"


# to get input for entering at particular place
def playerinput():
    while 1>0:
        key=int(input('Enter the position to enter your symbol 1-9  '))
        if chkinpt(key)==True :
            return key
        else :
            print(chkinpt(key))
            continue


# to assign 'X' or 'O' at particular space
def boardasn(board,key,mark):
          board[key]=mark
          print_board(board)



# to check for possible win
def win_check(board,mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# complete basic gameplay
def gameplay():
    print('Welcome to Tic Tac Toe game  ')
    check ='true'
    P1,P2='',''
    key,turn=0,1
    mboard=[' ']*10
    while check:
        P1=input('Please Select "X" or "O"  ').upper()
        if P1=='X':
                 P2='O'
                 break
        elif P1=='O':
                 P2='X'
                 break
        else :
                 print('Enter Correct Symbol  ')

    while True:
                if turn==1:
                          key=playerinput()
                          while 1>0:
                                             if checkspace(mboard,key):
                                                       boardasn(mboard,key,P1)
                                                       break
                                             else :
                                                       print('Already filled,enter in empty place plz Player 1 as ',P1)
                                                       key=playerinput()
                          if win_check(mboard,P1):
                                         print('Player 1 has won')
                                         break
                          elif fullcheck(mboard):
                            print('Match draw')
                            break
                          else:
                            turn=2
                            print('Pass the turn to Player 2: ',P2)
                elif turn==2:
                          key=playerinput()
                          while 1>0:
                                     if checkspace(mboard,key):
                                                       boardasn(mboard,key,P2)
                                                       break
                                     else :
                                                       print('Already filled,enter in empty place plz Player 2 as ',P2)
                                                       key=playerinput()


                          if win_check(mboard,P2):
                                         print('Player 2 has won')
                                         break
                          elif fullcheck(mboard):
                            print('Match draw')
                            break
                          else:
                            turn=1
                            print('Pass the turn to Player 1: ',P1)


# to check a particular space on board
def checkspace(board,key):
    return board[key] == ' '


# to check spaces on board and possible draw
def fullcheck(board):
    for i in range(1,10):
        if checkspace(board,i):
            return False
    return True
if __name__== "__main__":
    main()
