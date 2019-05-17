

# Calculator
def calculator(num1,num2,c):
    if c=='1':
        return num1+num2
    elif c=='2':
        return num1-num2
    elif c=='3':
        return num1*num2
    elif c=='4':
        return num1/num2
firstnumber=float(input("Please Enter a number"))
secondnumber=float(input("please Enter a number"))
print("Operation Are:")
print("1 for Addition")
print('2 for subraction')
print('3 for Multiplication')
print("4 for Devision")
c=input('input selection:')
total=calculator(firstnumber,secondnumber,c)
print("Output is:"+str(total))
