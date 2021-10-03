
# metode Bisection
print('Program Mencari Akar Persamaan Nonlinear ')
print('\t','\t','\t','\t','oleh')
print('\t','\t','\t',' Iren Brigita Pasu')
print('\t','\t','\t',' NIM: 231-18-008')
print()
print()
print('(2-0,AB*x)/x\n\n')

a = input('Masukkan nilai AB : ')
AB = int(a)
b = input('Masukkan nilai xi : ')
xi= float(b)
c = input('Masukkan nilai xu : ')
xu= float(c)


#Ditanya : akar dari persamaan menggunakan metode regulafalsi
print("-"*70 + "Metode Regulafalsi" + "-"*70)
p = input('Masukkan Berapa kali iterasi yang diinginkan : ')
x = int(p)

# Jawab :
print ('iterasi      xi\t\t\txu\t    \tf(xi)\t\t\tf(xu)\t\t   xr\t    \t\tf(xr)\t\tf(xi)*f(xr)\t\tEA') 
for i in range(x):
    i+=1
    fxi=(2-(AB/100)*xi)/xi
    fxu=(2-(AB/100)*xu)/xu
    xr=xu-((fxu*(xi-xu))/(fxi-fxu))
    fxr=(2-(AB/100)*xr)/xr
    akar=fxi*fxr
    if i==1 :
        print(" ",i,'\t%.8f'%xi,'     ','%.8f'%xu,'     ','%.12f'%fxi,'     ','%.12f'%fxu,'     ' ,'%.8f'%xr,'     ','%.12f'%fxr,'     ','%.12f'%akar)
        if akar<0.000000000000:
            xu=xr
        elif akar>0.000000000000:
            xi=xr
        continue
    if x>1 :
        EA=abs((xr-xr)/xr)*100
        print(" ",i,'\t%.8f'%xi,'     ','%.8f'%xu,'     ','%.12f'%fxi,'     ','%.12f'%fxu,'     ','%.8f'%xr,'     ' ,'%.12f'%fxr,'     ','%.12f'%akar,'     %.12f'%EA)
        if akar<0.000000000000:
            xu=xr
        elif akar>0.000000000000:
            xi=xr

        
