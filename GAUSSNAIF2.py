

# metode Bisection
print('Program Mencari Akar Persamaan Nonlinear ')
print('='*25+'ELIMINASI GAUSS'+'='*25)
print('\t','\t','\t','\t','oleh')
print('\t','\t','\t',' Iren Brigita Pasu')
print('\t','\t','\t',' NIM: 231-18-008')
print("AB=8")
print("\n 3x+z=10\n y+2z=5\n -3y-2z=-AB")
print()
print("\n")

# print("=====PERSAMAAN 1=====\n")


b= 3
d= 0
kamu= 1
konstanta= 10

# print("\n=====PERSAMAAN 2=====\n")
f= 0
h= 1
kamu1=2
konstanta1= 5

# print("\n=====PERSAMAAN 3=====\n")
j= 0
l= -3
kamu2= -2
konstanta2= -8

print("\n===Bentuk MATRIKS===")
print("\nKOEFISIEN\t\t KONSTANTA")
print("\n[","%f"%b," %f"%d," %f"%kamu,"]","\t\t[","%i"%konstanta,"]\n")
print("\n[","%f"%f," %f"%h," %f"%kamu1,"]","\t\t[","%i"%konstanta1,"]\n")
print("\n[","%f"%j," %f"%l," %f"%kamu2,"]","\t\t[","%i"%konstanta2,"]\n")

#LANGKAH 1
#normalisasi baris 1 dibagi dengan a11
a11=b/b
a12=d/b
a13=kamu/b
cos=konstanta/b
#baris ke 2=a21*normalisasi
a21=f*a11
a22=f*a12
a23=f*a13
cos1=f*konstanta1
#a31*normalisasi
a31=j*a11
a32=j*a12
a33=j*a13
cos2=j*konstanta2
print("==LANGKAH 1==\n")
print("\n[","%.8f"%a11," %.8f"%a12," %.8f"%a13,"]","\t\t[","%.8f"%cos,"]\n")
print("[","%.8f"%a21," %.8f"%a22," %.8f"%a23,"]","\t\t[","%.8f"%cos1,"]\n")
print("[","%.8f"%a31," %.8f"%a32," %.8f"%a33,"]","\t\t[","%.8f"%cos2,"]\n")

#LANGKAH 2
#baris pertama =persamaan ternormalisasi
a11baru=a11
a12baru=a12
a13baru=a13
cosbaru=cos
#bariske 2 = baris2persamaanawal-baris2persamaanlangka1
a21baru=f-a21
a22baru=h-a22
a23baru=kamu1-a23
cos1baru=konstanta1-cos1
#baris 3 = baris3 persamaanawal-baris3 persamaanlangka1
a31baru=j-a31
a32baru=l-a32
a33baru=kamu2-a33
cos2baru=konstanta2-cos2
print("\n\n==LANGKAH 2==\n")
print("\n[","%.8f"%a11baru," %.8f"%a12baru," %.8f"%a13baru,"]","\t\t[","%.8f"%cosbaru,"]\n")
print("[","%.8f"%a21baru," %.8f"%a22baru," %.8f"%a23baru,"]","\t\t[","%.8f"%cos1baru,"]\n")
print("[","%.8f"%a31baru," %.8f"%a32baru," %.8f"%a33baru,"]","\t[","%.8f"%cos2baru,"]\n")

#LANGKAH 3
#baris pertama =persamaan ternormalisasi
a11baru1=a11
a12baru1=a12
a13baru1=a13
cosbaru1=cos
#normalisasi baris 2 dibagi dengan a22
a21baru1=a21baru/a22baru
a22baru1=a22baru/a22baru
a23baru1=a23baru/a22baru
cos1baru1=cos1baru/a22baru
#a32*normalisasi
a31baru1=a32baru*a21baru1
a32baru1=a32baru*a22baru1
a33baru1=a32baru*a23baru1
cos2baru1=a32baru*cos1baru1
print("\n\n==LANGKAH 3==\n")
print("\n[","%.8f"%a11baru1," %.8f"%a12baru1," %.8f"%a13baru1,"]","\t\t[","%.8f"%cosbaru1,"]\n")
print("[","%.8f"%a21baru1," %.8f"%a22baru1," %.8f"%a23baru1,"]","\t\t[","%.8f"%cos1baru1,"]\n")
print("[","%.8f"%a31baru1," %.8f"%a32baru1," %.8f"%a33baru1,"]","\t[","%.8f"%cos2baru1,"]\n")

#LANGKAH 4
#baris pertama =persamaan ternormalisasi
a11baru2=a11
a12baru2=a12
a13baru2=a13
cosbaru2=cos
#bariske 2 = persamaan ternormalisasi baris ke 2 langkah 3
a21baru2=a21baru1
a22baru2=a22baru1
a23baru2=a23baru1
cos1baru2=cos1baru1
#baris 3 = baris3 langkah3-baris2 langkah2
a31baru2=a31baru1-a31baru
a32baru2=a32baru1-a32baru
a33baru2=a33baru1-a33baru
cos2baru2=cos2baru1-cos2baru
print("\n\n==LANGKAH 4==\n")
print("\n[","%.8f"%a11baru2," %.8f"%a12baru2," %.8f"%a13baru2,"]","\t\t[","%.8f"%cosbaru2,"]\n")
print("[","%.8f"%a21baru2," %.8f"%a22baru2," %.8f"%a23baru2,"]","\t\t[","%.8f"%cos1baru2,"]\n")
print("[","%.8f"%a31baru2," %.8f"%a32baru2," %.8f"%a33baru2,"]","\t[","%.8f"%cos2baru2,"]\n")

print("======Subsitusi ke belakang=====\n")
Z=cos2baru2/a33baru2
print("Z =%f"%Z)
Y= (cos1baru1-(a23baru2*Z))/a22baru2
print("Y =%f"%Y)
X=(cosbaru2-a12baru2*Y-a13baru2*Z)/a11baru2
print("X =%f"%X)


print("\n==Pembuktian nilai X,Y,Z ke dalam persamaan==\n")
hasilnya=(b*X)+(d*Y)+(kamu*Z)
hasilnya1=(f*X)+(h*Y)+(kamu1*Z)
hasilnya2=(j*X)+(l*Y)+(kamu2*Z)
print("Hasil persamaan 1 = %f"%hasilnya)
print("Hasil persamaan 2 = %f"%hasilnya1)
print("Hasil persamaan 3 = %f"%hasilnya2)


