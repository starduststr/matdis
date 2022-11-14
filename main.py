# KELOMPOK 4
# Defa Nugraha
# Dewi Ramdani
# Shandi Maulana S
# M.Fikri
# Bambang Yudoyono

# https://github.com/starduststr/matdis


#import math as mt

def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan



def faktor(p1,p2):
    n = 1
    c = 1
    
    while True:
        # print(n,c)
        # print(-n,-c)
        if n*c == p1 and n+c == p2:
            return c,n
        
        if -n*-c == p1 and -n+-c == p2:
            return -c, -n

        c += 1

        if c == 10:
            n +=1
            c = 1
        
    

def main():
    an = input("Masukan nilai an : ")

    a0 = eval(input("Masukan nilai a0 : "))
    a1 = eval(input("Masukan nilai a1 : "))

    data = an.split()
    # print(data)
    
    #menentukan derajat
    try :
        f = data[2].split('-')
        derajat = int(f[1])
    except Exception:
        derajat = 1

    
    if derajat == 2:
        #Pindah ruas
        if data[1] == '-':
            op = '+'
        else :
            op = '-'

        # print("an - {} {} {} = 0".format(data[0],op,data[2]))

        #mencari akar dengan faktor
        kali = data[2]
        tambah = data[0]

        r1, r2 = faktor(int(kali[0]), int(tambah[0]))
        # print("(r - {}) (r - {}) = 0".format(r1, r2))

        hasil = """ an = {} , a0 = {}, a1 = {}
    = an - {} {} {} = 0
    r**n-{}r + {} = 0
    (r - {}) (r - {}) = 0
    r1 = {}, r2 = {}

    """.format(an,a0,a1,data[0],op,data[2],int(kali[0]),int(tambah[0]),r1,r2,r1,r2)

        print(hasil)

    
    #solusi umum 

        #a0
        # a0_c1 = hitung_pangkat(r1, 0)
        # a0_c2 = hitung_pangkat(r2, 0)

        # if a0_c1 == 0:
        #     a0_c1 = ""
        # if a0_c2 == 0:
        #     a0_c2 = ""
        # a0 = "{}c1 + {}c2".format(a0_c1, a0_c2)

        # a0 = "c1 + c2"

        #a1
        a1_c1 = hitung_pangkat(r1, 1)
        a1_c2 = hitung_pangkat(r2, 1)

        if a1_c1 == 0:
            a1_c1 = ""
        if a1_c2 == 0:
            a1_c2 = ""
        # a1 = "{}c1 + {}c2".format(a1_c1, a1_c2)

        # print(a0)
        # print(a1)
        solusiUmum = """ an = C1 r**n + C2 r**n
    an = c1 {}**n + c2 {}**n
    a0 = {} -> a0 = C1({})**0 + C2({})**0
                {}= C1 + C2
    a1 = {} -> a1 = C1({})**1 + C2({})**1
                {}= {}C1 + {}C2

    """.format(r1,r2,a0,r1,r2,a0,a1,r1,r2,a1,r1,r2)
        print(solusiUmum)
    else :
        #Pindah ruas

        # print("an - {} {} {} = 0".format(data[0],op,data[2]))

        #mencari akar dengan faktor
        # kali = data[2]
        tambah = data[0]

        r1, r2 = faktor(int(kali[0]), int(tambah[0]))
        # print("(r - {}) (r - {}) = 0".format(r1, r2))

        hasil = """ an = {} , a0 = {}, a1 = {}
    = an - {}  = 0
    r**n-{}r + {} = 0
    (r - {}) (r - {}) = 0
    r1 = {}, r2 = {}

    """.format(an,a0,a1,data[0],0,int(tambah[0]),r1,r2,r1,r2)

        print(hasil)

    
    #solusi umum 

        #a0
        # a0_c1 = hitung_pangkat(r1, 0)
        # a0_c2 = hitung_pangkat(r2, 0)

        # if a0_c1 == 0:
        #     a0_c1 = ""
        # if a0_c2 == 0:
        #     a0_c2 = ""
        # a0 = "{}c1 + {}c2".format(a0_c1, a0_c2)

        # a0 = "c1 + c2"

        #a1
        a1_c1 = hitung_pangkat(r1, 1)
        a1_c2 = hitung_pangkat(r2, 1)

        if a1_c1 == 0:
            a1_c1 = ""
        if a1_c2 == 0:
            a1_c2 = ""
        # a1 = "{}c1 + {}c2".format(a1_c1, a1_c2)

        # print(a0)
        # print(a1)
        solusiUmum = """ an = C1 r**n + C2 r**n
    an = c1 {}**n + c2 {}**n
    a0 = {} -> a0 = C1({})**0 + C2({})**0
                {}= C1 + C2
    a1 = {} -> a1 = C1({})**1 + C2({})**1
                {}= {}C1 + {}C2

    """.format(r1,r2,a0,r1,r2,a0,a1,r1,r2,a1,r1,r2)
        print(solusiUmum)

try:
    main()
except:
    print('terjadi kesalahan')
