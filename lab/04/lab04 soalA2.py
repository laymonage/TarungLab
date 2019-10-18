jajan=input()
kata=input()
jumlah=0
indeks=0

while (kata.find(jajan)!=-1):
     indeks=kata.find(jajan)
     kata=kata[indeks+len(jajan):]
     jumlah=jumlah+1

print("Uang saku dipotong selama ",jumlah,"hari")

