import pandas as pd

data = pd.read_csv('find_s.csv')
h = ['0'] * 6
for i in range(data.shape[0]):

    training_data = [data.sky[i], data.air_temp[i], data.humidity[i], data.wind[i], data.water[i], data.forecast[i]]
    if data.enjoy_sport[i] == 'yes':
        for j in range(data.shape[1] - 1):
            if h[j] == '0':
                h[j] = training_data[j]
            if h[j] != training_data[j]:
                h[j] = '?'

print('Most Specific', h)
