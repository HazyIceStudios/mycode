#create lists
grocery_list = ["apple","banana","bread","spinach","beef",]
list_2 = ["muffin","brussel sprouts","wheat","brocoli",]

#print list
print(grocery_list)

#get length
print(len(grocery_list))

#index
print(grocery_list[0])

#count backwards
print(grocery_list[-1])

#print both lists
print(grocery_list + list_2)

#combine lists in new variable
new_list=grocery_list + list_2
print(new_list)

#combine in original list. creates a list within a list. basically an array with an array.
#grocery_list.append(list_2)
print(grocery_list)

#combine list items in original list
#grocery_list.extend(list_2)
grocery_list

#print range of array
print(grocery_list[1:3])

#print from index to end of array
print(grocery_list[1:])

#print from begining to index of array
print(grocery_list[:2])
