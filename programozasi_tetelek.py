# csere algoritmusa
# cseréljük ki a és b változó értékét egy segédváltozóval
# a és b mellé kell egy c, ami először üres, de beletöltöd a-t
# így a üres lesz, és át tudom bele tölteni b-t
# b-be beletöltöm a c-t (régi a-t)
a = 5
b = 9
c = a
a = b
b = c
print(a,b)

# pythonos megoldása a cserének:
a, b = b, a
print(a, b) 

# 1. sorozatszámítás tétele
tomb = [5, 7, 2, 9, 5, 4]
osszeg = 0
for szam in tomb:
    osszeg = szam + osszeg

print(osszeg)

# pythonos megoldás:
print(sum(tomb))

# 2. eldöntés tétele
# döntsük el, hogy van-e 2-es szám a listában
# n = a tömb elemeinek száma
x = [5, 7, 2, 9, 5, 4]
n = len(x)
i = 0
while i < n and x[i] != 2:
    i = i + 1
if i < n:
    print('van benne 2-es')
else:
    print('nincs benne 2-es')       

# pythonban ha meg akarjuk nézni, hogy egy adott elem
# létezik-e a tömbben:
print(2 in x)

# 3. lineáris keresés tétele
# lényegében ugyanaz, mint az eldöntés, csakez az indexet adja vissza
# vagyis, hogy hányadik elem a 2-es szám
x = [5, 7, 2, 9, 5, 4]
n = len(x)
i = 0
while i < n and x[i] != 2:
    i = i + 1
if i < n:
    print('van benne 2-es, ezen az indexen: {}'.format(i+1))
else:
    print('nincs benne 2-es')     