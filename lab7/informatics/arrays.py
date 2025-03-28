a=int(input("Enter a number: "))
for i in range(a):
    print(i,end=" ")
    
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)

cars = ["Ford", "Volvo", "BMW"]
x=len(cars)
print(x)

cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.clear()
print(cars)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)

def ss(s):
    return len(s)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(key=ss)

def ss(s):
    return len(s)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True, key=ss)

def ss(s):
    return s['year']
cars = [{'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=ss)