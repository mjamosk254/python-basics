fruits=["apple","banana","mango"]
print(fruits)

#.append-adds an item to the end of the list
fruits.append("kiwi")
print(fruits)

#indexing-accesing items or elements of a list(starts from 0)
print(fruits[0])
print(fruits[-1])

#.insert-adds an element at specific position
fruits.insert(1,"orange")
print(fruits)

#.remove-removes a specific item by value
fruits.remove("mango")
print(fruits)

#.pop-removes the last item
fruits.pop()
print(fruits)

#.reverse-reverses the order of the list
fruits.reverse()
print(fruits)

marks=[50,45,70,36,71]
#.sort-sorts the in ascending order(smallest-largest)
marks.sort()
print(marks)