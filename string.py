#Create 3 variables to store street, city and country, now create address variable to store entire address. 
# Use two ways of creating this variable, one using + operator and the other using f-string. 
# Now Print the address in such a way that the street, city and country prints in a separate line

street = "ivanona"
city = "Kharkiv"
country = "Ukraine"
print (country + ' ' + city + ' ' + street)
print ()

#Create a variable to store the string "Earth revolves around the sun"
#Print "revolves" using slice operator
#Print "sun" using negative index

sentence = "Earth revolves around the sun"
print (sentence [6:15])
print(sentence [-3:])

#Create two variables to store how many fruits and vegetables you eat in a day. 
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. 
# Use python f string for this.

total_veggies = 3
total_fruits = 5
print (F"I eat {total_veggies} veggies and {total_fruits} fruits daily")

#I have a string variable called s='maine 200 banana khaye'. 
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. 
# Replace incorrect words in original strong with new ones and print the new string. 
# Also try to do this in one line.

s='maine 200 banana khaye'
print (s[0-6] + '10 samosa' + s[-6:])