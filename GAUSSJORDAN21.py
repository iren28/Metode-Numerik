
# metode Bisection
print('Program Mencari Akar Persamaan Nonlinear ')
print('='*25+'GAUSS JORDAN'+'='*25)
print('\t','\t','\t','\t','oleh')
print('\t','\t','\t',' Iren Brigita Pasu')
print('\t','\t','\t',' NIM: 231-18-008')
print("AB=8")
print("\n x+4y=2\n -y+z=1\n 2y+z=A,B")
print()
print("\n")

#print("=====PERSAMAAN 1=====\n")


b= 1
d= 4
kamu= 0
konstanta= 2

# MATRIKS IDENTITAS
a14=1
a15=0
a16=0

a24=0
a25=1
a26=0

a34=0
a35=0
a36=1


# print("\n=====PERSAMAAN 2=====\n")
f= 0
h= -1
kamu1= 1
konstanta1= 1

#print("\n=====PERSAMAAN 3=====\n")
j= 0
l= 2
kamu2= 1
konstanta2= 0.8

print("\n===Bentuk MATRIKS===")
print("\nKOEFISIEN MATRIKS IDENTITAS  KONSTANTA")
print("\n[","%.8f"%b," %.8f"%d," %.8f"%kamu,"]","\t[",a14 ,a15,a16,"]","\t[","%f"%konstanta,"]\n")
print("\n[","%.8f"%f," %.8f"%h," %.8f"%kamu1,"]","[",a24,a25,a26,"]","\t[","%f"%konstanta1,"]\n")
print("\n[","%.8f"%j," %.8f"%l," %.8f"%kamu2,"]","\t[",a34,a35,a36,"]","\t[","%f"%konstanta2,"]\n")

#LANGKAH 1
#normalisasi baris 1 dibagi dengan a11
a11=b/b
a12=d/b
a13=kamu/b
a14baru=a14/b
a15baru=a15/b
a16baru=a16/b
cos=konstanta/b
#baris ke 2=a21*normalisasi
a21=f*a11
a22=f*a12
a23=f*a13
a24baru=f*a24
a25baru=f*a25
a26baru=f*a26
cos1=f*konstanta1
#a31*normalisasi
a31=j*a11
a32=j*a12
a33=j*a13
a34baru=j*a34
a35baru=j*a35
a36baru=j*a36
cos2=j*konstanta2
print("==LANGKAH 1==\n")

print("[","%.8f"%a11," %.8f"%a12," %.8f"%a13,"]","\t[ ",a14baru," ",a15baru," ",a16baru,"]","\t[","%.8f"%cos,"]\n")
print("[","%.8f"%a21," %.8f"%a22," %.8f"%a23,"]","[ ",a24baru,"  ",a25baru,"  ",a26baru,"]","\t[","%.8f"%cos1,"]\n")
print("[","%.8f"%a31," %.8f"%a32," %.8f"%a33,"]","\t[ ",a34baru,"  ",a35baru,"  ",a36baru,"]","\t[","%.8f"%cos2,"]\n")

#LANGKAH 2
#baris pertama =persamaan ternormalisasi
a11baru=a11
a12baru=a12
a13baru=a13
a14baru1=a14baru
a15baru1=a15baru
a16baru1=a16baru
cosbaru=cos
#bariske 2 = baris2persamaanawal-baris2persamaanlangka1
a21baru=f-a21
a22baru=h-a22
a23baru=kamu1-a23
a24baru1=a24-a24baru
a25baru1=a25-a25baru
a26baru1=a26-a26baru
cos1baru=konstanta1-cos1
#baris 3 = baris3 persamaanawal-baris3 persamaanlangka1
a31baru=j-a31
a32baru=l-a32
a33baru=kamu2-a33
a34baru1=a34-a34baru
a35baru1=a35-a35baru
a36baru1=a36-a36baru
cos2baru=konstanta2-cos2
print("\n\n==LANGKAH 2==\n")
print("\n[","%.8f"%a11baru," %.8f"%a12baru," %.8f"%a13baru,"]","\t[ ",a14baru1," ",a15baru1," ",a16baru1,"]","\t[","%.8f"%cosbaru,"]\n")
print("[","%.8f"%a21baru," %.8f"%a22baru," %.8f"%a23baru,"]","[",a24baru1,"  ",a25baru1  ,"  ",a26baru1,"]","\t[","%.8f"%cos1baru,"]\n")
print("[","%.8f"%a31baru," %.8f"%a32baru," %.8f"%a33baru,"]","\t[ ",a34baru1," ",a35baru1," ",a36baru1,"]","\t[","%.8f"%cos2baru,"]\n")

#LANGKAH 3
#normalisasi baris 2 dibagi dengan a22
a21baru1=a21baru/a22baru
a22baru1=a22baru/a22baru
a23baru1=a23baru/a22baru
a24baru2=a24baru1/a22baru
a25baru2=a25baru1/a22baru
a26baru2=a26baru1/a22baru
cos1baru1=cos1baru/a22baru
#baris pertama a22 *persamaan ternormalisasi
a11baru1=a12baru*a21baru1
a12baru1=a12baru*a22baru1
a13baru1=a12baru*a23baru1
a14baru2=a12baru*a24baru2
a15baru2=a12baru*a25baru2
a16baru2=a12baru*a26baru2
cosbaru1=a12baru*cos1baru1
#a32*normalisasi
a31baru1=a32baru*a21baru1
a32baru1=a32baru*a22baru1
a33baru1=a32baru*a23baru1
a34baru2=a32baru*a24baru2
a35baru2=a32baru*a25baru2
a36baru2=a32baru*a26baru2
cos2baru1=a32baru*cos1baru1
print("\n\n==LANGKAH 3==\n")
print("\n[","%.8f"%a11baru1," %.8f"%a12baru1," %.8f"%a13baru1,"]","[",a14baru2,"  ",a15baru2  ,"  ",a16baru2,"]","\t\t[","%.8f"%cosbaru1,"]\n")
print("[","%.8f"%a21baru1," %.8f"%a22baru1," %.8f"%a23baru1,"]","[",a24baru2,"  ",a25baru2  ,"  ",a26baru2,"]","\t\t[","%.8f"%cos1baru1,"]\n")
print("[","%.8f"%a31baru1," %.8f"%a32baru1," %.8f"%a33baru1,"]","[",a34baru2,"  ",a35baru2  ,"  ",a36baru2,"]","\t\t[","%.8f"%cos2baru1,"]\n")

#LANGKAH 4
#baris pertama =baris langkah2-baris 1 langkah 3
a11baru2=a11baru-a11baru1
a12baru2=a12baru-a12baru1
a13baru2=a13baru-a13baru1
a14baru3=a14baru1-a14baru2
a15baru3=a15baru1-a15baru2
a16baru3=a16baru1-a16baru2
cosbaru2=cosbaru-cosbaru1
#bariske 2 = persamaan ternormalisasi baris ke 2 langkah 3
a21baru2=a21baru1
a22baru2=a22baru1
a23baru2=a23baru1
a24baru3=a24baru2
a25baru3=a25baru2
a26baru3=a26baru2
cos1baru2=cos1baru1
#baris 3 = baris3 langkah2-baris3 langkah3
a31baru2=a31baru-a31baru1
a32baru2=a32baru-a32baru1
a33baru2=a33baru-a33baru1
a34baru3=a34baru1-a34baru2
a35baru3=a35baru1-a35baru2
a36baru3=a36baru1-a36baru2
cos2baru2=cos2baru-cos2baru1
print("\n\n==LANGKAH 4==\n")
print("\n[","%.8f"%a11baru2," %.8f"%a12baru2," %.8f"%a13baru2,"]","[",a14baru3,"  ",a15baru3  ,"  ",a16baru3,"]","\t\t[","%.8f"%cosbaru2,"]\n")
print("[","%.8f"%a21baru2," %.8f"%a22baru2," %.8f"%a23baru2,"]","[",a24baru3,"  ",a25baru3  ,"  ",a26baru3,"]","\t[","%.8f"%cos1baru2,"]\n")
print("[","%.8f"%a31baru2," %.8f"%a32baru2," %.8f"%a33baru2,"]","[",a34baru3,"  ",a35baru3  ,"  ",a36baru3,"]","\t\t[","%.8f"%cos2baru2,"]\n")

#LANGKAH 5
#normalisasi baris 3 dibagi dengan a33
a31baru3=a31baru2/a33baru2
a32baru3=a32baru2/a33baru2
a33baru3=a33baru2/a33baru2
a34baru4=a34baru3/a33baru2
a35baru4=a35baru3/a33baru2
a36baru4=a36baru3/a33baru2
cos2baru3=cos2baru2/a33baru2
#baris pertama = a13 *persamaan ternormalisasi
a11baru3=a13baru2*a31baru3
a12baru3=a13baru2*a32baru3
a13baru3=a13baru2*a33baru3
a14baru4=a13baru2*a34baru4
a15baru4=a13baru2*a35baru4
a16baru4=a13baru2*a36baru4
cosbaru3=a13baru2*cos2baru3
#baris 2 = a23*persamaan ternormalisasi
a21baru3=a23baru2*a31baru3
a22baru3=a23baru2*a32baru3
a23baru3=a23baru2*a33baru3
a24baru4=a23baru2*a34baru4
a25baru4=a23baru2*a35baru4
a26baru4=a23baru2*a36baru4
cos1baru3=a23baru2*cos2baru3

print("\n\n==LANGKAH 5==\n")
print("\n[","%.8f"%a11baru3," %.8f"%a12baru3," %.8f"%a13baru3,"]","[",a14baru4,"  ",a15baru4  ,"  ",a16baru4,"]","\t\t[","%.8f"%cosbaru3,"]\n")
print("[","%.8f"%a21baru3," %.8f"%a22baru3," %.8f"%a23baru3,"]","[",a24baru4,"  ",a25baru4  ,"  ",a26baru4,"]","\t[","%.8f"%cos1baru3,"]\n")
print("[","%.8f"%a31baru3," %.8f"%a32baru3," %.8f"%a33baru3,"]","[",a34baru4,"  ",a35baru4  ,"  ",a36baru4,"]","\t\t[","%.8f"%cos2baru3,"]\n")

#LANGKAH 6
#baris pertama =baris langkah4-baris 1 langkah 5
a11baru4=a11baru2-a11baru3
a12baru4=a12baru2-a12baru3
a13baru4=a13baru2-a13baru3
a14baru5=a14baru3-a14baru4
a15baru5=a15baru3-a15baru4
a16baru5=a16baru3-a16baru4
cosbaru4=cosbaru2-cosbaru3
#bariske 2 = baris 2angkah4-baris 2 langkah 5
a21baru4=a21baru1-a21baru3
a22baru4=a22baru1-a22baru3
a23baru4=a23baru1-a23baru3
a24baru5=a24baru2-a24baru4
a25baru5=a25baru2-a25baru4
a26baru5=a26baru2-a26baru4
cos1baru4=cos1baru1-cos1baru3
#baris 3 = baris 3 langkah 5
a31baru4=a31baru3
a32baru4=a32baru3
a33baru4=a33baru3
a34baru5=a34baru4
a35baru5=a35baru4
a36baru5=a36baru4
cos2baru4=cos2baru3
print("\n\n==LANGKAH 6==\n")
print("\n[","%.8f"%a11baru4," %.8f"%a12baru4," %.8f"%a13baru4,"]","[",a14baru5,"  ",a15baru5  ,"  ",a16baru5,"]","\t","[X]","\t[","%.8f"%cosbaru4,"]\n")
print("[","%.8f"%a21baru4," %.8f"%a22baru4," %.8f"%a23baru4,"]","[",a24baru5,"  ",a25baru5  ,"  ",a26baru5,"]","\t","[Y]","\t[","%.8f"%cos1baru4,"]\n")
print("[","%.8f"%a31baru4," %.8f"%a32baru4," %.8f"%a33baru4,"]","[",a34baru5,"  ",a35baru5  ,"  ",a36baru5,"]","\t","[Z]","\t[","%.8f"%cos2baru4,"]\n")

print("\n==Pembuktian nilai X,Y,Z ke dalam persamaan==\n")
hasilnya=(b*cosbaru4)+(d*cos1baru4)+(kamu*cos2baru4)
hasilnya1=(f*cosbaru4)+(h*cos1baru4)+(kamu1*cos2baru4)
hasilnya2=(j*cosbaru4)+(l*cos1baru4)+(kamu2*cos2baru4)
print("Hasil persamaan 1 = %f"%hasilnya)
print("Hasil persamaan 2 = %f"%hasilnya1)
print("Hasil persamaan 3 = %f"%hasilnya2)


