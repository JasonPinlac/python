# Dynamically typed language

# Type Hinting
def addNumbers(a: int, b: int) -> int :
    return a + b

# res = addNumbers(5,'world')
res = addNumbers(1, 2)
print(res)

'''this is a comment'''

# strings

if('hello world' == "hello world" == """hello world"""):
    print('its all true')
else:
    print('its false')

print('hello'.capitalize())

listOfValues = "some,csv,values".split(",")
print(listOfValues)

for v in listOfValues :
    print(v)

print("Nice to meet you {0}. I am {1}".format("Michael", "David"))

name = "Jason"
job = "developer"

print(f"this is a formatted string for {name}. I am a {job}")


# none is similar to null is javascript. it evalutes to false. use it as a place holder to a variable you have defined but havent assigned to a value
aliens_found = None
if(aliens_found):
    print("sweet you found an alien")
else:
    print("no aliens found")