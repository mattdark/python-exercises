a = int(input("Introduce año: "))
m = int(input("Introduce mes: "))
d = int(input("Introduce dia: "))
meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 2016
month = 9
day = 5
ny = year - (a+1) # Años completos transcurridos
nd = meses[m-1] - d    # Dias transcurridos
for i in range(m, 12): # desde fecha de nacimiento
    nd += meses[i]     # hasta último mes del año
nday = day                   # Dias transcurridos
for i in range((month - 1)): # Desde primer mes
    nday += meses[i]         # hasta fecha actual
nd = nd + nday
dias = ny * 365.25
dias = int(nd + dias)
if m == 1:
    if a % 4 == 0:
        dias = dias + 1
if year % 4 == 0:
    dias = dias + 1
print("Dias transcurridos: ", dias)
