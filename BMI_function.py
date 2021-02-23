
def bmifunkcja():
    wzrostcm = input("Podaj swój wzrost: ")
    waga = input("Podaj swoją wagę:")
    wzrost = int(wzrostcm) /100
    bmi = int(waga) / wzrost**2
    print ("Twoje BMI to", bmi)
        if bmi <= 18.5:
    print("Niedowaga")
        elif bmi > 18.5 and bmi <=24.99:
    print("prawdidlowa waga")
        elif bmi > 24.99 and bmi <=29.99:
    x = "nadwaga"
        elif bmi > 30:
    print("otylosc")
