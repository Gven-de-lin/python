#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190
#Create a list to store these monthly expenses and using that find out,

#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

expenses = [2200, 2350, 2600, 2130, 2190]
extra_money_in_Feb_to_Jan = expenses[1] - expenses [0]
total_exspenses_in_first_quarter = expenses[0]+expenses[1]+expenses[3]
third_question = 2000 in expenses
add_june = expenses.append("1980")
#correction_april =
print(extra_money_in_Feb_to_Jan, total_exspenses_in_first_quarter, third_question, expenses)

#You have a list of your favourite marvel super heros.

#Using this find out,

#1. Length of the list
#2. Add 'black panther' at the end of this list
#3. You realize that you need to add 'black panther' after 'hulk',
 #  so remove it from the list first and then add it after 'hulk'
#4. Now you don't like thor and hulk because they get angry easily :)
 #  So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
 # Do that with one line of code.
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']
length = len(heros)
print(length)
# add black panter
heros.append("black panther")
print(heros)
#delete black panter
heros.__delitem__(5)
print(heros)
#add black panther after hulk
heros.insert(3, "black panter")
print(heros)
#delete thor, hulk and add doctore strange
heros.__delitem__(1)
heros.__delitem__(1)
heros.append("doctor strange")
print(heros)
# sort heros in alphabetical order
heros.sort(key=str.lower)
print(heros)
