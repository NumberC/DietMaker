import requests
from pprint import pprint
import json

API_KEY="vGX5hsJJobITEeTOWfP3HbAh5FqBwif8m8NeQN5H"

# one time usage
def dataCollection(page):
    response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/list?pageSize=200&pageNumber=2&api_key=vGX5hsJJobITEeTOWfP3HbAh5FqBwif8m8NeQN5H", 
        params={
            "api_key": API_KEY,
            "pageSize":200,
            "pageNumber":page
        }
    )

    with open('data.json', 'a') as f:
        json.dump(response.json(), f)

def collectFirstTenPages():
    for i in range(10):
        dataCollection(i+1)

dataFile = open("data.json", "r")
foodData = json.load(dataFile)

def filterFoodsByNutrient(foodData, desiredNutrient, maxQtyOfNutrient):
    filteredFoodData = []
    for foodItem in foodData:
        foodNutrients = foodItem["foodNutrients"]
        for nutrient in foodNutrients:
            if nutrient["name"] == desiredNutrient and int(nutrient["amount"]) <= maxQtyOfNutrient:
                filteredFoodData.append(foodItem)
    return filteredFoodData

def filterFoodsByCalories(foodData, maxCalories):
    return filterFoodsByNutrient(foodData, "Energy", maxCalories)
def filterFoodsByFat(foodData, maxFat):
    return filterFoodsByNutrient(foodData, "Total lipid (fat)", maxFat)
def filterFoodsByCarbs(foodData, maxCarbs):
    return filterFoodsByNutrient(foodData, "Carbohydrate, by difference", maxCarbs)
def filterFoodsByProtein(foodData, maxProtein):
    return filterFoodsByNutrient(foodData, "Protein", maxProtein)

# dietary restrictons
dietaryRestrictions = {
    "peanuts" : ["nut"],
    "tree nuts" : ["nut", "almond", "cashew"],
    "nut" : ["nut", "almond", "cashew"],
    "wheat / celiac disease" : ["wheat"],
    "wheat" : ["wheat"], 
    "milk / lactose intolerant" : ["milk", "cheese", "chocolate"],
    "milk" : ["milk", "cheese", "chocolate"],
    "cheese" : ["milk", "cheese"],
    "egg" : ["egg"],
    "soy" : ["soy"],
    "fish" : ["fish"],
    "sesame" : ["sesame"],
    "vegan" : ["vegan"],  
    "vegetarian" : ["vegetarian"],
    "keto" : ["keto"],
    "low carb" : ["low carb"]
  
}

def getRedfinedRestrictionsFromRawRestrictions(rawRestrictions):
    redefinedRestrictions = []
    for restriction in rawRestrictions:
        redefinedRestrictions += dietaryRestrictions[restriction]
    
    # remove duplicate entries in the list
    return set(redefinedRestrictions)

def filterFoodsByDietaryRestriction (foodData, redefinedRestrictions):    
    filteredFoods = foodData
    for foodItem in foodData:
        for restriction in redefinedRestrictions:
            if restriction in foodItem["description"].lower():
                filteredFoods.remove(foodItem)
    return filteredFoods
            
def filterFoodByEverything(desiredCalories, desiredCarbohydrates, desiredProtein, desiredFat, rawDietaryRestrictions):
    filteredFoods = filterFoodsByCalories(foodData, desiredCalories)
    filteredFoods = filterFoodsByCarbs(filteredFoods, desiredCarbohydrates)
    filteredFoods = filterFoodsByFat(filteredFoods, desiredFat)
    filteredFoods = filterFoodsByProtein(filteredFoods, desiredProtein)
    return filteredFoods


# dietary restrictons
dietaryRestrictions = {
    "peanuts" : "nut",
    "tree nuts" : "nut",
    "nut" : "nut",
    "wheat / celiac disease" : "wheat",
    "wheat" : "wheat", 
    "milk / lactose intolerant" : "milk",
    "milk" : "milk",
    "cheese" : "milk",
    "egg" : "egg",
    "soy" : "soy",
    "fish" : "fish",
    "sesame" : "sesame"
 
}


   # ["peanuts", "tree nuts", "wheat / celiac disease", "milk / lactose intolerant", "nut", "wheat", "milk", "cheese", "egg", "soy", "fish", "sesame"]

