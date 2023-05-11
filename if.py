#1.Using following list of cities per country,
#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]
#1.1 Write a program that asks user to enter a city name and it should tell which country the city belongs to
#1.2 Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but if 
# I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("Enter a name of city: ")
if city in india:
    print("india")
elif city in pakistan:
    print("pakistan")
elif city in bangladesh:
    print("bangladesh")
else: print("I don't know")

city1=input("Enter a first name city: ")
city2=input("Enter a second name city: ")

if city1 in india and city2 in india:
    print("Both cities are in india")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in bangladesh")
else: print("They don't belong to same country")

#2.Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#2.1 Ask user to enter his fasting sugar level
#2.2 If it is below 80 to 100 range then print that sugar is low
#2.3 If it is above 100 then print that it is high otherwise print that it is normal

level_sugar=input("Enter your level sugar: ")
level_sugar=int(level_sugar)
if level_sugar>80 and level_sugar<100:
    print("normal")
elif level_sugar>100:
    print("high")
else: print("low")