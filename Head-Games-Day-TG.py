#setting the score
score=0
concussion=0
#importing stuff

import os
import time
import random
print('        _.-=..=-._ ')
print('       /\\       //\ ')
print('      | ||-++++-|| |')
print('       \//      \\/')
print('         `-=..=-`')
print('Football by Tavi Greenfield')
print('DISCLAIMER')
print('Actions in this game may result in serious injury or death, specifically concussions. DO NOT REPLICATE OR TRY AT HOME. You will notice a concussion counter at the top left of your screen. This is a simulation of the concussions you will get playing football. BE SAFE.')
time.sleep(10)
os.system('clear')


#to give the user instructions:
instruct=(input('enter 1 to see the intructions(enter to skip)'))
if instruct=='1':
  print('This is a football video game. You wil start by seeing the football field. Your player is the 0. The defenders are the Xs. As you move, they will come at you. If they run into you, you are tackled. If the defenders run into each other, one of them falls. If they run out of bounds, they dissappear. You lose if you get tackled or run out of bounds. Use the w,a,s,d keys to move. You will have to press the key+enter to move(ex: to move forward, you have to press w+enter). Good luck! (enter to continue)')
  input('')
#drawing the lines
a=['---','---','---','---','---','---','---','---','---','---','---','---',]
b=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
c=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
d=['---','---','---','---','---','---','---','---','---','---','---','---',]
e=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
f=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
g=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
h=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
i=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
j=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
k=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
l=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
m=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
n=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
o=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
p=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
q=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
r=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
s=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
t=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
u=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
v=['---','---','---','---','---','---','---','---','---','---','---','---',]
w=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
hello=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
y=['---','---','---','---','---','---','---','---','---','---','---','---',]
field=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,hello,y]
#to print the field and goalposts
def printGoalPostsMiss():
  for x in range(3):
    print('                                    |     |    0                      ')
  print('                                     -----                            ')
  for x in range(3):
    print('                                       |                              ')
def printGoalPostsMake():
  for x in range(3):
    print('                                    |  0  |                           ')
  print('                                     -----                            ')
  for x in range(3):
    print('                                       |                              ')
def printGoalPosts():
  for x in range(3):
    print('                                    |     |                           ')
  print('                                     -----                            ')
  for x in range(3):
    print('                                       |                              ')
def printfield():
  os.system('clear')
  #field=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,hello,y]
  print(' concussions: '+str(concussion))
  print(' score: '+ str(score))
  
  for x in range(3):
    print('                 |     |                           ')
  print('                  -----                            ')
  for x in range(1):
    print('                    |                              ')
  for x in field:
    y=''
    y=y.join(x)
    print('|'+y+'|')
  for x in range(1):
    print('                    |                              ')
  print('                 -----                            ')
  for x in range(3):
    print('                |     |                           ')
playAgain=1
#initially printing the field
while playAgain==1:
  d=['---','---','---','---','---','---','---','---','---','---','---','---',]
  field=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,hello,y]
  printfield()
  #for whether or not a touchdown has been scored or has been tackled
  tackle=0
  touchdown=0
  #to place the player on the field
  field=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,hello,y]
  printfield()
  player=field[20]
  player[5]=' 0 '
  field[20]=player
  column=5
  row=20
  printfield()
  #to place defenders:
  additions=0
  while additions<5:
    randomNum=random.randrange(11)
    defenderOne=field[4]
    if defenderOne[randomNum]=='   ':
      defenderOne[randomNum]=' X '
      additions+=1
    field[4]=defenderOne
    printfield()
  #to move the player
  def movePlayerColumn(direct,col,ro):
    if direct=='d':
      col+=1
    if direct=='a':
      col-=1
    if direct=='s':
      ro+=1
    if direct=='w':
      ro-=1
    if col<(0) or col>11:
      col='out'
    return col
  def movePlayerRow(direct,col,ro):
    if direct=='d':
      col+=1
    if direct=='a':
      col-=1
    if direct=='s':
      ro+=1
    if direct=='w':
      ro-=1  
    return ro
  #to move the defenders
  def moveDefender(rowDef,field):
    defPlace=[]
    newDefPlace=[]
    playIndex=[]
    newDefenders=['   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ','   ',]
    
    defenders=field[rowDef]
    players=field[rowDef+1]
    #test
    #print (defenders)
    if ' 0 ' in players:
      playIndex.append(players.index(' 0 '))
    for x in defenders:
      if x==' X ':
        defIndex=defenders.index(x)
        defPlace.append(defIndex)
        defenders[defIndex]='   '
    
    #print(defenders)
    #test
    #print(defPlace)
    for x in defPlace:
      change=random.randrange((-1),2)
      x=x+change
      newDefPlace.append(x)
    tackled=1
    for x in newDefPlace:
      if x in playIndex:
        newDefenders=['tackle']
        tackled=2
      if x>(-1) and x<12 and tackled==1:
        newDefenders[x]=' X '
        if playIndex!=[]:
          newDefenders[playIndex[0]]=' 0 '
    #print('newDefPlace')
    #print(newDefPlace) 
    #test
    #print(newDefenders)
    #test
    #print(newDefenders)
    #input('')
    return newDefenders

        



  #more moving player(making him actually move)
  player=field[20]
  defRow=4
  sameRow=0

  while touchdown==0 and tackle==0:
    move=input('')
    
    column=movePlayerColumn(move,column,row)
    
    if column!='out':
      
        
      row=movePlayerRow(move,column,row)
      ind=player.index(' 0 ')
      player[ind]='   '
      player=field[row]
      #check for tackle
      if player[column]==' X ':
        tackle=1
        playAgain=2
      
      player[column]=' 0 '
    else:
      tackle=2
      playAgain=2
    #test
    #print(column)
    #print(player)
    field[row]=player
    #to check for a tackle
    #if defRow<20:
      #if ' 0 ' in field[defRow+1]:
        #playerPos=player.index(' 0 ')
        #sameRow=1

    advance='go'
    tackleCheck=moveDefender(defRow,field)
    #print('tackleCheck ')
    #test
    #print(tackleCheck)
    #printfield()
    #input('')
    #
    if 'tackle' in tackleCheck:
      advance='no'
    if advance=='no':
      tackle=1
      playAgain=2
    elif advance=='go':
      if defRow<20:
        field[defRow+1]=tackleCheck
        defRow+=1
    #to erase the last player(fixing a bug here)
    change=0
    if move=='a':
      change=0
      latChange=1   
    elif move=='w':
      change=1
      latChange=0 
    elif move=='s':
      change=(-1)
      latChange=0 
    elif move=='d':
      change=0
      latChange=(-1) 
    else:
      change=5
      latChange=0
    
    if defRow-1==row+change:
      
      for x in field[defRow-1]:
        if x==' 0 ':
            
          erasePlayer=field[defRow-1]
          #inDex=erasePlayer.index(x)
          erasePlayer[ind]='   '
          field[defRow-1]=erasePlayer


      
    #input('')
    
    #print (field[5])
    #sameRowCopy=field[defRow]

    #input('')
    printfield()
    #to check for a tackle
    #if sameRow==1:
      #if sameRowCopy[playerPos]==' X ':
        #tackle=1
    #if column=='out':
      #tackle=2
    if row==3:
      touchdown=1
      os.system('clear')
      score+=6
    concussion+=random.randrange(6)
  #if a touchdown has been scored
  if touchdown==1:
    print('touchdown!')
    #field goal and 2pt mechanics
    print('now you will kick a field goal or go for 2')
    choice='3'
    while choice!='1' and choice!='2':
      choice=input('which one? 1/2 ')
    #field goal mechanics
    if choice=='1':
      printGoalPosts()
      print('hit enter to start the timer, and hit enter again when you think exactly 3 seconds have passed')
      input('')
      #to keep track of time between inputs
      startTime=time.time()
      input('')
      endTime=time.time()
      timeElapsed=endTime-startTime
      #to check miss/make based on time
      os.system('clear')
      print('you waited '+str(timeElapsed)+' seconds')
      if timeElapsed>=2.5 and timeElapsed<=3.5:
        
        printGoalPostsMake()
        print('you made it!')
        score+=1
      else:
        
        printGoalPostsMiss()
        print('you shanked it right!')
    #2pt mechanics
    if choice=='2':
      additions=0
      while additions<5:
        randomNum=random.randrange(11)
        defenderOne=field[4]
        if defenderOne[randomNum]=='   ':
          defenderOne[randomNum]=' X '
          additions+=1
      field[4]=defenderOne
      field[3]=['---','---','---','---','---','---','---','---','---','---','---','---',]
      player=field[6]
      player[5]=' 0 '
      field[6]=player
      printfield()
      column=5
      row=6
      defRow=4
      touchdown=0
      tackle2=0
      while touchdown==0 and tackle2==0:
        move=input('')
      
        column=movePlayerColumn(move,column,row)
        
        if column!='out':
          
            
          row=movePlayerRow(move,column,row)
          ind=player.index(' 0 ')
          player[ind]='   '
          player=field[row]
          #check for tackle
          if player[column]==' X ':
            tackle2=1
            playAgain=2
          
          player[column]=' 0 '
        else:
          tackle2=2
          playAgain=2
        #test
        #print(column)
        #print(player)
        field[row]=player
        #to check for a tackle
        #if defRow<20:
          #if ' 0 ' in field[defRow+1]:
            #playerPos=player.index(' 0 ')
            #sameRow=1

        advance='go'
        tackleCheck=moveDefender(defRow,field)
        #print('tackleCheck ')
        #test
        #print(tackleCheck)
        #printfield()
        #input('')
        #
        if 'tackle' in tackleCheck:
          advance='no'
        if advance=='no':
          tackle2=1
          playAgain=2
        elif advance=='go':
          if defRow<20:
            field[defRow+1]=tackleCheck
            defRow+=1
        #to erase the last player(fixing a bug here)
        change=0
        if move=='a':
          change=0
          latChange=1   
        elif move=='w':
          change=1
          latChange=0 
        elif move=='s':
          change=(-1)
          latChange=0 
        elif move=='d':
          change=0
          latChange=(-1) 
        else:
          change=5
          latChnage=0
        
        if defRow-1==row+change:
          
          for x in field[defRow-1]:
            if x==' 0 ':
                
              erasePlayer=field[defRow-1]
              #inDex=erasePlayer.index(x)
              erasePlayer[ind]='   '
              field[defRow-1]=erasePlayer


          
        #input('')
        
        #print (field[5])
        #sameRowCopy=field[defRow]

        #input('')
        printfield()
        #to check for a tackle
        #if sameRow==1:
          #if sameRowCopy[playerPos]==' X ':
            #tackle=1
        #if column=='out':
          #tackle=2
        if row==3:
          if tackle2==0:
            touchdown=1
            
            score+=2
      os.system('clear')
      if touchdown==1:
        print('you scored the two point conversion!')
      elif tackle2==1:
        print('you were tackled and did not score the two point conversion...')
      else:
        print('you ran out of bounds, you did not score the two point conversion...')

    again=input('enter to continue, type anything to stop playing')
    if again=='':
      playAgain=1
    else:
      playAgain=2
#to tell the player they have been tackled
    if tackle==1:
      
      playAgain=2
    elif tackle==2:
      
      playAgain=2

if tackle==1:
  
  os.system('clear')
  print('you have been tackled!')
elif tackle==2:
  
  os.system('clear')
  print('you ran out of bounds!')
        
print('Great job! final score= ' + str(score))
users=['Emi','Tavi','Ely','Nathan','bob']
highScores=['47','19','14','13','0']
print('the current high scores are:')
place=0
for x in users:
  place+=1
  print(str(place)+'. '+(x)+' ('+(highScores[place-1])+'pts'+')')
print('if you scored higher than any of these, contact the game developer')
