operasi = input("Masukkan operasi : ")

if (operasi=="PLUS"):
         N=input("Masukkan nilai N : ")
         M=input("Masukkan nilai M : ")
         print(int(N)+int(M))
elif (operasi=="MINUS"):
        N=input("Masukkan nilai N : ")
        M=input("Masukkan nilai M : ")
        if (int(N)<int(M)):
            print("Error!")
        else:
          print(int(N)-int(M))
else:
    N=input("Masukkan nilai N : ")
    prime=True
    for i in range(2,int(N)-1):
      if (int(N)%i == 0):
        prime=False
        break
      
    if (prime==True):
          print("Angka", N, "merupakan bilangan prima")
    else:
          print("Angka", N, "bukan merupakan bilangan prima")
          
