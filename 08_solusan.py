#########  PRIME NUMBER CHECKER  ###########
  
  
number =17
  
is_prime =True
  
if number > 1:
  for i in range(2 , number):
      if (number % i)==0:
          is_prime=False
          break
print("this is a prime number:",is_prime)  
#print(is_prime)    



#output =this is a prime number: True
#(17 is prime numbr)