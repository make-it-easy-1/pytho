#this is a simple programe in python of a calculator to practice 
def add(x,y):
 return x+y

def sub(x,y):
 return x-y

def mul(x,y):
 return x*y
  
def div(x,y):
 return x/y


choice =input( "please select an operator \n"\
       "1 for add \n " \
       "2 for substract \n " \
       "3 for multipaly \n" \
       "4 for division \n "
 ).isdigit()
print ("-------------------------------------------------")
x = int(input(" Enter number 1  "))
print ("-------------------------------------------------")
y = int(input(" Enter number 2  "))
print ("-------------------------------------------------")
 
if choice==1:
     print( x ,"+" , y ,"=" , add(x,y))

elif choice==2:
     print( x , "-" , y , "=" ,sub(x,y))

elif choice==3:
     print( x , "*" ,y , "=" , mul(x,y))

elif choice==4:
     print( x , "/" , y , "=" , div(x,y))
else :
   print('invalid ')
