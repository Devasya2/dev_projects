import random
import sys
#helping user understand the game
print('MONSTER:')
print('Who dare disturbs me \n')
name = input("what is your name delicious meal?\n")
print("If you wish to slay me. Try\n")
print("Otherwise be my prey\n ")
print('MORTAL YOU HAVE ONLY 3 MEASLEY LIVES\n')
print('HA HA HA!')


playerlives=3
print('land attacks on the monster by solving the missing operator puzzles\n')
print ('lets begin')
#starting with first sequence of action
num1=random.randint(0,100)
num2=random.randint(0,100)
op = random.randint(0,2)
op_list = ['+','-','*']
if op==0:
        rhs=num1+num2
if op==1:
         rhs=num1-num2
if op==2:
         rhs=num1*num2
qn = str(num1)+'----'+ str(num2)+'='+str(rhs)+"\n"

answer=input(qn)

if answer != op_list[op]:

 while answer != op_list[op]:
    print('be careful try again\n')
    playerlives=playerlives-1
    print('lives left:',playerlives)
    if playerlives==1:
         print('last chance')
    if playerlives==0:
       print("you were eaten")
       sys.exit()
    answer=input(qn)

       
 print("moster is hurt")
 
else:
      print("you hurt the monster")
     

print('MONSTER: TIME TO STEP THINGS UP')

num3=random.randint(0,100)
num1=random.randint(0,100)
num2=random.randint(0,100)
op = random.randint(0,3)
op_list = ('+-','-+','++','--')
if op==0:
        rhs=num1+num2-num3
if op==1:
         rhs=num1-num2+num3
if op==2:
         rhs=num1-num2-num3
if op==3:
    rhs=num1+num2+num3
       
qn = str(num1)+'----'+ str(num2)+'-----'+str(num3)+'='+str(rhs)+"\n"
answer=input(qn)

if answer != op_list[op]:

 while answer != op_list[op]:
    print('be careful try again\n')
    playerlives=playerlives-1
    print('lives left:',playerlives)
    if playerlives==1:
         print('last chance')
    if playerlives==0:
       print("you were eaten")
       sys.exit()
    answer=input(qn)
 
else:
      print("you have slayed the monster. THE NEW CHAMPION is ",name)
    
    
 

        
      
