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
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# users is a dict, Jonathan is a dict inside the users dict
# key/value pairs
# twitter is the key, johnnyt is the value, I need to grab the key to get the value
twitter_username = (users["Jonathan"]["twitter"])
print(twitter_username) 

# 2. Get Erik's hometown
eriks_home_town = (users["Erik"]["home_town"])
print(eriks_home_town) 

# 3. Get the list of Erik's lottery numbers
eriks_lottery = (users["Erik"]["lottery_numbers"])
print(eriks_lottery)

# 4. Get the species of Avril's pet Monty
# avrils_pet_species = (users["Avril"]["pets"[2]]) # I'm stuck on this 
# print(avrils_pet_species) 

# 5. Get the smallest of Erik's lottery numbers
smallest_eriks_lottery = (users["Erik"]str(["lottery_numbers"].split())) # I'm stuck on this 
print(smallest_eriks_lottery)
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary
