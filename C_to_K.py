def c_to_k(celsius):
    #Formula = K = °C + 273.15
    #Took from https://www.softschools.com/formulas/physics/kelvin_to_celsius_formula/47/
    k = c + 273.15
    return k

c = 100
k = c_to_k(c)

print("Celsius of " + str(c) + " is " + str(k) + " in Kelvin")
