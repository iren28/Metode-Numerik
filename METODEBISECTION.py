# metode Bisection
print('\t\t\t\t\t\t\tProgram Mencari Akar Persamaan Nonlinear\n')
print('Soal \n\tF(X)=(2-0,AB*x)/x')
print('AB = Nomor registrasi terakhir\n')
AB=8
xi=24
xu=25.5
print('AB = ',AB,'xi = ',xi,'xu = ',xu,'\n\n')

#Ditanya : akar dari persamaan menggunakan metode bisection
print("-"*70 + "Metode bisection" + "-"*70)
p = input('Masukkan Berapa kali iterasi yang diinginkan : ')
x = int(p)

# Jawab :
print ('iterasi\txi\t\t\txu\t\txr\t\tf(xi)\t\t\t     f(xr)\t\t  f(xi)*f(xr)\t\tEA')
xr=(xi+xu)/2
fxi=(2-(AB/100)*xi)/xi
fxu=(2-(AB/100)*xu)/xu
fxr=(2-(AB/100)*xr)/xr
akar=fxi*fxr
print('1','\t%.8f'%xi,'     ','%.8f'%xu,'     ','%.8f'%xr,'     ','%.12f'%fxi,'     ' ,'%.12f'%fxr,'     ','%.12f'%akar)
if akar<0.0:
    xu=xr
elif akar>0.0:
    s=xr
    
for i in range(x):
    i+=2
    xr2=(s+xu)/2
    fxi2=(2-(AB/100)*s)/s
    fxr2=(2-(AB/100)*xr2)/xr2
    akar2=fxi2*fxr2
    EA= abs ((xr2-s)/xr2)*100
    if akar>0 :
        print(i,'\t%.8f'%s,'     ','%.8f'%xu,'     ','%.8f'%xr2,'     ','%.12f'%fxi2,'     ' ,'%.12f'%fxr2,'     ','%.12f'%akar2,'     %.12f'%EA)
        if akar2<0.0:
            xu=xr2
        elif akar2>0.0:
            s=xr2
