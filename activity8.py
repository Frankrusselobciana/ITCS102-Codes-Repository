hobbies = "" #blank string 
favorite = ""

h = input ("what are your hobbies -->")
hobbies += h + ", "

h = input("what else --> " ) 
hobbies += h + ", "

h = input ("what else --> ") 
hobbies += h + ", "

f = input ("what's your favorite food --> ") 
favorite += f + ", "

f = input ("how about color? --> " ) 
favorite += f+ ", "

f = input("to do? --> ") 
favorite += f + ", "

print ("So, my hobbies are", hobbies) 
print("And my favorite color, food, and to do are ", favorite)