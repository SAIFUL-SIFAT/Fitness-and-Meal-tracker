import pandas as pd

class Tracker:
    def __init__(self, data_file):
        self.data_file = data_file
        self.df = pd.read_csv(data_file)

    def add_exercise(self, date, exercise, duration):
        index = self.df[(self.df['Date'] == date) & (self.df['Exercise'] == '')].index
        if len(index) > 0:
            self.df.loc[index[0], 'Exercise'] = exercise
            self.df.loc[index[0], 'Duration'] = duration
            self.df.to_csv(self.data_file, index=False)
        else:
            print("No meal entry found for the given date to add exercise.")

    def get_workouts(self, date):
        workouts = self.df[self.df['Date'] == date][['Exercise', 'Duration']]
        return workouts
