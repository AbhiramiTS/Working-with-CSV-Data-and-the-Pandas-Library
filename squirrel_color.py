
# import csv
#
# with open('weather_data.csv') as file:
#     data = list(csv.reader(file))
#     for i in range(1, len(data)):
#         data[i][1] = int(data[i][1])
#
# print(data)

# import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data[data.temp == data.temp.max()])
# print(data[data.temp == data.temp.max()].condition)


import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color = set(list(data['Primary Fur Color']))
squirrel_count = []

for color in fur_color:
    squirrel_count.append((data['Primary Fur Color'] == color).sum())
    # print(data[data['Primary Fur Color'] == color])

fur_color = list(fur_color)
data_dict = {
    "fur color": fur_color,
    "Count": squirrel_count
}
# print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')