import pandas as pd
import matplotlib.pyplot as plt
countries = dict()
countries = { " usa" :25.43 / 0.333, "china" :1.472 / 0.1412, "japan" :4.25 / 0.1251, "germany" :3.85 / 0.838, 
             "india" :3.41 / 1.417, "uk" :2.67 / 0.6697, "france" :2.63 / 0.6797,
             "russia" :2.24 / 0.1442, "canada" :2.16 / 0.3893, "italy" :2.04 / 0.5894}

names = countries.keys()
population= countries.values()
plt.pie(population,labels = names,
        colors = ["red", "green", "pink","yellow","orange","blue","brown","cyan","purple","lime"],
        autopct = " %1.if%%", startangle = 90, explode =(0,0,0,0,0,0.3,0,0,0,0), shadow = True)
plt.title("countries GDP per capita")
plt.show()


