import matplotlib.pyplot as plt
import pandas as pd


raw_data = {'names': ['Hems', 'Sharms', 'Raina', 'Kohli', 'Dhoni'],
            'jan_ir': [124, 153, 114, 132, 312],
            'feb_ir': [132, 142, 152, 129, 114],
            'mar_ir': [114, 132, 121, 142, 13]}

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'mar_ir'])

df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['mar_ir']

color = [(0/255, 26/255, 102/255, 80/100), (128/255, 0/255, 0/255, 80/100), (18/255, 223/255, 177/255, 80/100),
          (98/255, 1/255, 180/255, 80/100), (236/255, 157/255, 3/255, 80/100)]

plt.pie(df['total_ir'],
        labels=df['names'],
        colors=color,
        autopct='%1.1f%%')

plt.axis('equal')

plt.show()

print(df)
