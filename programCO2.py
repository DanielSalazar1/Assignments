co2 = input("Please input air quality value: ")
co2 = int(co2)
if co2 > 399 and co2 < 698:
    print("Excelent")
elif co2 > 699 and co2 < 898:
    print("Good")
elif co2 > 899 and co2 < 1098:
    print("Fair")
elif co2 > 1099 and co2 < 1598:
    print("Mediocre, contaminated indoor air")
elif co2 > 1599 and co2 < 2101:
    print("Bad, heavily contaminated indoor air")
