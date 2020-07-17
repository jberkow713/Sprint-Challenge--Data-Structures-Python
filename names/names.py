import time

start_time = time.time()



q = open('names_1.txt', 'r')

names_1 = q.read().split("\n")  # List containing 10000 names

q.close()



f = open('names_2.txt', 'r')

names_2 = f.read().split("\n")  # List containing 10000 names

f.close()

# so names_1 and names_2 return all names in their respective lists

#duplicates = set(names_1).intersection(names_2)



duplicates = []  # Return the list of duplicates in this data structure


#Runtime Complexity of running through nested for loops: is 
# O (n^2)
# I think it becomes O nlogn after changes

# Replace the nested for loops below with your improvements



#just change loop to search through only one list and compare, instead
# of searching through both lists first and then comparing

# combo = [x for x in names_1 if x in names_2]
for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)

#duplicates.append(combo)
#print(duplicates)
#print(f"There were {len(combo)}" + " " 'duplicates')


#for name_1 in names_1:

#    for name_2 in names_2:

#        if name_1 == name_2:

#            duplicates.append(name_1)


end_time = time.time()
end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

''''
trying to get the name file to recognize that I have updated it, is quite
a pain
, so why Python, why must you be so annoying????!???
'''
