# list methoths
l=[2,3,4,5,6,"apple",True,4.5,None] #note:-lists are mutable in python
l.append(2) #append is a method in python that is use to add a number in a list at last
print(l)
l1=[15,26,5,7,8,10,5]
# l1.sort();# it is use to sort the list data into assending order
# print(l1)
# l1.sort(reverse=True)# it is use to sort the list data into desending order
# print(l1)
l1.reverse() #it reverse the the whole list
print(l1)
print(l1.index(5))#it gives the index number of the given value . note:-it given the index of first occurance value
print(l1.count(5))#it count the same value that parsent inside a loop

# m=l1
# m[0]=0
# print(m)
# print(l1)
# note:- if we assign the all list to a varible and make a new varible ..and when we change the value of the new varible so it changes the origional list value because in python varible refrence the list l1 values
#to solve this issue we use the copy() method
m=l1.copy()
m[0]=0
print(m)
print(l1)

l1.insert(1,899)# it is use to insert a new value on specific index number here(index,newvalue)
print(l1)

l.extend(l1) #it means l1 ko kholo or l1 k saare elements ko l k last mein jod do.
print(l) 
k=[2,3,4,5,6]
n=k+l1 #it is use to concatinate to list
print(n)


# touple:-tuple are the order collection of multiple type of value. it value saprted by comma and and enclosed by breakets(). tuples are inmutable
tup=(1) #so it is a vraible
print(type(tup),tup)
tup=(1,)# it is a tuple
print(type(tup),tup)
tup=(2,34,5,56,76,87)
if 56 in tup:
    print("yes 56 persent in tup")


