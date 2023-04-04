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
print(stops[5])

#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop


