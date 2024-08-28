import datetime
name = str (input ("Enter your name:"))
age = int (input ("Enter your age:"))
nin = int (input ("Enter your nin:"))
phone = int (input ("Enter your phone:"))
data_reg = datetime.datetime.now ()
address = str (input ("Enter your address:"))
sex = str (input ("Enter your gender:"))
nationality = str (input ("Enter your nationality:"))

d_name = {"Name": name, "Age": age, "Nin": nin, "Phone": phone, "Resgistration Date" : data_reg, "sex": sex, "nationality": nationality }

print (d_name)

for keys, values in d_name.items():
    print (keys, values)
    
    
    


