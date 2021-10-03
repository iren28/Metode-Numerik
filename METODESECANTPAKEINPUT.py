
# metode SECANT
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
xi_1= float(b)
c = input('Masukkan nilai xi : ')
xi= float(c)



#Ditanya : akar dari persamaan menggunakan metode SECANT

print("="*40 + "Metode SECANT" + "="*40)
p = input('Masukkan Berapa kali iterasi yang diinginkan : ')
x = int(p)

# Jawab :
print ("iterasi\t     xi-1\t\txi\t\tf(Xi-1)\t\t\tf(xi)\t\txi+1\t\tEA") 
for i in range(x):
    i+=1
    fxi_1=(2-(AB/100)*xi_1)/xi_1
    fxi=(2-(AB/100)*xi)/xi
    xi1=xi-((fxi*(xi_1-xi))/(fxi_1-fxi))
    EA=abs((xi1-xi)/xi1)*100
    print(' ',i,'\t%.12f'%xi_1,'   %.12f   '%xi,'%.12f   '%fxi_1,'%.12f   '%fxi,'%.12f   '%xi1,'%.12f   '%EA)
    if (x>1):
        xi_1=xi
        xi=xi1
        

        
