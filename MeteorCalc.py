d = int(input("Enter diameter, m: "))
v = int(input("Enter speed, m/s: "))
dens = int(2600)
eff = float(4.184E12)
V = 4/3 * 3.1415 * (d/2)**3;
print (((V*dens)*(v**2)/2)/eff)
print("Explosion power, KT=%f" % (((V*dens)*(v**2)/2)/eff))