def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def valueInt(result):
    return int(result) if result == int(result) else result
print('select operations')
print('1.add')
print('2.sub')
print('3.mul')
print('4.div')

choice=input("enter choice(1/2/3/4)")
num1=float(input('enter your number'))
num2=float(input('enter your second number'))


if choice=='1':
    result=add(num1,num2)
    print(f'add is::{valueInt(result)}')

elif choice=='2':
    result=sub(num1,num2)
    print(f'sub is::{valueInt(result)}')
elif choice=='3':
    result=mul(num1,num2)
    print(f'mul is::{valueInt(result)}')
elif choice=='4':
  if num2!=0:
    result=div(num1,num2)
    print(f'div is::{valueInt(result)}')
  else:
        print('zero  division not allow')

elif choice>='4':
        print('enter valid number')

