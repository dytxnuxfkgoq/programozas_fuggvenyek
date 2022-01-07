"""feladat(1)
def kerulet(a,b,c):
    kerulet = a+b+c
    return kerulet
print(kerulet(7,9,4))

def terulet(a):
    return(a*a)
print(terulet(5))

def string(txt):
    return len(txt)

def negyzet(n):
    return (n**2)
print(negyzet(5))

def koszont():
    print("üdv a fedélzeten")
koszont()

def feladat(a):
    print()
    print(f"{a}. feladat:")
feladat(3)"""

def szamjegy(a):
    if 0 < szam < 10:
        return "egyszamjegyu"
    else:
        return "nem egyszamjegyu"

def negyzet(szam):
    return szam**2

def negyzet_elj(szam):
    print(szam**2)

def hossz(t):
    return len(t)

def paros(szam):
    if szam%2==0:
        return "páros"
    else:
        return "páratlan"

def feladat(i):
    print(f"{i}. feladat: ")

def szamok(szam1,szam2):
    if szam1>szam2:
        return szam1
    else:
        return szam2

feladat(1)
szam = 5
print(szam,szamjegy(szam))
print(szam,negyzet(szam))

feladat(2)
negyzet_elj(szam)
x=2*negyzet(szam)
print(x)
txt=input("szöveg:")
print(f"A szöveg hossza: {hossz(txt)}")

feladat(3)
print(szam,paros(szam))
for x in range(1,51):
    print(x,paros(x))

feladat(4)
szam1=int(input("Kérek egy számot:"))
szam2=int(input("Kérek egy másik számot"))
print(szamok(szam1,szam2))



