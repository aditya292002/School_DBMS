#RUN THE FOLLOWING CODE TO CREATE DATABASE

import datetime
import mysql.connector as sq
import glob
import shutil
import os

var=sq.connect(host="localhost",user="root",passwd="Adikes209.",database="project1")
if var.is_connected:
    print("connected")
else:
    print("not connected")
cursor=var.cursor()
print("welcome!!")
print("if you are new enter 'n'")
print("to see your saved details enter 'y'")
counter=input("enter y/n : ")


ADMITION_NO = -1
if counter == "n":
    admition_no=int(input("enter you admition number : ")) #!
    ADMITION_NO = admition_no
    sname=input("enter your name : ")#2
    #datetime.datetime(2009,5,5)
    print("date of birth")
    a=int(input("enter year : "))
    b=int(input("enter month :"))
    c=int(input("enter day : "))
    dob=datetime.date(a,b,c)
    print("date of admittion : ")
    d=int(input("enter year : "))
    e=int(input("enter month : "))
    f=int(input("enter day : "))
    doa=datetime.date(d,e,f)
    class1=input("enter your class  : ")#5
    section=input("enter your section : ")#6
    guardian_n=input("enter guardian name : ")#8
    mobile_no=int(input("enter four mobile number : "))
    aadhar_no=int(input("enter four aadhar number : "))
    cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",(admition_no,sname,dob,doa,class1,section,guardian_n,mobile_no,aadhar_no))
    print("congratulations you are sucessfully registed to our database")
    var.commit()



    photo_input = input("Are you willing to add image of the student press Y/y for yes , any other key for no : ");
    print("Please Note the image formate should be 'jpg'")
    
    if(photo_input == "Y" or photo_input == "y"):
        src_dir = input("Enter the path to the image : ")
        
        src_dir_new = ""
        i = -1
        for i in range(len(src_dir)-1,0,-1):
            if(src_dir[i] == '/'):
                break

        for i in range(0,i+1):
            src_dir_new = src_dir_new + src_dir[i]
        src_dir_new = src_dir_new  + str(ADMITION_NO)
        print(src_dir_new)

        
        os.rename(src_dir, src_dir_new)

        for jpgfile in glob.iglob(os.path.join(src_dir_new)):
            shutil.copy(jpgfile, dst_dir)

else:
    admition_no1=int(input("enter your admition number : "))
    cursor.execute(("select * from student where admition_no =%s"),[admition_no1])
    data=cursor.fetchall()
    for i in data:
        print(i)

var.close()
counter2=int(input("enter admition number to see image : "))

from PIL import Image
dst_dir_new = ""
i = -1
for i in range(len(dst_dir)-1,0,-1):
    if(dst_dir_new[i] == '/'):
        break

for i in range(0,i+1):
    dst_dir_new = dst_dir_new + dst_dir[i]
dst_dir_new = dst_dir_new + str(ADMITION_NO)


from PIL import Image
im = Image.open(dst_dir_new) 
im.show() 