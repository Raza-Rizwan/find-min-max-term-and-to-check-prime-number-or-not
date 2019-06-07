#Ningth Class Marksheet

print("\n")
print("Please enter a (Name , Father name and School) in a capitical Alphabate")
x=(input("Name:"))
y=(input("Father Name:"))
z=(input("School/Pravite:"))
w=int(input("ROll number:"))
print("\n")

#Please Enter a Marks
a="Biology Marks"
b="Biology Practical"
c="Chemistry Marks"
d="Chemistry Practical"
e="Sindhi Marks"
f="English Marks"
g="Pakistan Studies Marks"

#Grade numbers


a=int(input("Biology TH:"))
b=int(input("Biology PR:"))
c=int(input("Chemistry TH:"))
d=int(input("ChemistrY PH:"))
e=int(input("Sindhi SALEES:"))
f=int(input("English PAPER:"))
g=int(input("Pakistan Studies:"))

def check(h,i,j,k,l,m,n):
    if (h>=28) and (i>=5) and (j>=28) and (k>=5) and (l>=25) and (m>=25) and (n>=25):
        return("CLEAR")
    else:
        return("Failed")

def percentage(avg):
    if (avg > 80 and avg < 100):
       return("Grade:  A+")
    elif(avg > 70 and avg <= 79):
        return("Grade: A")
    elif(avg > 60 and avg <=69):
        return("Grade: B")
    elif(avg >= 50 and avg <=59):
        return("Grade: C")
    elif(avg >=40 and avg < 50):
        return("Grade: D")
    elif(avg < 40):
        return("Failed")

total=a+b+c+d+e+f+g
Avg=(total/425)*100
print("Percentage:"+ str(Avg), "%")
Total=percentage(Avg)
k=check(a,b,c,d,e,f,g)
print("\n\n")
print("\t\t\t\t      ----------\t\t\t\t")
print("\t\t\t\t      MARK SHEET \t\t\t\t")
print("\t\t\t\t      ----------\t\t\t\t")
print("\n")
print("______________________________________________________________________________________________")


print("\n\t\t\tBOARD OF SECOUNDARY EDUCATION\t\t")
print("\t\t\t\t  KARACHI\t\t\t\t")
print("\t\t\t     STATEMENT OF MARKS\t\t\t")
print("\t\t      S.S.C PART 1 (CLASS 9) EXAMINATION\t\t")
print("\t\t       (FOR SUCCESSFUL CANDIDATES ONLY)\t\t\n\n")

print("EXAMINATION  ANNUAL  -  2019        ROLL NUMBER                      "+str(w))
print("                                    GROUP                            SCIENCE")


print("\n")
print("NAME            "+x)
print("FATHER'S NAME   "+y)
print("SCHOOL/PRAVITE  "+z)
print("\n")

print("SUBJECT                        MAXIMUM   MINIMUM       MARKS")
print("-------                         MARKS   PASS MARKS    OBTAINED       ")
print("                               -------  ----------    --------       ")
print("\nSINDHI SALEES                   75         25           "+ str(e))
print("\nENGLISH PAPER                   75         25           "+ str(f))
print("\nPAKISTAN STUDIES                75         25           "+ str(g))
print("\nBIOLOGY THEORY                  85         28           "+ str(a))
print("\nBIOLOGY PRACTICAL               15         05           "+ str(b))
print("\nCHEMISTARY THEORY               85         28           "+ str(c))
print("\nCHEMISTARY PRACTICAL            15         05           "+ str(d))

print("\n")
print("                                            "+k)
print("                                 GRAND TOTAL: "  +str(total),   "Out of 425")
print("\t\t\t\t\t      __________")
print("\t\t\t\t\t      "+Total)
print("\t\t\t\t\t      __________")

    
   