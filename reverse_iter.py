class ReverseIter:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= 0:
            value = self.data[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration

list = input("Enter the numbers in the list with a space: ")
numbers = list.split()
numbers = [int(num) for num in numbers]

reverse_iterator = ReverseIter(numbers)

print("Iterating over the list in the reverse order: ")
for item in reverse_iterator:
    print(item)