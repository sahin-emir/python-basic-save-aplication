# In this application, we save the entered name and surname information to the file with the file open command.

print("name  ")
name=str(input("===  "))
print("surname")
surname=str(input("===  "))

file = open("newfile.csv","a",encoding='utf-8')
file.write(f'{name}  {surname} ')
file.write("\n")

file.close()


