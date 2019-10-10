tvoc = input("Please input air quality value: ")
tvoc = int(tvoc)

if tvoc > 0 and tvoc < 65:
    print("{Level 1 - Excelent}", "{Higienic rating - No objections}", "{Recomendations - Target value}", "{Exposure limit - no limit}")
elif tvoc > 65 and tvoc < 220:
    print("{Level 2 - Good}", "{Higienic rating - No relevant objections}", "{Recomendations - Ventilation}", "{Exposure limit - no limit}")
elif tvoc > 220 and tvoc < 660:
    print("{Level 3 - Moderate}", "{Higienic rating - Some objections}", "{Recomendations - Intensified ventilation}", "{Exposure limit - < 12 months}")
elif tvoc > 660 and tvoc < 2200:
    print("{Level 4 - Poor}", "{Higienic rating - Major objections}", "{Recomendations - Intensified ventilation}", "{Exposure limit - < 1 month}")
elif tvoc >2200 and tvoc < 5500:
    print("{Level 5 - Unhealty}", "{Higienic rating - Situation not acceptable}", "{Recomendations - Use only if unnavoidable}", "{Exposure limit - hours}")

    
