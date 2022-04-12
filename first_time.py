
#RUN THE FOLLOWING CODE TO 
#CREATE DATABASE AND TABLE
#AND TAKE INPUT OF DESTINATION PATH OF THE IMAGES

#In linux you can open mysql using this 

import mysql.connector as sq
var1=sq.connect(host="localhost",user="root",passwd="Adikes209.")
cursor1=var1.cursor()
cursor1.execute("create database project1;")

var1.close()
var2=sq.connect(host="localhost",user="root",passwd="Adikes209.",database="project1")
cursor2=var2.cursor()
cursor2.execute("create table student(admition_no int(5) primary key,sname varchar(30),dob  date,doa date,class1   varchar(5),section varchar(1),guardian_n varchar(30),mobile_no   varchar(15),aadhar_no varchar(15));")
var2.commit()
var2.close()	

#Take a path to the folder user wants to store all the images
dst_dir = input("Enter the path to the folder you want to store all your images")
f = open("Project1_main.py","w")
f.write("dst_dir = '" + str(dst_dir)+"'")
#you got the destination folder 
#using file handling make change to the destination path variable in the main file