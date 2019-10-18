import bennymart.py

input1=0
harga_coklat=0
harga_mie=0
harga_roti=0
while(input1!="exit"):
  input1=input()
  if(input1=="exit"):
    break
  input1=input1.split(' ')
  if(input1[1]=="coklat"):
    harga_coklat=beli_coklat(int(input1[2]),int(input1[3]),int(input1[4]))
  elif(input1[1]=="mie"):
    harga_mie=beli_mie(int(input1[2]),int(input1[3]))
  elif(input1[1]=="roti"):
    harga_roti=beli_roti_tawar(int(input1[2]),int(input1[3]),int(input1[4]))

checkout(harga_coklat+harga_mie+harga_roti)
