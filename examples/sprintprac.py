people = ["Abe", "Bill", "Charles", "Dolly", "Evelyn", "Frank", "Gunther"]

# comp for names that start with D
dcomp = [item for item in people if item[0] == 'D']
print(dcomp)
# comp for names that end in Y
ycomp = [item for item in people if item[len(item)-1] == 'y']
print(ycomp)
# comp for names that start with B through D
bdcomp = [item for item in people if item[0]=='B' or item[0]=='C' or item[0]=='D']
print(bdcomp)
# comp for names but in uppercase
upcomp = [item.upper() for item in people]
print(upcomp)