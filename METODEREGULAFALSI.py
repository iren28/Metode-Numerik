
# metode regulafalsi
print('\t\t\t\t\t\t\tProgram Mencari Akar Persamaan Nonlinear ')
print('\t\t\t\t\t\t\t\t\t','oleh')
print('\t\t\t\t\t\t\t\t',' Iren Brigita Pasu')
print('\t\t\t\t\t\t\t\t',' NIM: 231-18-008')
print()
print()
print('(2-0,AB*x)/x')

AB=8
xi=24
xu=25.5
print('xi = ',xi,'xu = ',xu,'\n\n')

#Ditanya : akar dari persamaan menggunakan metode regulafalsi
print("-"*70 + "Metode Regulafalsi" + "-"*70)
p = input('Masukkan Berapa kali iterasi yang diinginkan : ')
x = int(p)

# Jawab :
fxi=(2-(AB/100)*xi)/xi
fxu=(2-(AB/100)*xu)/xu
xr=xu-((fxu*(xi-xu))/(fxi-fxu))
fxr=(2-(AB/100)*xr)/xr
akar=fxi*fxr
print ('iterasi       xi\t\txu\t\tf(xi)\t\t     f(xu)\t\t     xr\t\t\tf(xr)\t\t   f(xi)*f(xr)\t        EA')
print("",'\t%.8f'%xi,'     ','%.8f'%xu,'     ','%.12f'%fxi,'     ','%.12f'%fxu,'     ' ,'%.8f'%xr,'     ','%.12f'%fxr,'     ','%.12f'%akar)
s=xr
for i in range(x):
    i+=1
    fxi2=(2-(AB/100)*xi)/xi
    fxu2=(2-(AB/100)*s)/s
    xr2=s-((fxu2*(xi-s))/(fxi2-fxu2))
    fxr2=(2-(AB/100)*xr2)/xr2
    akar2=fxi*fxr
    if akar<0 :
        EA=abs((xr2-s)/xr)*100
        print(" ",i,'\t%.8f'%xi,'     ','%.8f'%s,'     ','%.12f'%fxi2,'     ','%.12f'%fxu2,'     ','%.8f'%xr2,'     ' ,'%.12f'%fxr2,'     ','%.12f'%akar2,'     %.12f'%EA)
        if akar2<0.000000000000:
            s=xr2
        elif akar2>0.000000000000:
            xi=xr2

        
