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
    print('van benne 2-es, ezen az indexen: {}'.format(i))
else:
    print('nincs benne 2-es')

# pythonban ha indexet keresünk:
# hányadik elem a 2-es szám:
print(x.index(2))

# 4. megszámlálás tétele
# számoljuk meg, hogy hány db páros szám van a listában
x = [5, 7, 2, 9, 5, 4]
db = 0
for elem in x:
    # oszthatóság vizsgálata maradékos osztás segítségével
    # (páros szám esetében 2-vel)
    if elem % 2 == 0:
        db = db + 1
print('{} db páros szám van a listában\n'.format(db))

# 5. maximumkiválasztás tétele
x = [5, 7, 2, 9, 5, 4]
# van egy olyan függvény a pythonban, hogy max
# ezt inkább ne írjuk felül, ezért legyen a neve max_index
max_index = 0
for i, num in enumerate(x):
    if x[i] > x[max_index]:
        max_index = i
print("a legnagyobb elem a tömbben: {}".format(x[max_index]))

# 6. buborékrendezés tétel
# azért hívják buboréknak, mert az felfelé száll, és
# a legagyobb elem is mindig felfelé kerül
# rendezzük a tömb elemeit sorba
x = [5, 7, 2, 9, 5, 4]
n = len(x)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if x[j] > x[j + 1]:
            # kicseréljük a j-edik és a j+1-edik elemet:
            x[j], x[j+1] = x[j+1], x[j]
# a megrendezett x tömb:
print(x)

# az x tömb elemeit újra összekeverjük a következő példához
x = [5, 7, 2, 9, 5, 4]

# pythonban a lista rendezése:
print(sorted(x))

# 7. tétel: minimumkiválasztásos rendezés
# itt lentről megyünk felfelé, előre rendezzük a kisebbeket
# külső ciklus végig megy a tömb összes elemén, belső ciklus szűkül
# hatékonyabb, mint a buborékrendezés
# kevesebb cserét végez el (rögtön a helyére rakja az elemet)
for i in range(0, n):
    min_index = i
    for j in range (i+1, n):
        if x[min_index] > x[j]:
            min_index = j
    x[i], x[min_index] = x[min_index], x[i]
print(x)

# 8. tétel: faktoriális számítása
def fakt(n):
    if n == 0:
        return 1
    else: 
        # rekurzív függvény: saját magát meghívja
        return n * fakt(n-1)
print(fakt(4))
