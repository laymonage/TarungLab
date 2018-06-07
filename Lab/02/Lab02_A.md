# Soal Tutorial

## TIMEZONE

Pada suatu hari di sebuah tempat bermain impian yang telah terkenal hingga ke
seluruh penjuru samudera, TIMEZONE (Tarung Indonesia Memang Edan Zone),
terdapat seorang pendekar *games* bernama Fatih. Fatih memiliki ambisius yang tinggi
untuk menaklukkan segala *games* yang ada di *zone* tersebut. Di *zone* tersebut terdapat
empat mesin permainan yang akan ditaklukkan oleh Fatih. TIMEZONE memberikan
*tickets* untuk setiap mesin permainan yang dimainkan dengan batasan *highest score*
tertentu. Tickets tersebut dapat ditukarkan menjadi **Golden Coin**, **Silver Coin**, **Bronze 
Coin** dengan ketentuan :  

- **100 tickets = 1 Golden Coin**
- **10 tickets = 1 Silver Coin**
- **1 ticket = 1 Bronze Coin**

Fatih selalu mendapatkan *highest score* pada semua mesin permainan setiap kali ia
memainkan permainan - permainan tersebut. Kebetulan, kamu adalah seorang sahabat
baik Fatih dan ia rela membantu kamu untuk mendapatkan *coin-coin* tersebut sebanyak
yang kamu mau. Kamu dapat meminta Fatih untuk memainkan seluruh mesin
permainan tersebut sebanyak yang kamu inginkan. Akan tetapi, Fatih sangat lelah
untuk menghitung jumlah *tickets – tickets* yang ia dapatkan setiap ia bermain. Oleh
karena itu, bantulah Fatih dalam **menghitung banyak tickets yang didapatkan dari
permainan dan menghitung jumlah coin yang didapatkan dari total ticket tersebut
(diutamakan prioritas dari jenis coin yang terbesar Golden > Silver > Bronze).**

Berikut adalah mesin permainan yang dimiliki oleh TIMEZONE :
- Mesin permainan Bola Basket @Highest Score = 42 tickets 
- Mesin permainan Bowling @Highest Score = 60 tickets
- Mesin permainan Dino Duel @Highest Score = 87 tickets
- Mesin permainan DanceDance Revolution @Highest Score = 103 tickets

### Test Case 1:
#### Input:

> Bermain mesin permainan Bola Basket : **1**\
> Bermain mesin permainan Bowling: **2**\
> Bermain mesin permainan Dino Duel: **3**\
> Bermain mesin permainan DanceDance Revolution: **4**

➔ Keterangan : Angka yang dicetak tebal hanya bertujuan untuk menunjukkan
bahwa angka tersebut merupakan input dari user .

#### Output:
> Fatih berhasil mengumpulkan sebanyak 8 Golden Coin, 3 Silver Coin dan 5 Bronze
> Coin.

### Test Case 2:
#### Input:

> Bermain mesin permainan Bola Basket : **6**\
> Bermain mesin permainan Bowling: **3**\
> Bermain mesin permainan Dino Duel: **4**\
> Bermain mesin permainan DanceDance Revolution: **2**

#### Output:

> Fatih berhasil mengumpulkan sebanyak 9 Golden Coin, 8 Silver Coin dan 6 Bronze
> Coin.
  
---
## HADIAH FATIH
<sub><sup>Silakan dikerjakan jika soal utama sudah selesai.</sup></sub>

Setelah menghitung jumlah *coin* tersebut, akhirnya kamu memutuskan untuk
menukarkan *coin* dengan hadiah yang akan kamu berikan untuk Fatih sebagai tanda
terima kasih. Namun, sayangnya tidak semua *coin* dapat ditukarkan menjadi hadiah.
Syarat penukaran hadiah antara lain :

- **Golden coin** hanya dapat ditukarkan jika jumlah *golden coin* tersebut lebih dari 10.
- **Silver coin** hanya dapat ditukarkan jika jumlah *silver coin* tersebut genap
- **Bronze coin** tidak memiliki persyaratan untuk dapat ditukarkan.

Kamu cukup menambahkan pada output coin apa saja yang bisa kamu tukarkan
dengan hadiah.

### Test Case 1:
#### Input:

> Bermain mesin permainan Bola Basket : **3**\
> Bermain mesin permainan Bowling: **5**\
> Bermain mesin permainan Dino Duel: **4**\
> Bermain mesin permainan DanceDance Revolution: **3**

#### Output:
> Fatih berhasil mengumpulkan sebanyak 10 Golden Coin, 8 Silver Coin 
> dan 3 Bronze Coin.\
> Anda tidak dapat menukarkan Golden Coin anda.\
> Anda dapat menukarkan Silver Coin anda.\
> Anda dapat menukarkan Bronze Coin anda.

### Test Case 2:
#### Input:

> Bermain mesin permainan Bola Basket : **1**\
> Bermain mesin permainan Bowling: **3**\
> Bermain mesin permainan Dino Duel: **9**\
> Bermain mesin permainan DanceDance Revolution: **5**

#### Output:

> Fatih berhasil mengumpulkan sebanyak 15 Golden Coin, 2 Silver Coin dan 0 Bronze
> Coin.\
> Anda dapat menukarkan Golden Coin anda.\
> Anda dapat menukarkan Silver Coin anda.\
> Anda tidak memiliki Bronze Coin.

<br>

<p style="text-align: center; font-size: 1.5em;"><strong>SELAMAT MENGERJAKAN
DAN HAPPY CODING 😊</strong></p>

<br>

**PKF - HFZ - RCF - WR**

---

Diambil dari `Soal Tutorial Lab 2 - Kelas A.pdf` (Tutorial Lab 2 DDP1 A --
6 September 2017)

