class SubArray:
    def __init__(self, arr):

        self.array = arr.split(",")
        print(("the input array is:", self.array))

    def solve_sub_array(self):
        rear = [int(self.array[0])] * len(self.array)
        sum_value = [int(self.array[0])] * len(self.array)
        for i in range(1, len(self.array)):
            sum_value[i] = max(
                int(self.array[i]) + sum_value[i - 1], int(self.array[i])
            )
            rear[i] = max(sum_value[i], rear[i - 1])
        return rear[len(self.array) - 1]


if __name__ == "__main__":
    whole_array = input("enter numbers:")
    array = SubArray(whole_array)
    re = array.solve_sub_array()
    print(("the results is:", re))
