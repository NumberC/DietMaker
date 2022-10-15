import random
import FDC
import Calculations

# common food items for breakfast, lunch, and dinner
foodDict = {
    "breakfast" : ["egg", "bacon", "sausage", "pancake", "waffle", "bagel", "toast", "cereal", "muffin", "milk"],
    "lunch": ["sandwich", "taco", "burger", "pizza", "salad", "wrap", "tuna", "burrito", "hot dog", "fries", "fruit"],
    "dinner": ["soup", "steak", "chicken", "roast", "porkchop", "spaghetti", "rice", ""]
}

def getARandomFoodForTimeOfDay(foodData, listOfFood, exclusions):
    # we use random index to begin from for variation
    startIndex = random.randint(0, len(foodData)/2)

    for food in foodData[startIndex:]:
        if food not in exclusions:
            for timeOfDayFood in listOfFood:
                if timeOfDayFood in food["description"].lower():
                    return food
def getBreakfastFoods(foodData):
    firstBreakfastFood = getARandomFoodForTimeOfDay(foodData, foodDict["breakfast"], [])
    secondBreakfastFood = getARandomFoodForTimeOfDay(foodData, foodDict["breakfast"], [firstBreakfastFood])
    return [firstBreakfastFood, secondBreakfastFood]
def getLunchFoods(foodData):
    firstLunchFood = getARandomFoodForTimeOfDay(foodData, foodDict["lunch"], [])
    secondLunchFood = getARandomFoodForTimeOfDay(foodData, foodDict["lunch"], [firstLunchFood])
    return [firstLunchFood, secondLunchFood]
def getDinnerFoods(foodData):
    firstDinnerFood = getARandomFoodForTimeOfDay(foodData, foodDict["dinner"], [])
    secondDinnerFood = getARandomFoodForTimeOfDay(foodData, foodDict["dinner"], [firstDinnerFood])
    return [firstDinnerFood, secondDinnerFood]

# TESTING
desiredCal = Calculations.numCalorie(18, "male", 60, 180)
desiredCarbs = Calculations.numCarbsGrams(desiredCal)
desiredProtein = Calculations.numProteinGrams(180)
desiredFat = Calculations.numFatsGrams(desiredCal)

foodData = FDC.filterFoodByEverything(desiredCal, desiredCarbs, desiredProtein, desiredFat)

print(getBreakfastFoods(foodData))
print(getLunchFoods(foodData))
print(getDinnerFoods(foodData))

def getWeeklyMealPlan(foodData):
    mealsPerDay = []
    for i in range(7):
        mealForDay = []
        mealForDay[0] = getBreakfastFoods(foodData)
        mealForDay[1] = getLunchFoods(foodData)
        mealForDay[2] = getDinnerFoods(foodData)
        mealsPerDay.append(mealForDay)