# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:43:50 2019

@author: Dell
"""

import random
import sys
import os
import keyboard as k

def drawMat(mat):
    print("\n\n\t\t\t\t\t+-------+-------+-------+-------+")
    for i in range(len(mat)):
        print("\t\t\t\t\t|",end="")
        for j in range(len(mat[i])):
            if mat[i][j]==0:
                print("",end="\t|",)
            else:
                print(" ",mat[i][j],end="\t|")
        print("\n\t\t\t\t\t+-------+-------+-------+-------+")


def blankSpace(mat):
        pos=[]
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j]==0:
                    pos.append(i)
                    pos.append(j)
                    return pos
        
def isvalid(ch,bs):
    if ch==1 and bs[0]==3:
        return 0
    if ch==2 and bs[0]==0:
        return 0
    if ch==4 and bs[1]==0:
        return 0
    if ch==3 and bs[1]==3:
        return 0
    return 1
    
def isSolved(mat):
    temp=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    k=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=temp[k]:
                return False
            else:
                k+=1
                continue
    return True

def newmat(mat,bs,ch):
    i=bs[0]
    j=bs[1]
    temp=mat[i][j]
    if ch==1:
        mat[i][j]=mat[i+1][j]
        mat[i+1][j]=temp
    if ch==2:
        mat[i][j]=mat[i-1][j]
        mat[i-1][j]=temp
    if ch==4:
        mat[i][j]=mat[i][j-1]
        mat[i][j-1]=temp
    if ch==3:
        mat[i][j]=mat[i][j+1]
        mat[i][j+1]=temp
    return mat
       
    
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
random.shuffle(num)
mat=[]
nof_moves=0
for i in range(4):
    mat.append(num[:4])
    num=num[4:]
#print(mat)
while(1):
    os.system("cls")
    print("\n\t\t\t\t\t\tNO. OF MOVES:",nof_moves)
    drawMat(mat)
    while True:
        if k.read_key()=="q":
            ch=5
            break
        elif k.read_key()=="up":
            ch=1
            break
        elif k.read_key()=="down":
            ch=2
            break
        elif k.read_key()=="left":
            ch=3
            break
        elif k.read_key()=="right":
            ch=4
            break
        else:
            continue;
            
    if ch==5:
        sys.exit()
    b_pos=blankSpace(mat)
    #print(b_pos)
    if(isvalid(ch,b_pos)):
        nof_moves+=1
        mat=newmat(mat,b_pos,ch)
        if(isSolved(mat)):
            print("Puzzle solved")
            sys.exit()
        continue
    else:
        print("Invalid move")
        #continue
       
    