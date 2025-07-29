# List is a collection of items in a particular order
'''
countries = []
print(type(countries))
states = ()
print = (type(states))

countries = ["Australia", "Malawi", "Nigeria", "Jamaica", "USA"]
print(countries)

favouriteMovies = ["Dark", "Ironheart", "Sandman", "Oldguard", "head of state"]
numbers = [1,2,3,4,5,6,7,8,9,10]
myBio = ["Victor", "26", False, "male","5'2", "Black" ]
provisionList = ["Garri", "Milk", "Waffles", "Cornflakes", "Sugar"]
print(favouriteMovies)
print(numbers)
print(myBio)
print(provisionList)

android = ["Tecno", "Itel", "Redmi", "Samsung"]
ios = ["iphone11", "iphone13" "iphone8", "iphone7"]
phones = [android, ios]
print(phones)

code = ["x", "h", "e", "z", "l", "l", "!", "p", "o", "-", "n" ,"", "w", "@", "r", "d", "o", "#"]
h = code[1]
e = code[2]
l = code[4]
ll = code[5]
o = code[8]
print(h+e+l+ll+o)

w = code[-6]
o = code [-2]
r = code [-4]
l = code [5]
d = code [-3]
print(w+o+r+l+d)

print(code[::-1])

grid = [["the", "sky", "is"],["full", "of", "stars"],["shining", "bright", "tonight"]]

first = grid [0][0]
second = grid [0][1]
print(f"{first} {second}")

third = grid [1][2]
fourth = grid [2][0]
print(f"{first}  {third}  are  {fourth}")
print(grid[1][::-1])

myFruits = ["mangoe", "avocado", "apple", "guava"]
myFruits[3]= "pineapple" 
print(myFruits)
myFruits.append("banana")
print(myFruits)
myFruits.insert(1,"mangoe")
print(myFruits)


playlist = ["song A", "song B", "song C"]
playlist[1] = "song D"
print (playlist) 

playlist.append("song E")
print(playlist)

playlist.insert(0, "intro")
print(playlist)
'''
#unpacking  a list
countries = ["spain", "malawi", "iran", "usa"]
del countries[0:1]
countries.remove("malawi")
print(countries)
country1, country2,country3, = countries[0:]

print(country1)
print(country2)
print(country3)

accounts = [
 ["1001", "joy", "savings", 1500],
 ["1002", "david", "current", 2000],
 ["1003", "ruth", "savings", 1800]

]

accounts.remove(accounts[1])
print(accounts)

name, accountType = accounts [1][1:3]
print(name)
print(accountType)

names, accountTypes = accounts [0][1:3]
print(names)
print(accountTypes)

numbers = [1,2,3]
print(numbers[100-98])
print(numbers[0**100])
 
# calculator with a history
history = []
firstNumber = float(input("enter first number:\n>>"))
secondNumber = float(input("enter second number:\n>>"))
total = firstNumber + secondNumber
result = f"{firstNumber} + {secondNumber} = {total}"
history.append(result)
print(result)
















