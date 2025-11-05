# ------------------------------------------------------------
# 🩺 BMI CALCULATOR APPLICATION
# A creative and user-friendly Python program
# ------------------------------------------------------------

import time
import sys
import random

# Function to print text slowly (for visual effect)
def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

# Function to calculate BMI
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# Function to analyze BMI and give health tips
def analyze_bmi(bmi):
    if bmi < 18.5:
        category = "Underweight"
        suggestion = (
            "🍽️ You need to eat more nutritious food!\n"
            "💡 Increase your protein intake and try strength training."
        )
    elif 18.5 <= bmi < 25:
        category = "Normal Weight"
        suggestion = (
            "✅ You are fit and healthy!\n"
            "🏃 Maintain a balanced diet and keep exercising regularly."
        )
    elif 25 <= bmi < 30:
        category = "Overweight"
        suggestion = (
            "⚠️ You are slightly overweight.\n"
            "💪 Include more cardio and eat lighter dinners."
        )
    else:
        category = "Obese"
        suggestion = (
            "🚨 You fall in the obese category.\n"
            "🥗 Focus on a healthy diet and consult a fitness expert."
        )
    return category, suggestion

# Function to display motivational quotes
def motivation():
    quotes = [
        "💪 Every step counts — small progress is still progress!",
        "🌟 Take care of your body. It's the only place you have to live.",
        "🔥 You don’t have to be extreme, just consistent.",
        "✨ A fit body creates a calm mind!"
    ]
    print("\nMotivational Quote of the Day:")
    slow_print(random.choice(quotes))
    print()

# Function to show app header
def show_header():
    print("=" * 55)
    print("🩺  WELCOME TO THE BMI CALCULATOR APPLICATION  🩺")
    print("=" * 55)

# Function to get user details
def get_user_data():
    print("\nPlease enter your details:")
    name = input("👤 Name: ")
    age = input("🎂 Age: ")
    gender = input("🚻 Gender (Male/Female/Other): ")
    height = float(input("📏 Height (in cm): "))
    weight = float(input("⚖️ Weight (in kg): "))

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight
    }

# Function to show results
def display_result(user, bmi, category, suggestion):
    print("\n" + "-" * 45)
    slow_print(f"👤 Name: {user['name']}")
    slow_print(f"🎂 Age: {user['age']}")
    slow_print(f"🚻 Gender: {user['gender']}")
    print("-" * 45)
    slow_print(f"📏 Height: {user['height']} cm")
    slow_print(f"⚖️ Weight: {user['weight']} kg")
    slow_print(f"🧮 Your BMI is: {bmi}")
    slow_print(f"🏷️ BMI Category: {category}")
    print("-" * 45)
    slow_print(suggestion)
    print("-" * 45)
    motivation()

# Function to show menu options
def menu():
    print("\nMAIN MENU:")
    print("1. Calculate my BMI")
    print("2. About BMI")
    print("3. Exit")

# Function to explain BMI
def about_bmi():
    print("\n📘 ABOUT BMI:")
    slow_print(
        "BMI (Body Mass Index) is a measure of body fat based on height and weight.\n"
        "It helps determine if you are underweight, normal, overweight, or obese.\n"
        "Formula: BMI = weight (kg) / [height (m)]²"
    )
    print("\nBMI CATEGORIES:")
    print("Underweight: Less than 18.5")
    print("Normal weight: 18.5 – 24.9")
    print("Overweight: 25 – 29.9")
    print("Obese: 30 or greater\n")

# Main program
def main():
    show_header()
    while True:
        menu()
        choice = input("Enter your choice (1-3 or type the option name): ").strip().lower()

        # Accept both numbers and words
        if choice in ["1", "calculate my bmi", "calculate", "bmi"]:
            print("\nLet's calculate your BMI!")
            user = get_user_data()
            bmi = calculate_bmi(user['height'], user['weight'])
            category, suggestion = analyze_bmi(bmi)
            display_result(user, bmi, category, suggestion)

        elif choice in ["2", "about bmi", "about"]:
            about_bmi()

        elif choice in ["3", "exit", "quit", "close"]:
            print("\nThank you for using the BMI Calculator App! 👋")
            break

        else:
            print("\n❌ Invalid choice! Please try again by typing 1, 2, or 3.")

# Run program
if __name__ == "__main__":
    main()
