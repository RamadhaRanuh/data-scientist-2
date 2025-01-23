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
        user="postgres.hdpjyjyaeyxjddqdxged",
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

URL = "postgresql://postgres.hdpjyjyaeyxjddqdxged:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

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

![I Gusti Bagus Ramadha Saverian Ranuh-dashboard](https://github.com/user-attachments/assets/52565332-56ec-47f6-a4ba-0feb7e2f34c4)


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
  - Dropout: **> 1,400 siswa**.  
  - Enrolled (masih aktif): **< 1,000 siswa**.  
  - Graduate (lulus): **> 2,000 siswa**.  
  - Dropout mencapai lebih dari **30% dari total siswa**, yang menjadi perhatian utama institusi ini.  
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
  - Dropout: **< 0.7**.  
  - Enrolled: **0.9**.  
  - Graduate: **> 0.9**.  
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

### **Langkah-Langkah Deployment Sistem Machine Learning Menggunakan Streamlit Community Cloud**

#### Menjalankan Sistem di Environment Lokal Streamlit
1. Menyimpan model Logistic Regression yang telah dilatih

```python
joblib.dump(model, "sample_data/lr_model.joblib")
```
2. Instalasi Streamlit ke dalam environment

```python
!pip install streamlit -q
```

3. Memdapatkan alamat IP lokal

```python
!wget -q -O - ipv4.icanhazip.com
```

4. Menjalankan aplikasi streamlit di lokal

```python
! streamlit run app.py & npx localtunnel --port 8501
```

### Melakukan Deployment di Streamlit Community Cloud
1. Persiapan File dan Repository GitHub

- Pastikan file app.py (kode aplikasi) dan requirements.txt (dependensi) telah dibuat. Tambahkan file ini ke repository menggunakan Git:

```Command
git add app.py requirements.txt
git commit -m "push the application"
git remote add origin https://github.com/RamadhaRanuh/data-scientist-2
git push origin master
```

File requirements.txt:
```txt
joblib==1.4.2
numpy==1.26.4
pandas==2.2.2
scikit-learn==1.6.0
streamlit==1.41.1
```

2. Akses Streamlit Community Cloud
- Buka Streamlit Community Cloud

![Screenshot 2025-01-23 153751](https://github.com/user-attachments/assets/8812140a-4c19-4daf-b028-7fb7be9db173)


- Login menggunakan akun github


3. Membuat Aplikasi Baru
- Klik tombol "Create App" di dashboard Streamlit.

![Screenshot 2025-01-23 153758](https://github.com/user-attachments/assets/d07a70e7-8648-4b02-84d3-aca80ed7566d)


- Isi data pada formulir "Deploy an app" dengan repository GitHub yang telah dibuat.

  ![Screenshot 2025-01-23 153850](https://github.com/user-attachments/assets/261f3abb-0389-4e1b-ae75-23cbd0f88821)

4. Proses Deployment
- Streamlit akan secara otomatis membangun aplikasi menggunakan dependensi yang terdapat dalam file requirements.txt dan menjalankan file app.py. Jika proses ini berhasil, Anda akan mendapatkan tautan untuk mengakses aplikasi.

5. Aplikasi yang Telah Terdeploy

- Aplikasi dapat diakses melalui link ini: [Aplikasi Streamlit](https://data-scientist-2-bjrkcolvbj9ykwuqghyce8.streamlit.app/)

- Raw link: https://data-scientist-2-bjrkcolvbj9ykwuqghyce8.streamlit.app/


## Conclusion
Proyek ini bertujuan untuk membantu PT Jaya Jaya Institute mengidentifikasi faktor-faktor yang menyebabkan siswa melakukan dropout dan memberikan rekomendasi berbasis data untuk mengurangi angka tersebut. Berdasarkan analisis data pada dashboard:

Angka Dropout Tinggi (lebih dari 30%)
Hampir seperempat dari total siswa mengalami dropout, yang menjadi tantangan utama bagi institusi.

Faktor-Faktor Risiko Dropout:
- Kinerja akademik yang rendah (rata-rata satuan kurikulum hanya 5.9 pada semester kedua).
- Pembayaran biaya kuliah yang tertunda (hanya kurang dari 0.7 tuition fee dibandingkan lebih dari 0.9 tuition_fee pada siswa yang lulus).
- Persentase siswa yang memiliki utang lebih tinggi pada kelompok dropout.
- Kurangnya dukungan beasiswa pada siswa dropout (19.4% memiliki beasiswa dibandingkan dengan 61.8% pada siswa lulus).
- Siswa yang lebih tua saat mendaftar lebih rentan terhadap dropout (22.37 tahun rata-rata usia pendaftaran dibandingkan 21.78 tahun pada siswa lulus).

Kelebihan Institusi:
Tingkat kelulusan yang tinggi (sekitar 43% dari total siswa berhasil lulus).
Dukungan beasiswa terbukti berdampak positif terhadap keberhasilan akademik.

### Rekomendasi Action Items
Untuk menyelesaikan permasalahan dropout dan meningkatkan keberhasilan siswa, berikut adalah beberapa rekomendasi berbasis data:
1. Program Intervensi Dini untuk Siswa Risiko Tinggi

Identifikasi siswa dengan kinerja akademik rendah (satuan kurikulum di bawah rata-rata).
Berikan konseling akademik dan program tutoring untuk mendukung siswa yang struggling.
Pastikan siswa semester awal memiliki jadwal belajar yang terorganisasi dengan baik untuk meningkatkan capaian akademik.

2. Program Bantuan Keuangan dan Beasiswa

Tingkatkan jumlah siswa yang menerima beasiswa, terutama untuk siswa dari keluarga kurang mampu atau yang menunjukkan potensi risiko dropout.
Tawarkan skema pembayaran fleksibel untuk meringankan beban siswa yang memiliki keterlambatan pembayaran.

3. Monitoring dan Evaluasi Siswa Berisiko Tinggi

Bangun sistem monitoring berbasis data untuk mendeteksi siswa yang menunjukkan potensi dropout (usia lebih tua saat mendaftar, terlambat membayar, atau memiliki utang).
Adakan sesi konsultasi reguler dengan wali akademik untuk memantau perkembangan siswa.

4. Strategi Pendaftaran dan Seleksi Awal

Optimalkan proses pendaftaran untuk menarik siswa yang lebih muda (usia awal 20-an) dan memiliki potensi akademik tinggi.
Berikan edukasi awal tentang pentingnya menyelesaikan pendidikan secara tuntas, termasuk rencana jangka panjang setelah lulus.

5. Sistem Gamifikasi dan Reward untuk Meningkatkan Keterlibatan

Terapkan sistem penghargaan bagi siswa dengan capaian akademik baik atau ketepatan pembayaran biaya kuliah.
Gunakan dashboard untuk memberikan feedback transparan kepada siswa tentang performa akademik mereka secara berkala.
