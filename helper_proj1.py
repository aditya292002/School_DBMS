# entering the file names
firstfile = "Project1_main.py"
secondfile = "proj1.py"
# opening both files in read only mode to read initial contents
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')


# closing the files
f1.close()
f2.close()

# opening first file in append mode and second file in read mode
f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')

# appending the contents of the second file to the first file
f1.write("\n")
f1.write(f2.read())

# relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)


# closing the files
f1.close()
f2.close()
