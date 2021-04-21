"""
Created on Wed Apr 21 2021 20:05

@author: Sanjeev
"""

import json
import pandas as pd
from pandas.core.indexes import category

class BmiCalculator:
    def __init__(self):
        self.bmi = []
        self.overweightCount = 0
        # Opening the input JSON file
        f = open("input.json")

        # loading input json as a dictionary
        self.data = json.load(f)

        # print(self.data)

        # Closing file
        f.close()

    def calculate(self):
        try:
            # create dataframe from json data
            df = pd.DataFrame.from_dict(self.data)
            # for classification
            category = []

            # rows generator
            for index, row in df.iterrows():
                # BMI Formula
                tempBmi = 50*row['WeightKg']/row['HeightCm']

                if tempBmi<30 and tempBmi>=25:
                    self.overweightCount += 1

                # Classification
                tempCategory = "Underweight" if tempBmi<18.5 \
                                else "Normal weight" if tempBmi<25 \
                                else "Overweight" if tempBmi<30 \
                                else "Moderately obese" if tempBmi<35 \
                                else "Severely obese" if tempBmi<40 \
                                else "Very severely obese"
                self.bmi.append(tempBmi)
                category.append(tempCategory)

            # adding calculated result to dataframe
            df['BMI'] = self.bmi
            df['Category'] = category

            # printing tabular report
            print(df)

            # print overweight count
            print("\n Number of overweight people is: {}\n".format(self.overweightCount))

        except Exception as e:
            print('Exception occurred during BMI calculation: ' + str(e))


if __name__ == '__main__':
    obj = BmiCalculator()
    obj.calculate()
