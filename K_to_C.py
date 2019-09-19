#KELVIN TO celsius

def k_to_c(kelvin):
    #Formula = K = °C + 273.15
    #Took from https://www.softschools.com/formulas/physics/kelvin_to_celsius_formula/47/
    c = k - 273.15
    return c

k = 100
c = k_to_c(k)

print("Kelvin of " + str(k) + " is " + str(c) + " in Celsius")
