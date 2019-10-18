file1 = input("Masukkan nama file 1: ")
file2 = input("Masukkan nama file 2: ")

input1 = open(file1,'r')
input2 = open(file2,'r')
output = open("output.txt",'w')

dicari= input1.read()
dicari=dicari.splitlines()
jajanan = input2.read()
jajanan = jajanan.split(' ')

for i in dicari:
  jumlah=0
  for j in jajanan:
    if(i==j):
      jumlah=jumlah+1
  if(jumlah==0):
   print("Tidak ada",i,"di dalam daftar belanja",file=output)
  else:
   print("Jumlah", i, "dalam daftar belanja adalah sebanyak", jumlah,"buah",file=output)
  
input1.close()
input2.close()
output.close()
