from project import chkinpt
from project import checkspace
from project import win_check
import pytest

def test_chkinpt():
    assert chkinpt(0)=="Wrong Input : Out of Range"
    assert chkinpt(9)==True
    assert chkinpt(10)=="Wrong Input : Out of Range"

#Test Board
board=[' ']*10
board[4],board[5],board[6]='X','X','X'
board[1],board[2],board[9]='O','O','O'
board[7],board[8],board[3]=' ',' ',' '

def test_checkspace():
    assert checkspace(board,8)==True
    assert checkspace(board,7)==True
    assert checkspace(board,2)==False

def test_win_check():
    assert win_check(board,'X')==True
    assert win_check(board,'O')==False