import random

Country = {"Turkey" : "Ankara",
                   "Kazakhstan" : "Astana",
                   "Azerbaijan" : "Baku",
                   "Iraq" : "Baghdad",
                   "China" : "Beijing",
                   "Germany" : "Berlin",
                   "Kyrgyzstan" : "Bishkek",
                   "Australia" : "Canberra",
                   "Qatar" : "Doha",
                   "Tajikistan" : "Dushanbe",
                   "Pakistan" : "Islamabad",
                   "Afghanistan" : "Kabul",
                   "Spain" : "Madrid",
                   "Belarus" : "Minsk",
                   "Russia" : "Moscow",
                   "Canada" : "Ottawa",
                   "France" : "Paris",
                   "Italy" : "Rome",
                   "Uzbekistan" : "Tashkent",
                   "Japan" : "Tokyo" }
jemi=0
correct=0
sana=1
A=list(Country.keys())
B=random.choice(A)
while True:
    capital=input(f"{sana}. What is the capital of {B}?")
    sana+=1
    if Country[B]==capital and capital!="quit":
        print("Correct")
        correct+=1
        jemi+=1
    elif Country[B]!= capital and capital!="quit":
        print("Incorrect")
        jemi+=1
        print(f"Correct{Country[B]}")
    elif capital=="quit":
        print(f"Your score {correct}")
