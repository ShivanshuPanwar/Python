# we cannot combine strings and numbers like this
'''
age = 36
txt = "My name is John, I am " + age
print(txt) 

'''


# But we can combine strings and numbers by using the format() method!

AGE = 28
TXT = "My Name is Parth, I am {}"
print(TXT.format(AGE))


quantity = 5
itemno = 700
price = 120.55
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


Quantity = 5
Itemno = 700
Price = 120.55
Myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(Myorder.format(Quantity, Itemno, Price))
