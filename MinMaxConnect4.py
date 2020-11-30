
import math
import bitstring
import pygame
import sys


#RED IS 2
#BLUE IS 1
class Connect4:
    
#INITIATE THE BOARD
    def __init__(self):
        self.rows = 6
        self.cols = 8
        self.board = [[0]*self.cols for _ in range(self.rows)]
        self.yellow = 1
        self.red = 2
        self.round = 0
        self.last_move_row = -1
        self.last_move_col = -1
        self.possible_moves = ["f1","f2","f3","f4","f5","f6","f7","f8"]
        self.move_to_make = "f1"
        
        #TO ENSURE BOARD DOESN"T EXCEED PARAMS
        self.col_fil = [0,0,0,0,0,0,0,0]
        self.total_moves_allowed = 48
        
#RESET BOARD
    def initiate_empty_connect4(self):
        self.board = [[0]*self.cols for _ in range(self.rows)]
        self.round = 0
        self.last_move_row = -1
        self.last_move_col = -1
        
        self.col_fil = [0,0,0,0,0,0,0,0]
        self.total_moves_allowed = 48
    
#PRINT THE BOARD
    def print_board(self):
        row_str = ""
        print("f1 f2 f3 f4 f5 f6 f7 f8")
        print("-----------------------")
        for i in self.board:
            for j in i:
                if(j==1):
                    row_str += "B  "
                elif(j==2):
                    row_str += "R  "
                else:
                    row_str += "0  "
            print(row_str)
            print()
            row_str = ""
            

#TO FILL SPACES ON MAIN BOARD (USER INPUT)
    def fill_space(self,command):
#        command = input("Enter f1...f8/undo based on space\n")
        input_col = -1
        if(command == "f1" and self.col_fil[0]<6):
            input_col = 0
            self.col_fil[0] += 1
        elif(command == "f2" and self.col_fil[1]<6):
            input_col = 1
            self.col_fil[1] += 1
        elif(command == "f3"  and self.col_fil[2]<6):
            input_col = 2
            self.col_fil[2] += 1
        elif(command == "f4" and self.col_fil[3]<6):
            input_col = 3
            self.col_fil[3] += 1
        elif(command == "f5" and self.col_fil[4]<6):
            input_col = 4
            self.col_fil[4] += 1
        elif(command == "f6" and self.col_fil[5]<6):
            input_col = 5
            self.col_fil[5] += 1
        elif(command == "f7" and self.col_fil[6]<6):
            input_col = 6
            self.col_fil[6] += 1
        elif(command == "f8" and self.col_fil[7]<6):
            input_col = 7
            self.col_fil[7] += 1
        elif(command == "UNDO"):
            if(self.last_move_row != -1 and self.last_move_col != -1):
                self.board[self.last_move_row][self.last_move_col] = 0
                self.round -= 1
                self.col_fil[self.last_move_col] -= 1
                
            else:
                print("NOTHING TO UNDO")
        
        
        if(input_col != -1):
            iter = self.rows - 1
            while iter >= 0:
                if(self.board[iter][input_col]==0 and (self.round%2)==0):
                    #RED CHIP
                    self.board[iter][input_col]=2
                    self.last_move_row = iter
                    self.last_move_col = input_col
                    self.round += 1
                    break
                elif(self.board[iter][input_col]==0 and(self.round%2)==1):
                    #YELLOW CHIP
                    self.board[iter][input_col]=1
                    self.last_move_row = iter
                    self.last_move_col = input_col
                    self.round += 1
                    break
                iter -= 1
        else:
            print("NOT A POSSIBLE MOVE")
            self.total_moves_allowed += 1

    #CHECKS VERTICAL FOR A WIN
    def checkVertical(self,player):
        for i in range (0,self.cols):
            if(self.board[0][i]==player and self.board[1][i]==player and self.board[2][i]==player and self.board[3][i]==player):
                return True
            elif(self.board[1][i]==player and self.board[2][i]==player and self.board[3][i]==player and self.board[4][i]==player):
                return True
            elif(self.board[2][i]==player and self.board[3][i]==player and self.board[4][i]==player and self.board[5][i]==player):
                return True
        return False
        
    #CHECKS HORIZONTAL FOR A WIN
    def checkHorizontal(self,player):
        for i in range (0,self.rows):
            if(self.board[i][0]==player and self.board[i][1]==player and self.board[i][2]==player and self.board[i][3]==player):
                return True
            elif(self.board[i][1]==player and self.board[i][2]==player and self.board[i][3]==player and self.board[i][4]==player):
                return True
            elif(self.board[i][2]==player and self.board[i][3]==player and self.board[i][4]==player and self.board[i][5]==player):
                return True
            elif(self.board[i][3]==player and self.board[i][4]==player and self.board[i][5]==player and self.board[i][6]==player):
                return True
            elif(self.board[i][4]==player and self.board[i][5]==player and self.board[i][6]==player and self.board[i][7]==player):
                return True
        
        return False
    
    #CHECKS DIAGONAL FOR A WIN
    def checkDiagonal(self,player):
        for i in range (0,self.rows):
            for j in range (0,self.cols):
                if(self.board[i][j]==player and (i+1)<self.rows and (j-1)>=0 and (i+2)<self.rows and (j-2)>=0 and (i+3)<self.rows and (j-3)>=0):
                    if(self.board[i+1][j-1]==player and self.board[i+2][j-2]==player and self.board[i+3][j-3]==player):
                        return True
                    
                if(self.board[i][j]==player and (i+1)<self.rows and (j+1)<self.cols and (i+2)<self.rows and (j+2)<self.cols and (i+3)<self.rows and (j+3)<self.cols):
                    if(self.board[i+1][j+1]==player and self.board[i+2][j+2]==player and self.board[i+3][j+3]==player):
                        return True
        return False
        
    #CHECKS ALL FOR A WIN
    def checkVictory(self,player):
        return self.checkVertical(player) or self.checkHorizontal(player) or self.checkDiagonal(player)
        
    
        
    #TESTING SPECIFIC MOVES FOR MINMAX TREE
    def move_tester(self,move_tested,board_tester,maximizingPlayer):
        board_tester1 = [row[:] for row in board_tester]
        input_col = -1
        if(move_tested == "f1"):
            input_col = 0
        elif(move_tested == "f2"):
            input_col = 1
        elif(move_tested == "f3"):
            input_col = 2
        elif(move_tested == "f4"):
            input_col = 3
        elif(move_tested == "f5"):
            input_col = 4
        elif(move_tested == "f6"):
            input_col = 5
        elif(move_tested == "f7"):
            input_col = 6
        elif(move_tested == "f8"):
            input_col = 7
            
        iter = self.rows - 1
        while iter >= 0:
            if(board_tester1[iter][input_col]==0 and maximizingPlayer==2):
                #RED CHIP
                board_tester1[iter][input_col]=2
                break
            elif(board_tester1[iter][input_col]==0 and maximizingPlayer==1):
                #YELLOW CHIP
                board_tester1[iter][input_col]=1
                break
            iter -= 1
            
        return board_tester1
        
    
    
    #CHECKS VERTICAL FOR A HEURISTIC WIN
    def checkVertical_heur(self,player,curr_board):
        for i in range (0,self.cols):
            if(curr_board[0][i]==player and curr_board[1][i]==player and curr_board[2][i]==player and curr_board[3][i]==player):
                return True
            elif(curr_board[1][i]==player and curr_board[2][i]==player and curr_board[3][i]==player and curr_board[4][i]==player):
                return True
            elif(curr_board[2][i]==player and curr_board[3][i]==player and curr_board[4][i]==player and curr_board[5][i]==player):
                return True
        return False
        
    #CHECKS HORIZONTAL FOR A HEURISTIC WIN
    def checkHorizontal_heur(self,player,curr_board):
        for i in range (0,self.rows):
            if(curr_board[i][0]==player and curr_board[i][1]==player and curr_board[i][2]==player and curr_board[i][3]==player):
                return True
            elif(curr_board[i][1]==player and curr_board[i][2]==player and curr_board[i][3]==player and curr_board[i][4]==player):
                return True
            elif(curr_board[i][2]==player and curr_board[i][3]==player and curr_board[i][4]==player and curr_board[i][5]==player):
                return True
            elif(curr_board[i][3]==player and curr_board[i][4]==player and curr_board[i][5]==player and curr_board[i][6]==player):
                return True
            elif(curr_board[i][4]==player and curr_board[i][5]==player and curr_board[i][6]==player and curr_board[i][7]==player):
                return True
        
        return False
    
    #CHECKS DIAGONAL FOR A HEURISTIC WIN
    def checkDiagonal_heur(self,player,curr_board):
        for i in range (0,self.rows):
            for j in range (0,self.cols):
                if(curr_board[i][j]==player and (i+1)<self.rows and (j-1)>=0 and (i+2)<self.rows and (j-2)>=0 and (i+3)<self.rows and (j-3)>=0):
                    if(curr_board[i+1][j-1]==player and curr_board[i+2][j-2]==player and curr_board[i+3][j-3]==player):
                        return True
                    
                if(curr_board[i][j]==player and (i+1)<self.rows and (j+1)<self.cols and (i+2)<self.rows and (j+2)<self.cols and (i+3)<self.rows and (j+3)<self.cols):
                    if(curr_board[i+1][j+1]==player and curr_board[i+2][j+2]==player and curr_board[i+3][j+3]==player):
                        return True
        return False
        
    #CHECKS ALL FOR A HEURISTIC WIN
    def checkVictory_heur(self,player,curr_board):
        return self.checkVertical_heur(player,curr_board) or self.checkHorizontal_heur(player,curr_board) or self.checkDiagonal_heur(player,curr_board)
    
    
    
    #COUNTS NUMBER OF UNINTERRUPTED 2 AND 3 COLS
    def count_vertical_rows(self,player,curr_board):
        count2 = 0
        count3 = 0
        for i in range (0,self.cols):
            if(curr_board[0][i]==0 and curr_board[1][i]==player and curr_board[2][i]==player and curr_board[3][i]==player):
                #THREE FOUND
                count3 += 1
            elif(curr_board[1][i]==0 and curr_board[2][i]==player and curr_board[3][i]==player and curr_board[4][i]==player):
                #THREE FOUND
                count3 += 1
            elif(curr_board[2][i]==0 and curr_board[3][i]==player and curr_board[4][i]==player and curr_board[5][i]==player):
                #THREE FOUND
                count3 += 1
            elif(curr_board[0][i]==0 and curr_board[1][i]==0 and curr_board[2][i]==player and curr_board[3][i]==player):
                #TWO FOUND
                count2 += 1
            elif(curr_board[1][i]==0 and curr_board[2][i]==0 and curr_board[3][i]==player and curr_board[4][i]==player):
                #TWO FOUND
                count2 += 1
            elif(curr_board[2][i]==0 and curr_board[3][i]==0 and curr_board[4][i]==player and curr_board[5][i]==player):
                #TWO FOUND
                count2 += 1
                
        return (count2 * 0.3) + (count3 * 0.9)
                
                
    #COUNTS NUMBER OF UNINTERRUPTED 2 AND 3 ROWS
    def count_horizontal_rows(self,player,curr_board):
        count2 = 0
        count3 = 0
        for i in range (0,self.rows):
            str1 = str(curr_board[i][0]) + str(curr_board[i][1]) + str(curr_board[i][2]) + str(curr_board[i][3])
            str2 = str(curr_board[i][1]) + str(curr_board[i][2]) + str(curr_board[i][3]) + str(curr_board[i][4])
            str3 = str(curr_board[i][2]) + str(curr_board[i][3]) + str(curr_board[i][4]) + str(curr_board[i][5])
            str4 = str(curr_board[i][3]) + str(curr_board[i][4]) + str(curr_board[i][5]) + str(curr_board[i][6])
            str5 = str(curr_board[i][4]) + str(curr_board[i][5]) + str(curr_board[i][6]) + str(curr_board[i][7])
            
            
            #TWO FOUND
            if(str1.count('0')==2 and str1.count(str(player))==2):
                count2 += 1
            if(str2.count('0')==2 and str2.count(str(player))==2):
                count2 += 1
            if(str3.count('0')==2 and str3.count(str(player))==2):
                count2 += 1
            if(str4.count('0')==2 and str4.count(str(player))==2):
                count2 += 1
            if(str5.count('0')==2 and str5.count(str(player))==2):
                count2 += 1
           
           
            #THREE FOUND
            if(str1.count('0')==1 and str1.count(str(player))==3):
                count3 += 1
            if(str2.count('0')==1 and str2.count(str(player))==3):
                count3 += 1
            if(str3.count('0')==1 and str3.count(str(player))==3):
                count3 += 1
            if(str4.count('0')==1 and str4.count(str(player))==3):
                count3 += 1
            if(str5.count('0')==1 and str5.count(str(player))==3):
                count3 += 1
            
        return (count2 * 0.3) + (count3 * 0.9)
        
    
    #COUNTS NUMBER OF UNINTERRUPTED 2 AND 3 DIAGS
    def count_diagonals (self,player,curr_board):
        count2 = 0
        count3 = 0
        for i in range (0,self.rows):
            for j in range (0,self.cols):
                
                #THREE FOUND
                if(curr_board[i][j]==0 and (i+1)<self.rows and (j-1)>=0 and (i+2)<self.rows and (j-2)>=0 and (i+3)<self.rows and (j-3)>=0):
                    if(curr_board[i+1][j-1]==player and curr_board[i+2][j-2]==player and curr_board[i+3][j-3]==player):
                        count3 += 1
                    
                if(curr_board[i][j]==0 and (i+1)<self.rows and (j+1)<self.cols and (i+2)<self.rows and (j+2)<self.cols and (i+3)<self.rows and (j+3)<self.cols):
                    if(curr_board[i+1][j+1]==player and curr_board[i+2][j+2]==player and curr_board[i+3][j+3]==player):
                        count3 += 1
                
                if(curr_board[i][j]==player and (i+1)<self.rows and (j-1)>=0 and (i+2)<self.rows and (j-2)>=0 and (i+3)<self.rows and (j-3)>=0):
                    if(curr_board[i+1][j-1]==player and curr_board[i+2][j-2]==player and curr_board[i+3][j-3]==0):
                        count3 += 1
                        
                if(curr_board[i][j]==player and (i+1)<self.rows and (j+1)<self.cols and (i+2)<self.rows and (j+2)<self.cols and (i+3)<self.rows and (j+3)<self.cols):
                    if(curr_board[i+1][j+1]==player and curr_board[i+2][j+2]==player and curr_board[i+3][j+3]==0):
                        count3 += 1
                        
                #TWO FOUND
                if(curr_board[i][j]==0 and (i+1)<self.rows and (j-1)>=0 and (i+2)<self.rows and (j-2)>=0 and (i+3)<self.rows and (j-3)>=0):
                    if(curr_board[i+1][j-1]==0 and curr_board[i+2][j-2]==player and curr_board[i+3][j-3]==player):
                        count2 += 1
                        
                if(curr_board[i][j]==0 and (i+1)<self.rows and (j-1)>=0 and (i+2)<self.rows and (j-2)>=0 and (i+3)<self.rows and (j-3)>=0):
                    if(curr_board[i+1][j-1]==player and curr_board[i+2][j-2]==player and curr_board[i+3][j-3]==0):
                        count2 += 1
                
                if(curr_board[i][j]==player and (i+1)<self.rows and (j-1)>=0 and (i+2)<self.rows and (j-2)>=0 and (i+3)<self.rows and (j-3)>=0):
                    if(curr_board[i+1][j-1]==player and curr_board[i+2][j-2]==0 and curr_board[i+3][j-3]==0):
                        count2 += 1
                
                if(curr_board[i][j]==0 and (i+1)<self.rows and (j+1)<self.cols and (i+2)<self.rows and (j+2)<self.cols and (i+3)<self.rows and (j+3)<self.cols):
                    if(curr_board[i+1][j+1]==0 and curr_board[i+2][j+2]==player and curr_board[i+3][j+3]==player):
                        count2 += 1
                
                if(curr_board[i][j]==0 and (i+1)<self.rows and (j+1)<self.cols and (i+2)<self.rows and (j+2)<self.cols and (i+3)<self.rows and (j+3)<self.cols):
                    if(curr_board[i+1][j+1]==player and curr_board[i+2][j+2]==player and curr_board[i+3][j+3]==0):
                        count2 += 1
                        
                if(curr_board[i][j]==player and (i+1)<self.rows and (j+1)<self.cols and (i+2)<self.rows and (j+2)<self.cols and (i+3)<self.rows and (j+3)<self.cols):
                    if(curr_board[i+1][j+1]==player and curr_board[i+2][j+2]==0 and curr_board[i+3][j+3]==0):
                        count2 += 1
                
                
        return (0.3 * count2) + (0.9 * count3)
    
    
    #USED TO DETERMINE IF PLAYER2 BLOCKS PLAYER1
    def blocking_heuristic(self,player1,player2,curr_board):
        block2 = 0
        block3 = 0
        for i in range (0,self.rows):
            
            #3 HORIZONTAL ROWS BLOCKED BY PLAYER2
            if(curr_board[i][0]==player1 and curr_board[i][1]==player1 and curr_board[i][2]==player1 and curr_board[i][3]==player2):
                block3 += 1
            elif(curr_board[i][0]==player2 and curr_board[i][1]==player1 and curr_board[i][2]==player1 and curr_board[i][3]==player1 and curr_board[i][4]==player2):
                block3 += 1
            elif(curr_board[i][1]==player2 and curr_board[i][2]==player1 and curr_board[i][3]==player1 and curr_board[i][4]==player1 and curr_board[i][5]==player2):
                block3 += 1
            elif(curr_board[i][2]==player2 and curr_board[i][3]==player1 and curr_board[i][4]==player1 and curr_board[i][5]==player1 and curr_board[i][6]==player2):
                block3 += 1
            elif(curr_board[i][3]==player2 and curr_board[i][4]==player1 and curr_board[i][5]==player1 and curr_board[i][6]==player1 and curr_board[i][7]==player2):
                block3 += 1
            elif(curr_board[i][4]==player2 and curr_board[i][5]==player1 and curr_board[i][6]==player1 and curr_board[i][7]==player1):
                block3 += 1
                
            #2 HORIZONTAL ROWS BLOCKED BY PLAYER2
            if(curr_board[i][0]==player1 and curr_board[i][1]==player1 and curr_board[i][2]==player2):
                block2 += 1
            elif(curr_board[i][0]==player2 and curr_board[i][1]==player1 and curr_board[i][2]==player1 and curr_board[i][3]==player2):
                block2 += 1
            elif(curr_board[i][1]==player2 and curr_board[i][2]==player1 and curr_board[i][3]==player1 and curr_board[i][4]==player2):
                block2 += 1
            elif(curr_board[i][2]==player2 and curr_board[i][3]==player1 and curr_board[i][4]==player1 and curr_board[i][5]==player2):
                block2 += 1
            elif(curr_board[i][3]==player2 and curr_board[i][4]==player1 and curr_board[i][5]==player1 and curr_board[i][6]==player2):
                block2 += 1
            elif(curr_board[i][4]==player2 and curr_board[i][5]==player1 and curr_board[i][6]==player1 and curr_board[i][7]==player2):
                block2 += 1
            elif(curr_board[i][5]==player2 and curr_board[i][6]==player1 and curr_board[i][7]==player1):
                block2 += 1
            
            
        
            for j in range (0,self.cols):
            
                #3 VERTICAL COLS BLOCKED BY PLAYER2
                if(curr_board[0][j]==player2 and curr_board[1][j]==player1 and curr_board[2][j]==player1 and curr_board[3][j]==player1):
                    block3 += 1
                elif(curr_board[1][j]==player2 and curr_board[2][j]==player1 and curr_board[3][j]==player1 and curr_board[4][j]==player1):
                    block3 += 1
                elif(curr_board[2][j]==player2 and curr_board[3][j]==player1 and curr_board[4][j]==player1 and curr_board[5][j]==player1):
                    block3 += 1
                    
                #2 VERTICAL COLS BLOCKED BY PLAYER2
                if(curr_board[0][j]==player2 and curr_board[1][j]==player1 and curr_board[2][j]==player1):
                    block2 += 1
                elif(curr_board[1][j]==player2 and curr_board[2][j]==player1 and curr_board[3][j]==player1):
                    block2 += 1
                elif(curr_board[2][j]==player2 and curr_board[3][j]==player1 and curr_board[4][j]==player1):
                    block2 += 1
                elif(curr_board[3][j]==player2 and curr_board[4][j]==player1 and curr_board[5][j]==player1):
                    block2 += 1
                
                
            
        return (0.3 * block2) + (0.9 * block3)
    
    
    #MAKE FUNCTION THAT TAKES MOVE AND BOARD AND CHECKS IF IT IS VALID
    def check_move(self,curr_board,move_ma):
        if(curr_board[0][0]==0 and move_ma=='f1'):
            return True
        elif(curr_board[0][1]==0 and move_ma=='f2'):
            return True
        elif(curr_board[0][2]==0 and move_ma=='f3'):
            return True
        elif(curr_board[0][3]==0 and move_ma=='f4'):
            return True
        elif(curr_board[0][4]==0 and move_ma=='f5'):
            return True
        elif(curr_board[0][5]==0 and move_ma=='f6'):
            return True
        elif(curr_board[0][6]==0 and move_ma=='f7'):
            return True
        elif(curr_board[0][7]==0 and move_ma=='f8'):
            return True
        else:
            return False
    
    #SETTING UP THE HEURISTIC FUNC
    def heuristic_eval(self,curr_board):
        #NEED TO MAKE HEURISTIC FOR REMAINING BOARD TYPES
        total_score = 0
        
        #YELLOW VERTICAL
        total_score -= self.count_vertical_rows(1,curr_board)
        
        #YELLOW HORIZONTAL
        total_score -= self.count_horizontal_rows(1,curr_board)
            
        #YELLOW DIAGONAL
        total_score -= self.count_diagonals(1,curr_board)
        
        #RED VERTICAL
        total_score += self.count_vertical_rows(2,curr_board)
            
        #RED HORIZONTAL
        total_score += self.count_horizontal_rows(2,curr_board)
        
        #RED DIAGONAL
        total_score += self.count_diagonals(2,curr_board)
        
        #YELLOW BLOCKING
#        total_score -= self.blocking_heuristic(2,1,curr_board)
        
        #RED BLOCKING
#        total_score += self.blocking_heuristic(1,2,curr_board)
        
        
        return total_score
            
        
            
    
    #SETTING UP MINMAX TREE
    def minimax(self,curr_board,depth,maximizingPlayer,alpha,beta):
        if (self.checkVictory_heur(1,curr_board)):
            #CHECKS IF YELLOW WON
            return [-1000 + depth,"NA"]
        elif(self.checkVictory_heur(2,curr_board)):
            #CHECKS IF RED WON
            return [1000 + depth,"NA"]
        elif(depth == 0):
            return [self.heuristic_eval(curr_board),"NA"]
        
        if maximizingPlayer==2:
            #RED CHIP
            maxEval = -math.inf
            for move in self.possible_moves:
                
                if(self.check_move(curr_board,move)):
                    eval = self.minimax_helper(self.move_tester(move,curr_board,maximizingPlayer),depth-1,1,alpha,beta)
                    if(eval > maxEval):
                        self.move_to_make = move
                    maxEval = max(maxEval,eval)
                    
                    alpha = max(alpha,eval)
                    if beta <= alpha:
                        break
                    
            return [maxEval,self.move_to_make]
                    
        elif maximizingPlayer==1:
            #YELLOW CHIP
            minEval = math.inf
            for move in self.possible_moves:
            
                if(self.check_move(curr_board,move)):
                    eval = self.minimax_helper(self.move_tester(move,curr_board,maximizingPlayer),depth-1,2,alpha,beta)
                    if(eval < minEval):
                        self.move_to_make = move
                    minEval = min(minEval,eval)
                    
                    beta = min(beta,eval)
                    if beta <= alpha:
                        break
                    
            return [minEval,self.move_to_make]
        
    
    
    def minimax_helper(self,curr_board,depth,maximizingPlayer,alpha,beta):
    
        if (self.checkVictory_heur(1,curr_board)):
            #CHECKS IF YELLOW WON
            return (-1000 - (depth))
            
        elif(self.checkVictory_heur(2,curr_board)):
            #CHECKS IF RED WON
            return (1000 + (depth))
            
        elif(depth == 0):
            return self.heuristic_eval(curr_board)



        if maximizingPlayer==2:
            #RED CHIP
            maxEval = -math.inf
            for move in self.possible_moves:
                #EVAL MAY BE WRONG IF ITS SUPPOSED TO BE THE NEXT PLAYER AFTER MAXIMIZING
                if(self.check_move(curr_board,move)):
                    eval = self.minimax_helper(self.move_tester(move,curr_board,maximizingPlayer),depth-1,1,alpha,beta)
                    maxEval = max(maxEval,eval)
                    
                    alpha = max(alpha,eval)
                    if beta <= alpha:
                        break

            return maxEval
                
        elif maximizingPlayer==1:
            #YELLOW CHIP
            minEval = math.inf
            for move in self.possible_moves:
                if(self.check_move(curr_board,move)):
                    eval = self.minimax_helper(self.move_tester(move,curr_board,maximizingPlayer),depth-1,2,alpha,beta)
                    minEval = min(minEval,eval)
                    
                    beta = min(beta,eval)
                    if beta <= alpha:
                        break
                    


            return minEval
            
            
    
    #MAKING A MOVE FROM THE AI
    def ai_move(self,move_made):
        input_col = -1
        if(move_made == "f1" and self.col_fil[0]<6):
            input_col = 0
            self.col_fil[0] += 1
        elif(move_made == "f2" and self.col_fil[1]<6):
            input_col = 1
            self.col_fil[1] += 1
        elif(move_made == "f3") and self.col_fil[2]<6:
            input_col = 2
            self.col_fil[2] += 1
        elif(move_made == "f4" and self.col_fil[3]<6):
            input_col = 3
            self.col_fil[3] += 1
        elif(move_made == "f5" and self.col_fil[4]<6):
            input_col = 4
            self.col_fil[4] += 1
        elif(move_made == "f6" and self.col_fil[5]<6):
            input_col = 5
            self.col_fil[5] += 1
        elif(move_made == "f7" and self.col_fil[6]<6):
            input_col = 6
            self.col_fil[6] += 1
        elif(move_made == "f8" and self.col_fil[7]<6):
            input_col = 7
            self.col_fil[7] += 1
         
        if(input_col != -1):
            iter = self.rows - 1
            while iter >= 0:
                if(self.board[iter][input_col]==0 and self.round%2==0):
                    #RED CHIP
                    self.board[iter][input_col]=2
                    self.round += 1
                    break
                elif(self.board[iter][input_col]==0 and self.round%2==1):
                    #YELLOW CHIP
                    self.board[iter][input_col]=1
                    self.round += 1
                    break
                iter -= 1
                
            return 1
        else:
            print("NOT A POSSIBLE MOVE")
            self.total_moves_allowed += 1
            return 0
        


#TESTING CHECK MOVE FUNCTION TO SEE IF TOKEN EXCEEDS BOARD CONSTRAINTS
def constraints_test(con4):

    #TEST 1
    con4.board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]]
    print()
    con4.print_board()
    if(con4.check_move(con4.board,'f1')):
        print("TEST 1 CONSTRAINTS PASSED\n")
    else:
        print("TEST 1 CONSTRAINTS FAILED\n")
        
    #TEST 2
    con4.board = [[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0]]
    print()
    con4.print_board()
    if(not con4.check_move(con4.board,'f1')):
        print("TEST 2 CONSTRAINTS PASSED\n")
    else:
        print("TEST 2 CONSTRAINTS FAILED\n")
        
    #TEST 3
    con4.board = [[0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    print()
    con4.print_board()
    if(not con4.check_move(con4.board,'f2')):
        print("TEST 3 CONSTRAINTS PASSED\n")
    else:
        print("TEST 3 CONSTRAINTS FAILED\n")
        
    #TEST 4
    con4.board = [[0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    print()
    con4.print_board()
    if(not con4.check_move(con4.board,'f3')):
        print("TEST 4 CONSTRAINTS PASSED\n")
    else:
        print("TEST 4 CONSTRAINTS FAILED\n")
        
    #TEST 5
    con4.board = [[0,2,2,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    print()
    con4.print_board()
    if(not con4.check_move(con4.board,'f3')):
        print("TEST 5 CONSTRAINTS PASSED\n")
    else:
        print("TEST 5 CONSTRAINTS FAILED\n")
        
    #TEST 6
    con4.board = [[0,2,2,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1]]
    print()
    con4.print_board()
    if(con4.check_move(con4.board,'f5')):
        print("TEST 6 CONSTRAINTS PASSED\n")
    else:
        print("TEST 6 CONSTRAINTS FAILED\n")
        
        

#TESTING THE HEURISTIC TO SEE IF IT CAN ACCURATELY QUANITFY A BOARD
def heuristic_test(con4):

    #TEST 1
    curr_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1]]
    print("\nACTUAL HEURISTIC: " + str(con4.heuristic_eval(curr_board)))
    print("EXPECTED HEURISTIC -0.9")
    if(con4.heuristic_eval(curr_board)== -0.9):
        print("TEST 1 HEURISTIC PASSED\n")
    else:
        print("TEST 1 HEURISTIC FAILED\n")

    #TEST 2
    curr_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]]
    print("ACTUAL HEURISTIC: " + str(con4.heuristic_eval(curr_board)))
    print("EXPECTED HEURISTIC -0.3")
    if(con4.heuristic_eval(curr_board)== -0.3):
        print("TEST 2 HEURISTIC PASSED\n")
    else:
        print("TEST 2 HEURISTIC FAILED\n")

    #TEST 3
    curr_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,2,1,0,0,0,0],[0,0,2,1,0,0,0,0]]
    print("ACTUAL HEURISTIC: " + str(con4.heuristic_eval(curr_board)))
    print("EXPECTED HEURISTIC 0.0")
    if(con4.heuristic_eval(curr_board)== 0.0):
        print("TEST 3 HEURISTIC PASSED\n")
    else:
        print("TEST 3 HEURISTIC FAILED\n")
        
    #TEST 4
    curr_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0]]
    print("ACTUAL HEURISTIC: " + str(con4.heuristic_eval(curr_board)))
    print("EXPECTED HEURISTIC -2.4")
    if(con4.heuristic_eval(curr_board)== -2.4):
        print("TEST 4 HEURISTIC PASSED\n")
    else:
        print("TEST 4 HEURISTIC FAILED\n")
        
    #TEST 5
    curr_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,2,2,0,0],[0,0,0,1,1,1,0,0]]
    print("ACTUAL HEURISTIC: " + str(con4.heuristic_eval(curr_board)))
    print("EXPECTED HEURISTIC 0.0")
    if(con4.heuristic_eval(curr_board)== 0.0):
        print("TEST 5 HEURISTIC PASSED\n")
    else:
        print("TEST 5 HEURISTIC FAILED\n")
        
    #TEST 6
    curr_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,1,0,0,0]]
    print("ACTUAL HEURISTIC: " + str(con4.heuristic_eval(curr_board)))
    print("EXPECTED HEURISTIC -1.5")
    if(con4.heuristic_eval(curr_board)== -1.5):
        print("TEST 6 HEURISTIC PASSED\n")
    else:
        print("TEST 6 HEURISTIC FAILED\n")
    
    #TEST 7
    curr_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,1,1,0,0,0]]
    print("ACTUAL HEURISTIC: " + str(round(con4.heuristic_eval(curr_board),1)))
    print("EXPECTED HEURISTIC 0.6")
    if(round(con4.heuristic_eval(curr_board),1)== 0.6):
        print("TEST 7 HEURISTIC PASSED\n")
    else:
        print("TEST 7 HEURISTIC FAILED\n")




#CREATE BUTTON FOR MOVES
def create_moveButtons(x,y,w,h,inactive_color,text,text_size):
    font = pygame.font.SysFont("Poppins-ExtraLight.ttf", text_size)
    text_surf = font.render(text, True, (0,0,0))
    button_rect = pygame.Rect(x, y, w, h)
    text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'name': text,
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': inactive_color,
        }
    return button

#DRAW MOVE BUTTONS
def draw_moveButtons(button,screen):
#    shape_surf = pygame.Surface(button['rect'].size, pygame.SRCALPHA)
#    pygame.draw.rect(screen, button['color'], shape_surf.get_rect())
    pygame.draw.rect(screen, button['color'], button['rect'] )
    screen.blit(button['text'], button['text rect'])


#FUNCTION TO PLAY AGAINST A HUMAN
def play_human(con4,num_red_win,num_yellow_win):
    
    #INITIATING THE GAME
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([500,600])
    con4.initiate_empty_connect4()
    
    red_win = False
    yellow_win = False
    
    #TOTAL MOVES MADE BY BOTH PLAYERS
    movesMade = 0
    
    #BUTTON_MOVES
    f1 = create_moveButtons(50,460,50,50,(255,255,255),'1',40)
    f2 = create_moveButtons(100,460,50,50,(255,255,255),'2',40)
    f3 = create_moveButtons(150,460,50,50,(255,255,255),'3',40)
    f4 = create_moveButtons(200,460,50,50,(255,255,255),'4',40)
    f5 = create_moveButtons(250,460,50,50,(255,255,255),'5',40)
    f6 = create_moveButtons(300,460,50,50,(255,255,255),'6',40)
    f7 = create_moveButtons(350,460,50,50,(255,255,255),'7',40)
    f8 = create_moveButtons(400,460,50,50,(255,255,255),'8',40)
    Title_Screen = create_moveButtons(370,5,120,40,(249, 219, 109),'TITLE SCREEN',20)
    Play_Again = create_moveButtons(370,50,120,40,(90, 177, 187),'PLAY AGAIN',20)
    undo_move = create_moveButtons(385,520,65,65,(90, 177, 187),'UNDO',20)
    button_moves = [f1,f2,f3,f4,f5,f6,f7,f8,Title_Screen,Play_Again,undo_move]
    
    check_undo = False

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            
                #CLOSING THE WINDOW
                running = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                #CLICKING THE BUTTON
                if event.button == 1:
                    for button in button_moves:
                        if button['rect'].collidepoint(event.pos) and button['name'] == "TITLE SCREEN":
                            main()
                            
                        elif button['rect'].collidepoint(event.pos) and button['name'] == "PLAY AGAIN":
                            play_human(con4,num_red_win,num_yellow_win)
                            
                        elif button['rect'].collidepoint(event.pos) and button['name'] == "UNDO":
                            if(red_win == False and yellow_win == False and check_undo == False):
                                con4.fill_space(button['name'])
                                movesMade -= 1
                                check_undo = True
                            
                        elif button['rect'].collidepoint(event.pos) and button['name'] != "TITLE SCREEN" and button['name'] != "PLAY AGAIN" and movesMade < con4.total_moves_allowed and button['name'] != "UNDO":
                            
                            if(red_win == False and yellow_win == False):
                            
                                con4.fill_space("f" + button['name'])
                                movesMade += 1
                                check_undo = False
                                #CHECKS FOR WIN
                                if(con4.checkVictory(1)):
                                    yellow_win = True
                                    num_yellow_win += 1
                                elif(con4.checkVictory(2)):
                                    red_win = True
                                    num_red_win += 1
                                
                            
            elif event.type == pygame.MOUSEMOTION:
            
                #HOVERING OVER A BUTTON
                for button in button_moves:
                    if button['rect'].collidepoint(event.pos):
                        #CHANGE COLOR TO ACTIVE COLOR
                        button['color'] = (0,127,255)
                    elif button['name'] != "TITLE SCREEN" and button['name'] != "PLAY AGAIN" and button['name']!= "UNDO":
                       #CHANGE BACK TO INACTIVE COLOR FOR MOVE BUTTONS
                       button['color'] = (255,255,255)
                    elif button['name'] == "TITLE SCREEN":
                       button['color'] = (249, 219, 109)
                    elif button['name'] == "PLAY AGAIN" or button['name']== "UNDO":
                       button['color'] = (90, 177, 187)
                   
                
        #FILLING SCREEN WITH WHITE
        screen.fill((255, 255, 255))
          
        #SETTING BACKGROUND
        background_img = pygame.image.load("background3_3.png")
        screen.blit(background_img,(0,0))
          
        #HEADER FONT
        header_font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 50)
        screen.blit(header_font.render('CONNECT 4', True, (0,0,0)), (140,100))
    
    
        #MINI INSTRUCTIONS
        instructions = pygame.font.SysFont("Poppins-Italic.ttf", 25)
        screen.blit(instructions.render('RED GOES FIRST', True, (223, 41, 53)), (10,10))
        
        #NUMBER OF YELLOW WINS
        instructions = pygame.font.SysFont("Poppins-Italic.ttf", 20)
        screen.blit(instructions.render('BLUE WINS: '+ str(num_yellow_win), True, (0, 0, 0)), (10,45))
        
        #NUMBER OF RED WINS
        instructions = pygame.font.SysFont("Poppins-Italic.ttf", 20)
        screen.blit(instructions.render('RED WINS: '+ str(num_red_win), True, (0, 0, 0)), (10,30))
    
    
        #DRAW GRID
        starting_pos_x = 50
        starting_pos_y = 150
        for i in range (0,8):
            for j in range (0,6):
                pygame.draw.rect(screen,(0,0,0),(starting_pos_x+(i*50),starting_pos_y+(j*50),50,50),5)
                
                
        #DRAW BUTTONS
        for button in button_moves:
                    draw_moveButtons(button, screen)
                    
                  
        #DRAW TOKENS
        for x in range (0,con4.cols):
            for y in range (0,con4.rows):
                if(con4.board[y][x]==1):
                    pygame.draw.circle(screen,(19,87,190),(75+(x*50),175+(y*50)),20)
                elif(con4.board[y][x]==2):
                    pygame.draw.circle(screen,(223, 41, 53),(75+(x*50),175+(y*50)),20)


        #WINNING
        if(yellow_win):
            yellow_win_font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 50)
            screen.blit(yellow_win_font.render('BLUE WON', True, (19,87,190)), (150,530))
#            running = False
        elif(red_win):
            red_win_font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 50)
            screen.blit(red_win_font.render('RED WON', True, (223, 41, 53)), (160,530))
#            running = False
            

        pygame.display.flip()
    
    pygame.time.delay(5000)
    pygame.quit()

    
    
    
    
#FUNCTION TO PLAY AGAINST AN AI
def play_ai(con4,win,loss):

    #INITIATING THE GAME
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([500,600])
    con4.initiate_empty_connect4()
    
    red_win = False
    yellow_win = False
    
    movesMade = 0
    
    #BUTTON_MOVES
    f1 = create_moveButtons(50,460,50,50,(255,255,255),'1',40)
    f2 = create_moveButtons(100,460,50,50,(255,255,255),'2',40)
    f3 = create_moveButtons(150,460,50,50,(255,255,255),'3',40)
    f4 = create_moveButtons(200,460,50,50,(255,255,255),'4',40)
    f5 = create_moveButtons(250,460,50,50,(255,255,255),'5',40)
    f6 = create_moveButtons(300,460,50,50,(255,255,255),'6',40)
    f7 = create_moveButtons(350,460,50,50,(255,255,255),'7',40)
    f8 = create_moveButtons(400,460,50,50,(255,255,255),'8',40)
    Title_Screen = create_moveButtons(370,5,120,40,(249, 219, 109),'TITLE SCREEN',20)
    Play_Again = create_moveButtons(370,50,120,40,(90, 177, 187),'PLAY AGAIN',20)
    ai_move = create_moveButtons(50,520,65,65,(249, 219, 109),'AI MOVE',20)
    undo_move = create_moveButtons(385,520,65,65,(90, 177, 187),'UNDO',20)
    button_moves = [f1,f2,f3,f4,f5,f6,f7,f8,Title_Screen,Play_Again,ai_move,undo_move]
    
    round = 0
    
    depth = 5

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            
                #CLOSING THE WINDOW
                running = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                #CLICKING THE BUTTON
                if event.button == 1:
                    for button in button_moves:
                    
                        if button['rect'].collidepoint(event.pos) and button['name'] == "TITLE SCREEN":
                            main()
                        
                        elif button['rect'].collidepoint(event.pos) and button['name'] == "PLAY AGAIN":
                            play_ai(con4,win,loss)
                        
                        elif  button['rect'].collidepoint(event.pos) and button['name'] == "UNDO":
                            if(round%2==1 and red_win == False and yellow_win == False):
                                con4.fill_space(button['name'])
                                round -= 1
                                movesMade -= 1
                        
                        elif button['rect'].collidepoint(event.pos) and button['name'] == "AI MOVE":
                                                    
                            if(round%2 == 1 and movesMade < con4.total_moves_allowed and red_win == False and yellow_win == False):
                                #AI MAKES A MOVE
                                alpha = -math.inf
                                beta = math.inf
                                
                                valuation, best_move = con4.minimax(con4.board,depth,1,alpha,beta)
                                con4.ai_move(best_move)
                                round += 1
                                ai_check = False
                                movesMade += 1
                                                       
                                #CHECKS FOR WIN AFTER AI
                                if(con4.checkVictory(1)):
                                    yellow_win = True
                                    loss += 1
                                    break
                                elif(con4.checkVictory(2)):
                                    red_win = True
                                    win += 1
                                    break
                        
                        
                        elif button['rect'].collidepoint(event.pos) and button['name'] != "TITLE SCREEN" and button['name'] != "PLAY AGAIN":
                        
                            
                            if(round%2 == 0 and movesMade < con4.total_moves_allowed and red_win == False and yellow_win == False):
                                #HUMAN MAKES A MOVE
                                con4.fill_space("f" + button['name'])
                                round += 1
                                movesMade += 1
                                
                                #CHECKS FOR WIN
                                if(con4.checkVictory(1)):
                                    yellow_win = True
                                    loss += 1
                                    break
                                elif(con4.checkVictory(2)):
                                    red_win = True
                                    win += 1
                                    break
                        
                                
                                
                            
            elif event.type == pygame.MOUSEMOTION:
            
                #HOVERING OVER A BUTTON
                for button in button_moves:
                    if button['rect'].collidepoint(event.pos):
                        #CHANGE COLOR TO ACTIVE COLOR
                        button['color'] = (0,127,255)
                    elif button['name'] != "TITLE SCREEN" and button['name'] != "PLAY AGAIN" and button['name'] != "AI MOVE" and button['name'] != "UNDO":
                        #CHANGE BACK TO INACTIVE COLOR FOR MOVE BUTTONS
                        button['color'] = (255,255,255)
                    elif button['name'] == "TITLE SCREEN" or button['name'] == "AI MOVE":
                        button['color'] = (249, 219, 109)
                    elif button['name'] == "PLAY AGAIN" or button['name'] == "UNDO":
                        button['color'] = (90, 177, 187)
                    
                   
                
        #FILLING SCREEN WITH WHITE
        screen.fill((255, 255, 255))
          
        #SETTING BACKGROUND
        background_img = pygame.image.load("background3_3.png")
        screen.blit(background_img,(0,0))
          
        #HEADER FONT
        header_font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 50)
        screen.blit(header_font.render('CONNECT 4', True, (0,0,0)), (140,100))
    
    
        #MINI INSTRUCTIONS
        instructions = pygame.font.SysFont("Poppins-Italic.ttf", 25)
        screen.blit(instructions.render('RED GOES FIRST', True, (223, 41, 53)), (10,10))
        
        #LOSSES
        instructions = pygame.font.SysFont("Poppins-Italic.ttf", 20)
        screen.blit(instructions.render('LOSSES: '+ str(loss), True, (0, 0, 0)), (10,45))
        
        #WINS
        instructions = pygame.font.SysFont("Poppins-Italic.ttf", 20)
        screen.blit(instructions.render('WINS: '+ str(win), True, (0, 0, 0)), (10,30))
        
    
        #DRAW GRID
        starting_pos_x = 50
        starting_pos_y = 150
        for i in range (0,8):
            for j in range (0,6):
                pygame.draw.rect(screen,(0,0,0),(starting_pos_x+(i*50),starting_pos_y+(j*50),50,50),5)
                
                
        #DRAW BUTTONS
        for button in button_moves:
                    draw_moveButtons(button, screen)
                    
                  
        #DRAW TOKENS
        for x in range (0,con4.cols):
            for y in range (0,con4.rows):
                if(con4.board[y][x]==1):
                    pygame.draw.circle(screen,(19,87,190),(75+(x*50),175+(y*50)),20)
                elif(con4.board[y][x]==2):
                    pygame.draw.circle(screen,(223, 41, 53),(75+(x*50),175+(y*50)),20)

        #WINNING
        if(yellow_win):
            yellow_win_font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 50)
            screen.blit(yellow_win_font.render('BLUE WON', True, (19,87,190)), (150,530))
#            running = False
        elif(red_win):
            red_win_font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 50)
            screen.blit(red_win_font.render('RED WON', True, (223, 41, 53)), (160,530))
#            running = False
            
                

        pygame.display.flip()
    
    pygame.time.delay(5000)
    pygame.quit()
    
        
    

#DRAW PLAY_AI BUTTON AND PLAY_A_HUMAN BUTTON
def draw_button(button, screen):
    pygame.draw.rect(screen, button['color'], button['rect'])
    screen.blit(button['text'], button['text rect'])
    
    
    
#SET ATTRIBUTES FOR PLAY_AI BUTTON AND PLAY_A_HUMAN BUTTON
def create_button(x,y,w,h,inactive_color,text,func_name):
    font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 28)
    text_surf = font.render(text, True, (0,0,0))
    button_rect = pygame.Rect(x, y, w, h)
    text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'name': text,
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': inactive_color,
        'func': func_name
        }
    return button
    
    
        
def main():
    con4 = Connect4()

    #INITIATING WINDOW
    pygame.init()
    screen = pygame.display.set_mode([500,600])
    
    #AI BUTTON ATTRIBUTES
    buttonAI_width = 150
    buttonAI_height = 50
    buttonAI_x = 65
    buttonAI_y = 500
    
    #HUMAN BUTTON ATTRIBUTES
    buttonHum_width = 150
    buttonHum_height = 50
    buttonHum_x = 285
    buttonHum_y = 500
    
    #BUTTON CREATION
    buttonAI = create_button(buttonAI_x, buttonAI_y, buttonAI_width, buttonAI_height,(235,212,148), 'Play the AI',play_ai)
    buttonHum = create_button(buttonHum_x, buttonHum_y, buttonHum_width, buttonHum_height,(58,183,149), 'Play a Human',play_human)

    #BUTTON LIST
    button_list = [buttonAI, buttonHum]
    
    #BOOLEAN FOR WINDOW CLOSING
    running = True
    
    while running:
    
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            
                #CLOSING THE WINDOW
                running = False
                pygame.quit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                #CLICKING THE BUTTON
                if event.button == 1:
                    for button in button_list:
                        if button['rect'].collidepoint(event.pos):
                            button['func'](con4,0,0)
                            pygame.quit()
                            
            elif event.type == pygame.MOUSEMOTION:
            
                #HOVERING OVER A BUTTON
                for button in button_list:
                    if button['rect'].collidepoint(event.pos):
                        #CHANGE COLOR TO ACTIVE COLOR
                        button['color'] = (0,127,255)
                    elif button['name']=='Play the AI':
                        #CHANGE BACK TO INACTIVE COLOR FOR AI BUTTON
                        button['color'] = (235,212,148)
                    elif button['name']=='Play a Human':
                        #CHANGE BACK TO INACTIVE COLOR FOR HUMAN BUTTON
                        button['color'] = (58,183,149)
                
                
        #FILLING SCREEN WITH WHITE
        screen.fill((255, 255, 255))
        
        #SETTING BACKGROUND
        background_img = pygame.image.load("background3_3.png")
        screen.blit(background_img,(0,0))
        
        #GET MOUSE POSITION
        mouse = pygame.mouse.get_pos()
        
        
        #HEADER FONT
        header_font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 50)
        screen.blit(header_font.render('CONNECT 4', True, (0,0,0)), (140,100))
        
        #CREATOR FONT
        name_font = pygame.font.SysFont("Poppins-ExtraLight.ttf", 22)
        screen.blit(name_font.render('CREATED BY ARNAV SARIN', True, (4, 150, 255)), (10,10))
        
        #DRAWING BUTTONS
        for button in button_list:
            draw_button(button, screen)
                
        pygame.display.flip()
    
    
    
if __name__ == "__main__":
    
    #MAIN PROGRAM
    main()
    
    #TESTING FUNCTIONS
#    con4 = Connect4()
#
#    constraints_test(con4)
#
#    heuristic_test(con4)
