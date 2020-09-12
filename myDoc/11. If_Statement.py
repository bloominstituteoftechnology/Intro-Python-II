Mahiya = "Crush"
crush = Mahiya
print(Mahiya)

if len(Mahiya) > len(crush) or 2:               # If one condition is true 
    print("I love you Apu")
elif Mahiya == "crush" or crush:
    print("I still love you apu")
elif crush == Mahiya:
    print("I will always love you apu")
else:
    print("Where's Apuuu")


if Mahiya == crush and "Crush":              # If both condition is true
    print("I love you a lot apu")


if Mahiya == "Crush" and not(crush):         # This won't output because crush is Mahiya, but we are saying it isn't
    print("I so much Love you Apu")
else:
    print("Always love you apu")