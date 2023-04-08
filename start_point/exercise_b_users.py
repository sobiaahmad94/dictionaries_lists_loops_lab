users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      },
      {
        "favourite_superhero": "Spider-Man",
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

# users is a dict, Jonathan is a dict inside the users dict
# key/value pairs
# twitter is the key, johnnyt is the value, I need to grab the key to get the value

# users dict --> Jonathan dict --> "twitter" is the key that contains the value "jonnyt
# store "jonny t" in twitter_username variable
twitter_username = users["Jonathan"]["twitter"]
print(twitter_username) 

# 2. Get Erik's hometown
# users dict --> Erik dict --> "home_town" key contains the value "Linlithgow"
# store hometown in eriks_hometown variable
eriks_home_town = (users["Erik"]["home_town"])
print(eriks_home_town) 

# 3. Get the list of Erik's lottery numbers
# users dict --> Erik dict --> key "lottery_numbers" contains the values
# store lottery numbers in eriks_lottery variable
eriks_lottery = (users["Erik"]["lottery_numbers"])
print(eriks_lottery)

# 4. Get the species of Avril's pet Monty
# users dict --> Avril dict --> pets list --> index 1 is "species key" within species dict
# store value in a avrils_pet_montys_species
# pets list - "name" is index 0, species is index 1
avrils_pet_montys_species = users["Avril"]["pets"][0]["species"]
print(avrils_pet_montys_species)

# I added another item into the pets list just to test things
# Outputting Avril's favourite superhero
# avrils_pet_montys_species = users["Avril"]["pets"][1]["favourite_superhero"]
# print(avrils_pet_montys_species)


# 5. Get the smallest of Erik's lottery numbers
# users dict --> Erik dict --> "lottery_numbers" key to get list
# --> now I've got the list  then store lottery numbers list in eriks_lottery_numbers variable
# create a variable called eriks_smallest_lottery_number and use min() on it
# print smallest number

eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
eriks_smallest_lottery_number = (min(eriks_lottery_numbers))
print(eriks_smallest_lottery_number)

# 6. Return an list of Avril's lottery numbers that are even
# users dict --> Avril dict --> "lottery_numbers" key --> list that contains Avril's lottery numbers
# store Avril's lottery numbers in avrils_lottery_numbers var
# create an empty list called avrils_even_lottery_numbers
# do a for loop that goes through each number in avril_lottery_numbers
# search up the formula to get an even number - if number % 2 == 0:
# % (modulus) refers to remainder, if a number has no remainder it'll be equal so it'll be an even number
# modulus operator gives the remainder
# use avrils_even_lottery_numbers to store the numbers 
# append the numbers to avrils_even_lottery_numbers

avrils_lottery_numbers = users["Avril"]["lottery_numbers"]
avrils_even_lottery_numbers = []

for number in avrils_lottery_numbers:
    if number % 2 == 0:
        avrils_even_lottery_numbers.append(number)
        
print(avrils_even_lottery_numbers)

# My example

# How to get even numbers out of a list

pokemon_pokedex_numbers = [10, 4, 25, 7, 96, 39, 26, 52] 
even_pokedex_numbers = []

for pokedex_number in pokemon_pokedex_numbers:
    if pokedex_number % 2 == 0:
        even_pokedex_numbers.append(pokedex_number)

print(even_pokedex_numbers)
    

# How to get odd numbers out of a list

pokemon_pokedex_numbers = [10, 4, 25, 7, 96, 39, 26, 52] 
even_pokedex_numbers = []

for pokedex_number in pokemon_pokedex_numbers:
    if pokedex_number % 2 != 0: # != means NOT EQUAL so would be the opposite of even
        even_pokedex_numbers.append(pokedex_number)

print(even_pokedex_numbers)


# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# users dict --> Erik dict --> "lottery_numbers" 
# store lottery numbers in eriks_lottery_numbers (already created)
# append 7 to "lottery_numbers" key
eriks_lottery_numbers = users["Erik"]["lottery_numbers"]

users["Erik"]["lottery_numbers"].append(7)
print(eriks_lottery_numbers)

# 8. Change Erik's hometown to Edinburgh
# users dict --> Erik dict --> "home_town" key has the value Linlithgow
# create a variable called eriks_new_home_town 
# change the hometown within "home_town" key to Ednburgh

eriks_new_home = users["Erik"]["home_town"] = "Edinburgh"
print(eriks_new_home)
# print(users["Erik"])

# 9. Add a pet dog to Erik called "fluffy"
# users dict --> Erik dict --> "pets" key --> list
# append new pet "name" and "species" key value pairs

print(users["Erik"]["pets"].append({"name" : "fluffy", "species" : "dog"})
)
#* I want some help with this

# 10. Add another person to the users dictionary

users["Halsey"] = {
    "real_name" : "Ashley Nicolette Frangipane",
    "year_of_birth" : 1994,
    "full_date_of_birth" : "29/09/1994",
    "twitter" : "halsey",
    "home_town" : "Edison, New Jersey, USA",
    "instruments" : ["vocals", "violin", 
"viola", "cello", "guitar"]   
}
print(users)
