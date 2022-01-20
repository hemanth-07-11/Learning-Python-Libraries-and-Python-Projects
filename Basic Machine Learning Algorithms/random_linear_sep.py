import random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

current_datetime = datetime.now()
second = current_datetime.second
random.seed(second)

total_number = 200
train_test_rate = 0.8

width = 1
height = 1

lineA = random.uniform(-5, 5)
lineB = random.uniform(-1, 1)

learningRate = 0.0005

def ActivationFunction(x):
	if x >= 0:
		return 1
	return -1

class Perceptron:
	def __init__(self):
		weights = []
		for i in range(3):
			weights.append(random.uniform(-1, 1))

		self.weights = weights

	def guess(self, inputs):
		sum = 0
		for i in range(3):
			sum += inputs[i] * self.weights[i]

		self.output = ActivationFunction(sum)

	def train(self, inputs, target):
		error = target - self.output

		for i in range(3):
			self.weights[i] += error * inputs[i] * learningRate

class Point:
	def __init__(self):
		self.x = random.uniform(-width, width)
		self.y = random.uniform(-height, height)
		self.bias = 1

		if self.y >= LineFunction(self.x):
			self.label = 1
		else:
			self.label = -1

def GenerateData():	
	points = []

	for i in range(total_number):
		points.append(Point())

	return points

def Train(points):
	train_data = points[0:int(total_number*train_test_rate)]
	for point in train_data:
		p.guess([point.x, point.y, point.bias])

		p.train([point.x, point.y, point.bias], point.label)

def Guess(points):
	test_data = points[int(total_number*train_test_rate):total_number]
	wrong = 0
	for point in test_data:
		p.guess([point.x, point.y, point.bias])

		color = 'green'

		if p.output != point.label:
			wrong += 1
			color = 'red'

		plt.plot(point.x, point.y, 'o', color=color)
	return wrong

def LineFunction(x):
	return lineA * x + lineB

def PerceptronFunction(x):
	w0 = p.weights[0]
	w1 = p.weights[1]
	w2 = p.weights[2]

	return -(w0/w1) * x - (w2/w1)

p = Perceptron()

points = GenerateData()

def animation(i):
	if (i != 0):
		plt.gcf().clear()
		wrong_percentage = Guess(points)/(total_number*(1-train_test_rate))
		right_percentage = 1-wrong_percentage

		acc = round(right_percentage*100, 2)

		plt.axline((-width, LineFunction(-width)), (width, LineFunction(width)), color="black")
		axes = plt.gca()
		axes.set_xlim([-width, width])
		axes.set_ylim([-height, height])
		plt.title("Accuracy: " + str(acc) + "%")
		plt.show()

		plt.axline((-width, PerceptronFunction(-width)), (width, PerceptronFunction(width)), color="orange")

		Train(points)

animation = FuncAnimation(plt.gcf(), animation, interval=500)
plt.show()