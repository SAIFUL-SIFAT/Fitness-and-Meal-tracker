from meal_planner import MealPlanner
from tracker import Tracker

def main():
    data_file = 'data/data.csv'
    meal_planner = MealPlanner(data_file)
    tracker = Tracker(data_file)

    # Example usage
    print("Fitness Tracker with Meal Planning")
    
    while True:
        print("\nOptions: ")
        print("1. Add Meal")
        print("2. Get Meals")
        print("3. Add Exercise")
        print("4. Get Workouts")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            meal = input("Enter meal name: ")
            calories = input("Enter calories: ")
            meal_planner.add_meal(date, meal, calories)
            print("Meal added successfully.")
        
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            meals = meal_planner.get_meals(date)
            print(meals)
        
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            exercise = input("Enter exercise name: ")
            duration = input("Enter duration (minutes): ")
            tracker.add_exercise(date, exercise, duration)
            print("Exercise added successfully.")
        
        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD): ")
            workouts = tracker.get_workouts(date)
            print(workouts)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
