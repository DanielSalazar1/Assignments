def f_to_c(Fahrenheit):
    #Formula = (32 °F − 32) × 5 / 9
    #https://www.google.com/search?sxsrf=ACYBGNTcnBxSPeT_c73q8f_jn1O0NkRh3A%3A1568156230358&source=hp&ei=Rip4XcH4E-bB_QbnsJagAg&q=formula+from+fahrenheit+to+celsius&oq=formula+from+fah&gs_l=psy-ab.1.0.0i203l2j0i22i10i30j0i22i30l7.58.4066..12804...0.0..0.140.1953.2j14......0....1..gws-wiz.......35i39i19j35i39j0i67j0.wdfp0Bzf_M4
    c = (f - 32) * 5 / 9
    return c

f = 100
c = f_to_c(f)

print("Fahrenheit of " + str(f) + " is " + str(c) + "in Celsius")
