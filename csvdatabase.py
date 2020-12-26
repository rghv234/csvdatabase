#employee database using csv module in python
import csv

def writefile():
    f=open('employee.csv','w')
    l=csv.writer(f,delimiter='|')
    d=['Empid','Name','Designation','Salary']
    l.writerow(d)
    while True:
        eid=int(input('enter the employee ID: '))
        name=input("enter the employee's name: ")
        desig=input('enter their designation: ')
        sal=int(input('enter the salary: '))
        r=[eid,name,desig,sal]
        l.writerow(r)
        c=input('do you wish to enter more? (enter y for yes and n for no): ')
        if c=='n' or c=='N':
            break
def readfile():
    f=open('employee.csv','r')
    m=csv.reader(f)
    for i in f:
        print(i)

#program execution begins here
while True:
    print('***EMPLOYEE DATABASE***')
    print('1.Write 2.Read 3.Exit')
    ch=int(input('what would you like to choose? (enter 1,2 or 3): '))
    if ch==1:
        writefile()
    elif ch==2:
        readfile()
    elif ch==3:
        break
    else:
        print('invalid choice')
    
