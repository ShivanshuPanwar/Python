myList = ["raj","rahul","palak"]
print(myList)

myList1 = ["sakshi","goyal","21"]
print(myList1)


myList2 = ["parth","deepa","delhi"]
print(len(myList2))


myList3 = ["arvind","ankit","pawan","manoj"]
print(myList3[1:3])

myList4 = ["a","b","c","d"]
print(myList4[2])


myList5 = ["wt","coa","ai","se","cn"]
myList5[1] = "cc"
print(myList5)


# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

myList6 = ["hr","mr","vr","br"]
myList6.insert(2,"vp")
print(myList6)


# To add an item to the end of the list, use the append() method:

myList7 = ["cr","spc"]
myList7.append("crpc")
print(myList7)


#  To append elements from another list to the current list, use the extend() method

myList8 = ["py","java"]
myList9 = ["c","c#"]
myList8.extend(myList9)
print(myList8)


# The remove() method removes the specified item

myList10 = ["mayank","mayanka","weds"]
myList10.remove("mayanka")
print(myList10)


# The pop() method removes the specified index

myList11 = ["1","2","3"]
myList11.pop(1)
print(myList11)


# sort() method that will sort the list alphanumerically, ascending, by default

myList12 = [15,20,14,27,24]
myList12.sort()
print(myList12)


# To sort descending, use the keyword argument reverse = True

myList13 = [10,15,13,27,23]
myList13.sort(reverse=True)
print(myList13)


myList14 = ["1","7","9"]
thisList14 = myList14.copy()
print(thisList14)

myList15 = [1,8,9]
thisList = list(myList15)
print(thisList)