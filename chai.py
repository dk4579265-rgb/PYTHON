import time
print("chai is here")
username ="hitesh"
print(username)








##########  AGEN RIDE =__NEXT__,ITER,#####
########## ENTERVIOU QUCGAN ###########


#######
>>> f=open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("chai is here")\n'
>>> f.__next__()
'username ="hitesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> for line in open('chai.py'):
...     print(line)
...     
import time

print("chai is here")

username ="hitesh"

print(username)
>>> for line in open('chai.py'):
...     print(line, end='')
... 
import time
print("chai is here")
username ="hitesh"
>>> t(username)









#########################
> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> myNewList=[1,2,3]
>>> iter(myNewList) is myNewList
False
>>> 
