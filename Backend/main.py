import json
import uuid
from flask import Flask, request
import FDC
import Meals
import Calculations

def uploadMealPlanToDatabase(weeklyMealPlan):
    databaseFile = open("weeklyPlansDatabase.json", "rw")
    databaseJSON = json.load(databaseFile)

    id = uuid.uuid4()
    databaseJSON[id] = weeklyMealPlan
    json.dump(databaseJSON, databaseFile)

    return id

app = Flask(__name__)

@app.route("/getWeeklyMeal")
def getWeeklyMealPlan():
    databaseFile = open("weeklyPlansDatabase.json")
    databaseJSON = json.load(databaseFile)

    id = request.data["id"]
    return databaseJSON[id]

@app.route("/createWeeklyMeal")
def createWeeklyMealPlan():
    print(request.data)
    data = json.loads(request.data)
    height = data['height']
    weight = data['weight']
    age = data['age']
    sex = data['sex']
    dietaryRestrictions = data['dietaryRestrictions']

    print("height: " + height)
    print("weight: " + weight)
    print("age: " + age)
    print("sex: " + sex)
    print("dietary restrictions: " + dietaryRestrictions)

    desiredCalories = Calculations.numCalorie(age, sex, height, weight)
    desiredCarbohydrates = Calculations.numCarbsGrams(desiredCalories)
    desiredProtein = Calculations.numProteinGrams(weight)
    desiredFat = Calculations.numFatsGrams(desiredCalories)

    foodData = FDC.filterFoodByEverything(desiredCalories, desiredCarbohydrates, desiredProtein, desiredFat, dietaryRestrictions)
    weeklyMealPlan = Meals.getWeeklyMealPlan(foodData)

    mealPlanID = uploadMealPlanToDatabase(weeklyMealPlan)

    return mealPlanID

if __name__ == "__main__":
    app.run()