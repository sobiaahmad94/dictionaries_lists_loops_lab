stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list

stops.append("Edinburgh Waverley")
# print(stops)

#2. Add "Glasgow Queen St" to the start of the list

stops.insert(0, "Glasgow Queen St")
# stops[0] = "Glasgow Queen St" - I think this line should could also work
# print(stops)

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")

# 0 Glasgow Queen St
# 1- Croy
# 2 - Cumbernauld
# 3 - Falkirk High
# 4 - Linlithgow - Polmont needs to go here so it's before Linlithgow, then index will move as there's another item in list
# 5 - Livingston...

stops.insert(4, "Polmont")
# print(stops)

#4. Print out the index position of "Linlithgow"

# 0 Glasgow Queen St
# 1- Croy
# 2 - Cumbernauld
# 3 - Falkirk High
# 4 - Polmont
# 5 - Linlithgow - Polmont needs to go here so it's before Linlithgow, then index will move as there's another item in list
# 6- Livingston...
# print(stops[5])

#5. Remove "Livingston" from the list using its name

# for stop in stops:
#     # print(stop)
#     if stop == "Livingston":
#         stops.remove(stop)

# print(stops)

# Livingston is index 6

#6. Delete "Cumbernauld" from the list by index
# print(stops)
# Cumbernauld is index 2
# print(stops.pop(2))
# print(stops)


#7. Print the number of stops there are in the list
# print(len(stops))

#8. Sort the list alphabetically
# print(sorted(stops))

#9. Reverse the positions of the stops in the list
print(stops)

for stop in stops:
    print(stop)
    
for stop in reversed(range(9)):
    print(stop)

    # How do you combine these two things? I'm not too sure.


#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)


