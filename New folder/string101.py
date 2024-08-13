# array indexes (first : last) it could be called ( start at : end on);


print("I\'ll be Ignored")
print("Hello "+"ME")
str3 = "Hello World"

print("1st 3",str3[0:3]) #from the str variable we get hel output : 1st 3 Hel
print("Every Other", str3[0:-1:3]) # str3 its starts with H its from 0 : So the side of it gives iteration to the indexes value of string
                                   # the -1 gets the last index of string so if str3[0:3] L then iterate to str3[0:6] until the last index of string
str3 = str3.replace("Hello", "Goodbye") # logically it replace the string value
print(str3)

str3 = str3[:8] + "y" + str3[9:] # end it after space then replace the index 8 with Y and start with at index 9
print(str3)

print("you" in str3) # checks if the word you is in str3
print("you" not in str3) # checks if the word you is not in str3
print("you index", str3.find("you"))
print("    Hello   ".strip())

print("".join(["Some","Words"]))

print("A String".split(" "))   

int1 = int2 = 5
print(f'{int1} + {int2} = {int1 + int2} ')

print("A String".lower())
print("A String".upper())

print("A String 123".isalnum()) # checks if all Numbers
print("ASTRING".isalpha())  #Checks if only lettrs no SPACES or etc
print("A STRING".isdigit()) #Checks if only digits