co2 = input("Please input CO2 value ")
co2 = int(co2)
if co2 > 1700 and co2 < 2200:
    print("Air quality is bad")
elif co2 > 1200 and co2 < 1600:
    print("Air quality is mediocre, ventilation recommended")
elif co2 > 1000 and co2 < 1100:
    print("Air quality is fair")
elif co2 > 800 and co2 < 900:
    print("Air quality is good")
elif co2 > 300 and co2 < 700:
    print("Air quality is amazing, keep improving!")
