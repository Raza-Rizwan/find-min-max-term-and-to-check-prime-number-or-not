import random

a=[]
for i in range(10):
   a.append(random.randint(10,100))
   print(a)

#Minimum naumbers
print("\n\n")
max_num=a[0]
for i in range(10):
   if a[i] > max_num:
      max_num = a[i]
index=a.index(max_num)  
print("Maximim Number")    
print("*************************************************")
print("The maximum number in the List is:"+str(max_num))
print("And the index is:"+str(index))
print("*************************************************")

# Minimum number
print("\n")
min_num=a[0]
for i in range (10):
   if a[i] < min_num:
     min_num=a[i]
min_index=a.index(min_num)
print("Minimum Number")
print("*************************************************")
print("The minimum number in the list is:"+str(min_num))
print("And the index is:"+str(min_index))
print("*************************************************")