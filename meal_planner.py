import pandas as pd

class MealPlanner:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = pd.read_csv(data_file)

    def add_meal(self, date, meal, calories):
        new_entry = pd.DataFrame([[date, meal, calories, '', '']], columns=['Date', 'Meal', 'Calories', 'Exercise', 'Duration'])
        self.df = pd.concat([self.df, new_entry], ignore_index=True)
        self.df.to_csv(self.data_file, index=False)

    def get_meals(self, date):
        meals = self.df[self.df['Date'] == date]
        return meals

    def update_meal(self, index, meal, calories):
        self.df.loc[index, 'Meal'] = meal
        self.df.loc[index, 'Calories'] = calories
        self.df.to_csv(self.data_file, index=False)
