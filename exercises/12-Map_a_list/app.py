Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:
   value = (x*9/5)+32
   return value

result = list(map(fahrenheit_values, Celsius_values))
print(result)
