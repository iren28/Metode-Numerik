
# metode Netwon-Raphson
print('Program Mencari Akar Persamaan Nonlinear ')
print('\t','\t','\t','\t','oleh')
print('\t','\t','\t',' Iren Brigita Pasu')
print('\t','\t','\t',' NIM: 231-18-008')
print()
print()
print('(xi^3)-10*(xi^2)+AB')

a = input('Masukkan nilai AB : ')
AB = int(a)
b = input('Masukkan nilai xi : ')
xi= float(b)



#Ditanya : akar dari persamaan menggunakan metode NEWTON RAPHSON
print("="*40 + "Metode Newton Raphson" + "="*40)
p = input('Masukkan Berapa kali iterasi yang diinginkan : ')
x = int(p)

# Jawab :
print ("iterasi   xi\t\t  f(Xi)\t\t  f'(xi)\t  xi+1\t\t   EA") 
for i in range(x):
    i+=1
    fxi=(xi**3)-10*(xi**2)+AB
    fxiturunan = 3*(xi**2)-(20*xi)
    xi1=xi-(fxi/fxiturunan)
    EA=abs((xi1-xi)/xi1)*100
    
    print('  ',i,'\t%.7f'%xi,'\t%.7f'%fxi,'\t%.7f'%fxiturunan,'\t%.7f'%xi1,'\t%.7f'%EA)
    if (x>1):
        xi=xi1
        

        
