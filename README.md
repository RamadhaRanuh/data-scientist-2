# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan PT JAYA JAYA INSTITUTE

## Business Understanding

PT Jaya Jaya Institute adalah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000. Selama dua dekade terakhir, institusi ini telah menghasilkan banyak lulusan dengan reputasi yang sangat baik di dunia kerja. Namun, terdapat tantangan besar yang dihadapi oleh institusi ini, yaitu tingginya tingkat siswa yang tidak menyelesaikan pendidikan mereka alias dropout.

Masalah dropout ini memiliki dampak yang signifikan terhadap institusi, termasuk:

1. Reputasi Institusi: Tingginya angka dropout dapat menurunkan reputasi akademik di mata publik.
2. Efisiensi Operasional: Sumber daya yang dialokasikan untuk siswa yang akhirnya dropout menjadi kurang efisien.
3. Dampak Sosial: Dropout dapat mengurangi kontribusi lulusan terhadap masyarakat dan industri.

Agar dapat mengurangi angka dropout, Jaya Jaya Institute ingin memanfaatkan data yang ada untuk mendeteksi siswa-siswa yang berisiko tinggi melakukan dropout lebih dini. Dengan begitu, mereka dapat memberikan bimbingan khusus untuk membantu siswa menyelesaikan pendidikan mereka.

### Permasalahan Bisnis

Berdasarkan latar belakang tersebut, berikut adalah permasalahan bisnis yang perlu diselesaikan:

1. Mendeteksi Dini Risiko Dropout: Bagaimana cara memprediksi siswa yang memiliki risiko tinggi untuk dropout menggunakan data historis siswa?
2. Identifikasi Faktor Risiko: Apa saja faktor utama yang memengaruhi keputusan siswa untuk dropout?
3. Optimalisasi Sumber Daya Bimbingan: Bagaimana memastikan bimbingan khusus dapat diberikan kepada siswa yang paling membutuhkan berdasarkan hasil prediksi risiko dropout?
4. Pemantauan Performa Siswa: Bagaimana menyediakan alat atau dashboard yang intuitif bagi pihak manajemen untuk memonitor data performa siswa secara real-time?

### Cakupan Proyek

### Persiapan

#### Sumber Data: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

#### Setup Environment:

##### Metabase

1. Jalankan perintah berikut pada Terminal/Command Prompt/PowerShell guna memanggil (pull) Docker image untuk menjalankan Metabase.

```PowerShell
docker pull metabase/metabase:v0.46.4
```

2. Menjalankan image tersebut menggunakan perintah berikut.

```PowerShell
docker run -p 3000:3000 --name metabase metabase/metabase
```

3. Menjalankan URL `http://localhost:3000/setup` untuk masuk ke dalam metabase

4. Melakukan registrasi:
- email: root@mail.com
- password: root123

##### Supabase

1. **Menyiapkan environment proyek**

```python
pip install pandas sqlalchemy
```

2. **Menyiapkan Dataset**

```python
df = pd.read_csv('/content/sample_data/employee_data.csv', encoding = 'windows-1252')
```

3. **Membuat New Project di Supabase**

- Untuk proyek ini, saya akan menggunakan PostgreSQL sebagai DBMS dari database yang akan digunakan. 
Database akan dijalankan pada sebuah cloud bernama supabase.

- Login melalui tautan berikut: https://supabase.com/dashboard/sign-in.
- Jika proses login di atas berjalan dengan lancar, akan diarahkan ke halaman dashboard. Pada halaman dashboard, klik New Project.
- Lengkapi seluruh informasi yang dibutuhkan untuk membuat proyek baru (organization, name, database password, region, pricing plan) pada supabase. Lalu klik Create new project! 
- Tunggu sampai proses build selesai. Jika telah selesai, Anda bisa masuk ke Project setting.
- Pada halaman Project setting, klik Database.
- Pada halaman Database, Anda akan menemukan informasi yang dibutuhkan untuk menyambungkan Postgres database dengan metabase ataupun sqlalchemy.

4. **Melakukan Test koneksi ke dalam Supabase**

```python
# Test using psycopg2 directly first
import psycopg2

try:
    conn = psycopg2.connect(
        host="aws-0-ap-southeast-1.pooler.supabase.com",
        database="postgres",
        user="postgres.fvqiswwruzdsyzacpohl",
        password="password"
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection error: {e}")
```

5. **Mengirim dataset ke dalam database**
- Mengirim dataset yang sebelumnya telah kita unduh ke dalam database menggunakan library sqlalchemy. Untuk melakukannya, Anda membutuhkan DATABASE_URL yang disediakan oleh supabase.
```python
from sqlalchemy import create_engine

URL = "postgresql://postgres.fvqiswwruzdsyzacpohl:[password]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

engine = create_engine(URL)
df.to_sql('orders', engine)
```

- Saya menggunakan koneksi `Transaction Pooler` agar bisa membuat multiple connection dengan lancar.
- Jika proses di atas berjalan dengan lancar, Anda akan menemukan tampilan seperti berikut pada halaman Tabel editor.

##### Menggabungkan Metabase dengan Supabase

1. Masuk ke Metabase

```PowerShell
docker run -p 3000:3000 --name metabase metabase/metabase
```
- Setelah menjalankan perintah tersebut, dapat menggunakan URL berikut: http://localhost:3000/setup 

2. Klik bagian Settings dan masuk ke bagian Admin settings.
3. Pada halaman Admin setting, masuk ke bagian Database dan klik Add database.
4. Tahap berikutnya adalah lengkapi informasi konfigurasi dari database yang sebelumnya telah Anda buat. 
Parameter:
- host: aws-0-ap-southeast-1.pooler.supabase.com
- port: 6543
- database: postgres
- user: postgres.hdpjyjyaeyxjddqdxged
5. Jika proses di atas berjalan dengan lancar, maka database pada supabase sudah terhubung ke metabase.

## Business Dashboard

Dari **business dashboard** yang telah dibuat di atas, berikut adalah penjelasan rinci dan detail berdasarkan setiap visualisasi yang tersedia:

---

### **1. Gender Distribution**  
- **Komposisi Gender:**  
  - Female: **64.8%**  
  - Male: **35.2%**  
  - Hal ini menunjukkan bahwa mayoritas siswa di PT Jaya Jaya Institute adalah perempuan.

---

### **2. Total Students and Average Age of Enrollment**  
- **Jumlah Total Siswa:** **4,424 siswa**.  
  - Ini merupakan jumlah keseluruhan siswa, baik yang sedang aktif belajar, telah lulus, maupun yang dropout.  
- **Rata-rata Usia Pendaftaran:** **23.27 tahun**.  
  - Siswa cenderung mendaftar di usia awal 20-an, yang sesuai dengan profil mahasiswa perguruan tinggi pada umumnya.

---

### **3. Marital Status Distribution**  
- **Status Perkawinan Siswa:**  
  - Single: **88.58%** (mayoritas).  
  - Married: **8.57%**.  
  - Other: **2.85%**.  
  - Mayoritas siswa berstatus belum menikah, sesuai dengan profil umum siswa yang mendaftar di usia muda.

---

### **4. Count for Each Status**  
- **Distribusi Status Siswa:**  
  - Dropout: **1,000 siswa**.  
  - Enrolled (masih aktif): **1,500 siswa**.  
  - Graduate (lulus): **1,924 siswa**.  
  - Dropout mencapai hampir **23% dari total siswa**, yang menjadi perhatian utama institusi ini.  
  - Graduate mendominasi, menunjukkan keberhasilan akademik, namun angka dropout tetap tinggi.

---

### **5. Average Curricular Unit Approved (Semester 2)**  
- **Rata-rata Satuan Kurikulum yang Disetujui:**  
  - Dropout: **5.9** satuan.  
  - Enrolled: **11.12** satuan.  
  - Graduate: **12.7** satuan.  
  - Tren menunjukkan bahwa semakin tinggi rata-rata satuan kurikulum yang disetujui, semakin kecil risiko dropout, dan siswa lebih mungkin lulus.  
  - Siswa dropout memiliki kinerja akademik yang sangat rendah dibandingkan dengan yang lainnya.

---

### **6. Tuition Fees and Scholarship by Status**  
- **Rata-rata Biaya Kuliah yang Terbayar:**  
  - Dropout: **IDR 0.6 juta**.  
  - Enrolled: **IDR 1.0 juta**.  
  - Graduate: **IDR 1.5 juta**.  
  - Siswa yang lulus cenderung lebih disiplin dalam membayar biaya kuliah dibandingkan yang dropout.  
- **Rata-rata Beasiswa yang Dimiliki:**  
  - Dropout: **19.4% memiliki beasiswa**.  
  - Graduate: **61.8% memiliki beasiswa**.  
  - Beasiswa tampaknya berperan signifikan dalam mendukung siswa untuk menyelesaikan pendidikan.

---

### **7. Application Mode by Status**  
- **Rata-rata Mode Aplikasi:**  
  - Dropout: **7.5** (mode aplikasi lebih rendah).  
  - Graduate: **12.5** (mode aplikasi lebih tinggi).  
  - Siswa yang memiliki aplikasi dengan lebih banyak kelengkapan atau proses aplikasi yang lebih intensif cenderung memiliki tingkat kelulusan yang lebih tinggi.

---

### **8. Debtor and Age at Enrollment by Status**  
- **Rata-rata Debtor (utang):**  
  - Dropout: **25% siswa memiliki utang**.  
  - Graduate: **4.6% siswa memiliki utang**.  
  - Siswa dropout memiliki kecenderungan lebih tinggi untuk memiliki utang, yang mungkin menjadi faktor risiko dropout.  
- **Rata-rata Usia Pendaftaran:**  
  - Dropout: **22.37 tahun**.  
  - Graduate: **21.78 tahun**.  
  - Siswa dropout sedikit lebih tua dibandingkan dengan yang lulus, yang dapat menjadi faktor tambahan risiko dropout.

---

### **Kesimpulan Utama**  
1. **Faktor Risiko Dropout:**
   - Kinerja akademik rendah (rata-rata satuan kurikulum).
   - Keterlambatan pembayaran biaya kuliah.
   - Kurangnya beasiswa.
   - Kecenderungan memiliki utang.

2. **Peluang untuk Intervensi:**
   - Memberikan dukungan akademik dan konseling kepada siswa yang memiliki satuan kurikulum rendah.  
   - Program bantuan beasiswa dan strategi pembayaran biaya kuliah fleksibel.  
   - Monitoring lebih ketat untuk siswa dengan utang dan usia pendaftaran lebih tua.  

Dashboard ini memberikan wawasan yang komprehensif bagi manajemen PT Jaya Jaya Institute untuk menyusun strategi intervensi guna mengurangi angka dropout dan meningkatkan efisiensi akademik.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
