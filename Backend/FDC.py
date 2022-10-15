import requests
from pprint import pprint
import json
import Calculations

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

desiredCal = Calculations.numCalorie(18, "male", 60, 180)
desiredCarbs = Calculations.numCarbsGrams(desiredCal)
desiredProtein = Calculations.numProteinGrams(180)
desiredFat = Calculations.numFatsGrams(desiredCal)

def filterFoodByEverything(desiredCalories, desiredCarbohydrates, desiredProtein, desiredFat):
    filteredFoods = filterFoodsByCalories(foodData, desiredCal)
    filteredFoods = filterFoodsByCarbs(filteredFoods, desiredCarbs)
    filteredFoods = filterFoodsByFat(filteredFoods, desiredFat)
    filteredFoods = filterFoodsByProtein(filteredFoods, desiredProtein)
    return filteredFoods

foodDict = {
    "breakfast" : ["egg", "bacon", "sausage", "pancake", "waffle", "bagel", "toast", "cereal", "muffin", "milk"],
    "lunch": ["sandwich", "taco", "burger", "pizza", "salad", "wrap", "tuna", "burrito", "hot dog", "fries", "fruit"],
    "dinner": ["soup", "steak", "chicken", "roast", "porkchop", "spaghetti", "rice", ""]
}
