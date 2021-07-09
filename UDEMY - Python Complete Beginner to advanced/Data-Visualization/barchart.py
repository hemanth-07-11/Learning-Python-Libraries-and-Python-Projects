import matplotlib.pyplot as plt
import matplotlib.axes as axes
import numpy as np


col_count = 3
bar_width = .15

australia_score = (510, 494, 503)
canada_score = (523, 516, 527)
us_score = (496, 470, 497)
uk_score = (509, 492, 498)

index = np.arange(col_count)


a1 = plt.bar(index, australia_score, bar_width, label='Australia', color=(0/255, 26/255, 102/255, 60/100))
c1 = plt.bar(index + 0.2, canada_score, bar_width, label='Canada', color=(128/255, 0/255, 0/255, 60/100))
us1 = plt.bar(index + 0.4, us_score, bar_width, label='United States', color=(236/255, 157/255, 3/255, 60/100))
uk1 = plt.bar(index + 0.6, uk_score, bar_width, label='United Kingdom', color=(98/255, 1/255, 180/255, 60/100))

def create_labels(data):
    for item in data:
        height = item.get_height()

        plt.text(item.get_x() + item.get_width() / 2., height * 1.05,
                 '%d' % int(height),
                 ha = 'center', va='bottom')

create_labels(a1)
create_labels(c1)
create_labels(us1)
create_labels(uk1)


plt.ylabel('Mean Score in PISA 2015')
plt.xlabel('Subjects')
plt.title('Test Scores by Country')


plt.xticks(index + .6/2, ('Science', 'Math', 'Reading'))

plt.legend(frameon=False, bbox_to_anchor=(1, 1), loc=2)

plt.grid(True)


plt.show()


