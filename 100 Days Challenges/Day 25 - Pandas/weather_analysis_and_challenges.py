# Weather analysis
import pandas as pd
import csv

# first challenge: create a list from teh weather data csv

with open('100 Days Challenges\\Day 25 - Pandas\\weather_data.csv', 'r',) as data_1:
    data_1 = data_1.readlines()
    for i, y in enumerate(data_1):
        data_1[i] = y.rstrip()

# with the built-in csv package

with open('100 Days Challenges\\Day 25 - Pandas\\weather_data.csv', 'r',) as data_2:
    data = csv.reader(data_2)
    print(data) # the reader method from the library creates an iterable object
    temperature = []
    for i, row in enumerate(data):
        temperature.append(row)
        if i > 0:
            row[1] = int(row[1])
    print(temperature)

# The key take away from the the blocks of code above is to show how much better and convenient it is to just use Pandas
# Using pandas below did all of the above in just one simple line of code, with even better output

weather_df = pd.read_csv('100 Days Challenges\\Day 25 - Pandas\\weather_data.csv')
print(type(weather_df)) # Data Frame Object
print(weather_df)
print(type(weather_df['temp'])) # Series Object.
print(weather_df['temp']) # Pandas already identify the column is an integer column and does the conversion itself. And we can use the column name as the index.

weather_dict = weather_df.to_dict()
print(weather_dict)
temp_list = weather_df['temp'].to_list()

# Challenge: get the average temperature
average_temp = sum(temp_list) / len(temp_list)

# With pandas
average_temp_2 = weather_df['temp'].mean()

# Challenge: Max Value
max_temp = weather_df['temp'].max()
print(max_temp)

# Getting to the rows
monday_row = weather_df[weather_df['day'] == 'Monday']
print(monday_row)

# Challenge: Get the row with the max temp
max_temp = weather_df[weather_df['temp'] == weather_df['temp'].max()]
print(max_temp)

# Challenge: Get Monday's temp but convert it to Fahrenheit
temp_fahrenheit = (monday_row['temp'] * (9/5) + 32)
print(temp_fahrenheit)

# creating a data frame from scratch
random_dict = {
    'students': ['Amy', 'James', 'Dick'],
    'scores': [76, 56, 65]
}

radnom_df = pd.DataFrame(random_dict)
radnom_df.to_csv('100 Days Challenges\\Day 25 - Pandas\\random.csv')
print(radnom_df)
