#check a prime number or not
n=int(input("Please Enter a number:"))
if n<1:
        print("not a prime number")
for i in range(1,n):
        n%i==0
        print("__________________")
        print("Not a Prime Number")
        print("__________________")
        break
else:
        print("___________________________")
        print("Yes! This is a Prime number")
        print("___________________________")