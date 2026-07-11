ishgarler={"Mekan" : {"hunari" : "programist",
"yasayan yeri" : "Ashgabat",
 "yashy" : 22},

"Oraz" : {"hunari" : "hasapchy",
"yasayan yeri" : "Ashgabat",
"yashy" : 30},


"Selim" : {"hunari" : "Mollim",
"yasayan yeri" : "Ashgabat",
"yashy" : 40},
}

for i, j in ishgarler.items():
    print(i)
    for x, y in j.items():
        print(x, "-", y)