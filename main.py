x = 5 # integer
y = 6.5 #float/double
emri = "medina"

#typecasting
#x = str(x)

print(type(x))
print(type(y))
print(type(emri))

print(x+y)

age = 30

print("Besarti eshte", age, "vjeq" )

first_name = "Blend"
last_name = "Zeqiri"

full_name = first_name + " " + last_name

print(full_name)

cars = ["Audi", "BMW", "Mercedes", "Mazda"]

print(cars[1])

diff_elem = ["Klima", "Marker", 2, 30, 4.5]

#elementi i fundit i listes
print(diff_elem[-1])

diff_elem.append("Futboll")

print(diff_elem)

diff_elem[0] = "Klime"

print(diff_elem)

diff_elem.insert(1, "Kompjuteri")

print(diff_elem)

diff_elem.remove("Marker")

print(diff_elem)

#reversed list
print(diff_elem[::-1])

#tuppless

words = ("shkolla", "klasa", "python", "sql")

print(words)

print(words[-1])

print(words[-3])

#slicing

print(words[0:2])

#words[2] = "Java"

print(words[1].count("a"))

#Dictionaries
# key value pairs, muteable

countries = {
            "Kosova":"Prishtina",
            "Shqiperia":"Tirana",
            "Germany":"Berlin",
            "Canada":"Ottawa",
            "Australia":"Canberra",
            "Egypt":"Cairo"
            }

ks = countries["Kosova"]

print(ks)

kryeqytetet = countries.values()

print(kryeqytetet)

shtetet = countries.keys()\

print(shtetet)