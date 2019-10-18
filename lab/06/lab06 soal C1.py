


def beli_coklat(jumlah_kecil,jumlah_sedang,jumlah_besar):
  harga_kecil=jumlah_kecil*5000
  harga_sedang=jumlah_sedang*8000
  harga_besar=jumlah_besar*12000
  if(jumlah_kecil!=0):
    print("Membeli coklat kecil sebanyak",jumlah_kecil,"seharga",harga_kecil)
  if(jumlah_sedang!=0):
    print("Membeli coklat sedang sebanyak",jumlah_sedang,"seharga",harga_sedang)
  if(jumlah_besar!=0):
    print("Membeli coklat besar sebanyak",jumlah_besar,"seharga",harga_besar)
  return (harga_kecil+harga_sedang+harga_besar)

def beli_mie(jumlah_single,jumlah_double):
  harga_single=jumlah_single*2500
  harga_double=jumlah_double*3500
  if(jumlah_single!=0):
    print("Membeli mie single sebanyak",jumlah_single,"seharga",harga_single)
  if(jumlah_double!=0):
    print("Membeli mie double sebanyak",jumlah_double,"seharga",harga_double)
  return (harga_single+harga_double)

def beli_roti_tawar(jumlah_biasa,jumlah_gandum,jumlah_kupas):
  harga_biasa=jumlah_biasa*12000
  harga_gandum=jumlah_gandum*15000
  harga_kupas=jumlah_kupas*13500
  if(jumlah_biasa!=0):
    print("Membeli roti biasa sebanyak",jumlah_biasa,"seharga",harga_biasa)
  if(jumlah_gandum!=0):
    print("Membeli roti gandum sebanyak",jumlah_gandum,"seharga",harga_gandum)
  if(jumlah_kupas!=0):
    print("Membeli roti kupas sebanyak",jumlah_kupas,"seharga",harga_kupas)
  return (harga_biasa+harga_gandum+harga_kupas)

def checkout(total_harga):
  print("Total belanja sebesar", total_harga)

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
