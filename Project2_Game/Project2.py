#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Project:To make a TIC TAC TOE and a SUDOKU Game
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:2-Oct-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[ ]:





# In[2]:


#TO CREATE A TIC TAC TOE GAME

import numpy as np
a='*'
game=[]
for i in range(0,9,1):
    game.append(a)
    
game=np.array(game)
game=game.reshape(3,3)

class TicTacToe:
    #Condition to check whether any row,column or diagonal is having a sum of 3 or -3
    def check(self):
        #To check if any row or column or diagonal count of 'X' becomes 3
        #It will return  as true
        if any(np.count_nonzero(game=='X',axis=1)==3) or any(np.count_nonzero(game=='X',axis=0)==3) or np.count_nonzero(np.diag(game)=='X')==3 or np.count_nonzero(np.diag(game[::-1])=='X')==3:
            return True
        #To check if any row or column or diagonal count of 'O' becomes 3
        #It will return  as true
        if any(np.count_nonzero(game=='O',axis=1)==3) or any(np.count_nonzero(game=='O',axis=0)==3) or np.count_nonzero(np.diag(game)=='O')==3 or np.count_nonzero(np.diag(game[::-1])=='O')==3:
            return True
        return False

    def player_turn(self):
        #For storing the Player value at (x,y) position in the game 
        #Note->x,y starts with 0 position
        x = int(input(f"{turn} Please enter the Row position:"))
        y = int(input(f"{turn} Please enter the Column position:"))
        try:
            if game[x,y]=='*':
                game[x,y]=value
            else:
                #If the psoition is already filled a user has to enter again
                print("Oops that position is already filled...Please Enter again...")
                self.player_turn()
        except IndexError:
            #For invalid position entered by the Player
            print("Oops Invalid Position...Please enter again...")
            self.player_turn()
#Rules for Tic Tac Toe Game
print("========Welcome to Tic Tac Toe Game==========================")
print("About this Game:")
print("1. There are 9 places present in the box")
print("2. A player has to enter the Row And Column where he want to insert")
print("3. Row and Column value should be in the range 0 to 2")
print("3. A player will win when the position of his values will be same either horizontally,vertically or diagonally")
print("========================================================")

#For storing Player names
player1=input("Enter the name of Player 1:")
player2=input("Enter the name of player 2:")

ob=TicTacToe()
turn=player1
see=0
#As in a tic tac toe game only 9 places have to filled
total=9
flag=0
value="X"
while(total >0):
    for i in range(0,3,1):
        for j in range(0,3,1):
            print(game[i,j],end="  ")
        print("")
    #Player_turn function is called so that a Player can enter his value at his desired position If available
    ob.player_turn()
    #To check wheteher any row,column,or diagonal sum is 3 or -3 if true then Won message wiil be displayed
    if(ob.check()):
        for i in range(0,3,1):
            for j in range(0,3,1):
                print(game[i,j],end="  ")
            print("")
        print (turn,"Has Won The Game.....")
        flag=1
        break
    #As there will be only two players so after each iteration next player name value will be stored in turn along with its value
    if(see%2==0):
        turn=player2
        value="O"
    else:
        turn=player1
        value="X"
    total=total-1
    see+=1
#If flag is 0 means that the game is draw
if(flag==0):
    print("That's a Draw.....Well Played")


# In[ ]:





# In[4]:


#TO CREATE A SUDOKU GAME

import numpy as np
class Board:
    #Initialy creating a game for the player
    def __init__(self):
        self.board = [['1','*','*','4','8','9','*','*','6'],
        ['7','3','*','*','*','*','*','4','*'],
        ['*','*','*','*','*','1','2','9','5'],
        ['*','*','7','1','2','*','6','*','*'],
        ['5','*','*','7','*','3','*','*','8'],
        ['*','*','6','*','9','5','7','*','*'],
        ['9','1','4','6','*','*','*','*','*'],
        ['*','2','*','*','*','*','*','3','7'],
        ['8','*','*','5','1','2','*','*','4']]

        self.board=np.array(self.board)

        self.board_solution=[]
    
    #Creating a solution for the sudoku game which is entered so that the players's ans can be checked
    def possible(self,row,column,number):
        #Checking whether the number appeared in the given row or not
        for i in range(0,9):
            if self.board[row][i] == str(number):
                return False

        #Checking whether the number appeared in the given column or not
        for i in range(0,9):
            if self.board[i][column] == str(number):
                return False

        #As in a sudoku game no number should be repeated in the square as well
        #So checking whether the number appeared in the square or not
        x = (column // 3) * 3
        y = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                #If present in the square return False
                if self.board[y+i][x+j] == str(number):
                    return False

        return True
    ans=[]
    
    #Filling the '*' places for creating a solution
    def solve(self):
        for row in range(0,9):
            for column in range(0,9):
                if self.board[row][column] == '*':
                    for number in range(1,10):
                        #Calling the possible function to get the number which can be fitted
                        if self.possible(row, column, number):
                            self.board[row][column] = str(number)
                            self.solve()
                            self.board[row][column] = "*"

                    return
        see=np.array(self.board)
        self.board_solution.append(see)

    #Checking for the player's input whether it is valid at that position or not
    def SetBoard(self, row, item, guess):
        if self.board[row][item] == "*":
            self.board[row][item] = str(guess) 
        else: 
            print("Incorrect position or not a proper number...Please Enter again..")  
        
    #Displaying how the baord will look after each time a player enter's his guess           
    def Display(self):
        for i in range(0,9,1):
            for j in range(0,9,1):
                print(self.board[i,j],end=" ")
            print("")
            
    #Checking whether board is full or not
    def Board_not_Full(self):
        for row in self.board:
            for item in row:
                if "*" == item:
                    return True
        return False

class Check:
    #Here the players's solution is checked with the actual solution 
    def BoardsAreEqual(self, board, board_solution):
        for i in range(0,len(board_solution),1):
            flag=0
            q=board_solution[i]
            for row in range(0,9,1):
                for column in range(0,9,1):
                    if(board[row][column]!=q[row][column]):
                        flag=1
                        break
            if(flag==0):
                return True
        return False


print('========Welcome to Sodoku==========================')
print('Important Rules:')
print('1. This is a 9x9 grid box. Valid numbers are 1 to 9')
print('2. Each row has all numbers from 1 to 9')
print('3. Each column has all numbers from 1 to 9')
print('4. Each 3x3 grid box has all numbers from 1 to 9')
print('5. In each Row no number should be repeated')
print('6. In each Column no number should be repeated')
print('7. In each sqaure box of 3x3 no number should be repeated')
print('8. Please Enter the Row and Column Value in the Range 0 to 8')
print('9. Enter quit to EXIT the game...Else press any key')
print("====================================================")
name=input("Plase Enter Your Name:")
print("========Welcome",name,"===========")

 

ob=Board()
ob.Display()
ob.solve()

#Checking whether Board is full or not
#If not then Asking the player to enter his choice of guess in the board at his desired position
#Note that position should be '*'
while ob.Board_not_Full() == True:
        try:
            row = int(input("Enter a row:"))
        except ValueError:
            print("Row must be a number from 0 to 8")

        try:
            item = int(input("Enter a column:"))
        except ValueError:
            print("Column must be a number from 0 to 8")
        try:
            guess = int(input("Enter a guess:"))
            if guess in range(1,10):
                try: 
                    ob.SetBoard(row, item, guess)
                except IndexError as other:
                    print(other)
                ob.Display()
            else:
                print("Guess should be in range 1 to 9.... Please correct.")
        except:
            print("Guess should be in range 1 to 9.... Please correct.")
        try:
            give_up = input("Enter quit to give up:")
            if give_up!="quit":
                continue
            else:
                break
        except:
            print('Must enter a character to continue.')
            if give_up =="quit":
                break


result = Check()

if(give_up=="quit"):
    print(name,"Thanks For Playing")
    
#Now if the board is completely filled,we will be checkimg the Players's ans with the actual solution
while ob.Board_not_Full() == False:
    if result.BoardsAreEqual(ob.board,ob.board_solution) == True:
        print("..........Congratulations ",name," You have solved the Sudoku correctly.....")
    else: 
        print(".......Nice Attempt ",name," But the solution is not correct.Thank you for playing.Please Try Again........")
    break
    


# In[ ]:




