import math


def inToMeters(inches):
    return inches*0.0254

def lbToKg(pounds):
    return pounds/2.205

def calcBMI(pounds, inches):
    Kgs = lbToKg(pounds)
    Meters = inToMeters(inches)
    BMI = Kgs/(math.pow(Meters, 2))
    return BMI

def BMIcheck(BMI):
    if (BMI < 18.5):
        return "Underweight"
    elif (BMI < 25):
        return "Normal"
    elif (BMI < 30):
        return "Overweight"
    elif (BMI < 40):
        return "Obese"
    else:
        return "Morbidly Obese"


def numCalorie(age, gender, height, weight): # Using the Henry-Benedict's Formula
    numCal = 0
    if (gender == "Male"):
        numCal = 66.47 + 6.24*weight + 12.7*height - 6.755*age
    elif (gender == "Female"):
        numCal = 655.1 + 4.35*weight + 4.7*height - 6.8*age
    return numCal


def numProteinGrams(weight):
    return 0.8*(lbToKg(weight))

def numCarbsGrams(numCal):
    return 0.55*(numCal)

def numFatsGrams(numCal):
    return 0.35*(numCal)






nuts = ["peanut", "almond", "walnut", "cashew"]
dairyProducts = ["cheese", "butter", "milk", "yogurt"]
fish = ["salmon", "tuna", "cod", "fish"]
gluten = ["gluten"]
wheats = ["wheat"]
shellFish = ["crab", "lobster", "prawn", "shrimp", "clam"]


allergies = [nuts, dairyProducts, fish, gluten, wheats, shellFish]