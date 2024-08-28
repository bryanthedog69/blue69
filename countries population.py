import matplotlib.pyplot as plt
countries = dict()
countries = {"Nigeria":223804632, "Ethopia": 126527060, "Egypt": 112716598, "Dr congo": 102262808, "Tanzania": 67438106, "South africa": 60414495, "Kenya": 55100586, "Sudan": 48109006, "Uganda": 48582334, "Algeria": 45606480} 
print(countries)
names = countries.keys()
population = countries.values()
print(names, population)
plt.pie(population, labels =names, colors = ['red', 'green', 'yellow','blue', 'purple', 'orange', 'pink', 'white', 'brown', 'lime'], startangle =90, autopct = "%1.if%%", shadow =True,explode = (0.1,0,0,0,0,0,0,0,0,0))
plt.title("contries population")
plt.show()