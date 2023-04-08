united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
# united_kingdom list --> index 1 is Wales --> change Swansea to Cardiff
# ...[1] "capital" is the key that has the value that needs to be changed
united_kingdom[1]["capital"] = "Cardiff"
print(united_kingdom)

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
# get the existing dict, which is united_kingdom list
# add the dict {"name" : "Northern Ireland", "population" : 1811000, "capital" : "Belfast"}
united_kingdom.append({
    "name" : "Northern Ireland",
    "population" : 1811000,
    "capital" : "Belfast"   
})
print(united_kingdom)


# 3. Use a loop to print the names of all the countries in the UK.
# create the loop - for country in united_kingdom
# the key "name" will output the names of each country 
# 1st country loop - Scotland
# 2nd country loop - Wales
# 3rd country loop - England
# 4th country loop - Northern Ireland


for country in united_kingdom:
    print(country["name"])

# 4. Use a loop to find the total population of the UK.
# create the loop - for country in united_kingdom
# the key "population" will output the population of each country 

total_uk_population = 0

for country in united_kingdom:
    total_uk_population += country["population"]
  
print(total_uk_population)

# My examples

# Adding all of the numbers in a list together

pokemon_pokedex = [
    {"name" : "Pikachu", "pokedex_number" : 25, "energy_card" : "lightning"},
    {"name" : "Charmander", "pokedex_number" : 4, "energy_card" : "fire"},
    {"name" : "Squirtle", "pokedex_number" : 7, "energy_card" : "water"},
    {"name" : "Bulbasaur", "pokedex_number" : 1, "energy_card" : "grass" },
    {"name" : "Meowth", "pokedex_number": 52, "energy_card" : "darkness"}
]
    
# Adding up all of the pokedex_numbers using a loop
total_pokedex_nums = 0

for pokedex_num in pokemon_pokedex:
    total_pokedex_nums += pokedex_num["pokedex_number"]

print(total_pokedex_nums)
    



