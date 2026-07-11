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

name = input("Emloyee Name:").title()

if name in ishgarler:
    choice = input("Full information (yes/no): ")
    if choice == "yes":
        print(ishgarler[name])
    elif choice == "no":
        info = input("hunari/yasayan_yeri/yashy: ").lower()
        print(ishgarler[name][info])
    else:
        print("Invalid input")
else:
    print(name, "is not in emplayees")
