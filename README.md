# **Submission Akhir: Menyelesaikan Permasalahan Institusi Pendidikan**

## **Business Understanding**
Jaya Jaya Institut adalah sebuah lembaga pendidikan tinggi yang telah beroperasi sejak tahun 2000. Selama bertahun-tahun, institusi ini telah menghasilkan banyak lulusan berkualitas dengan reputasi yang membanggakan. Namun, terdapat pula sejumlah mahasiswa yang tidak berhasil menyelesaikan studi mereka dan memilih untuk keluar (dropout).

Tingkat dropout yang cukup tinggi ini menjadi salah satu tantangan besar bagi keberlangsungan dan citra institusi. Untuk itu, Jaya Jaya Institut ingin segera mengidentifikasi mahasiswa yang berpotensi dropout, sehingga mereka dapat diberikan intervensi dan pendampingan lebih awal.

Sebagai seorang calon data scientist, Anda diberi kesempatan untuk membantu menangani permasalahan ini. Pihak institut telah menyediakan dataset yang dapat Anda unduh melalui tautan: students' performance. Selain itu, mereka juga meminta Anda untuk membangun dashboard yang memudahkan dalam analisis data serta pemantauan kinerja mahasiswa.

### **Permasalahan Bisnis**
Permasalahan yang perlu diselesaikan dalam proyek ini meliputi:

- **Berapa persentase mahasiswa di Jaya Jaya Institut yang mengalami dropout?**

- **Faktor-faktor apa saja yang mempengaruhi keputusan mahasiswa untuk dropout?**

### **Cakupan Proyek**
Pekerjaan yang harus dilakukan dalam proyek ini antara lain:

- **Data Preparation:** Menyiapkan dan membersihkan data untuk analisis lebih lanjut.

- **Data Understanding:** Memahami struktur dan karakteristik data.

- **Exploratory Data Analysis (EDA):** Mengeksplorasi data untuk menemukan pola atau anomali.

- **Visualisasi Data di Jupyter Notebook:** Membuat grafik dan visualisasi untuk memperjelas temuan.

- **Data Preprocessing dan Train-Test Split:** Menyiapkan data untuk proses pelatihan model.

- **Pemodelan Machine Learning:** Membuat model prediktif untuk memperkirakan kemungkinan mahasiswa dropout.

- **Evaluasi Model:** Menilai performa model menggunakan metrik evaluasi yang sesuai.

- **Simpan Model dan Deploy Lokal:** Menyimpan model yang sudah dilatih dan membuat aplikasi sederhana menggunakan Streamlit (app.py).

- **Pembuatan Dashboard Bisnis dengan Metabase:** Membuat dashboard interaktif untuk analisis data.

- **Deploy Streamlit App ke Streamlit Community Cloud:** Mempublikasikan aplikasi agar dapat diakses secara online.

### **Persiapan**
Dataset yang digunakan dalam proyek ini diambil dari Dicoding dan dapat diunduh melalui tautan berikut:

Sumber data: [Students' Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:


**1. Membuat virtual environment baru dengan nama venv:**
```
python -m venv venv
```
**2. Mengaktifkan virtual environment:**
- Untuk pengguna Windows
```
.\venv\Scripts\activate
```
- Untuk pengguna MacOS/Linux:
```
source venv/bin/activate
```
**3. Menginstal semua package yang diperlukan dari file requirements.txt:**
```
pip install -r requirements.txt
```

## **Business Dashboard**
Dashboard dikembangkan menggunakan platform Metabase, dengan koneksi database yang terintegrasi melalui PostgreSQL. Untuk kebutuhan hosting database, digunakan layanan [Supabase](https://supabase.com/), yang menyediakan solusi backend berbasis cloud untuk penyimpanan dan manajemen data secara real-time. 

Anda dapat mngakses dashboarnya pada link berikut: [Dashboard](http://localhost:3000/public/dashboard/a16347ff-dbfd-47ad-88b2-00d73ac751f3)

![image](https://s4.gifyu.com/images/bL04S.jpg)

![Image](https://s4.gifyu.com/images/bL06D.png)

Di bagian bawah judul terdapat keterangan atau card yang menampilkan indikator penting seperti:

- Dropout Rate: sebesar 32,12%.

- Total Students: sebanyak 4.424 siswa.

- Average Age: rata-rata usia siswa adalah 23,27 tahun.

- Maximum Age: usia siswa tertua adalah 70 tahun.

- Minimum Age: usia siswa termuda adalah 17 tahun.

Keterangan-keterangan tersebut bersifat dinamis dan dapat berubah berdasarkan filter yang digunakan dalam dashboard. Di bawah keterangan tersebut, terdapat tujuh grafik sebagai berikut:

**1. Diagram pie Tuition Fees Up To Date Distribution**

Menunjukkan distribusi siswa berdasarkan status pembayaran biaya pendidikan.

Kategori:

- True (88%): siswa yang membayar biaya pendidikan tepat waktu.

- False (12%): siswa yang belum membayar biaya pendidikan.

**2. Diagram pie Student Status Distribution**

Menampilkan persentase status siswa:

- Graduate (49,9%)

- Dropout (32,1%)

- Enrolled (17,9%)

**3. Diagram batang Average Grade Per Semester**

- Menampilkan rata-rata nilai semester 1 dan semester 2 berdasarkan status siswa (Graduate, Dropout, Enrolled).

- Terlihat adanya perbedaan performa akademik antar kelompok status.

**4. Diagram batang Scholarship Holder by Status**

- Menampilkan jumlah penerima beasiswa berdasarkan status siswa.

- Siswa yang lulus (Graduate) memiliki jumlah penerima beasiswa terbanyak dibandingkan siswa dropout maupun enrolled.

**5. Diagram batang Age Distribution vs Dropout**

- Menunjukkan distribusi usia siswa dan kaitannya dengan status siswa (Dropout, Enrolled, Graduate).

- Kelompok usia 17-20 tahun mendominasi populasi mahasiswa.

**6. Diagram batang Gender vs Status**

- Menampilkan distribusi jumlah siswa berdasarkan gender (Female dan Male) terhadap status siswa (Dropout, Enrolled, Graduate).

- Terdapat ketimpangan jumlah antara laki-laki dan perempuan di beberapa status.

**7. Diagram batang Dropout Based on Course Category**

Menampilkan jumlah siswa dropout dan lulus berdasarkan kategori jurusan:

- Business & Management

- Health Science

- Science & Technology

- Social Science

Terdapat perbedaan tingkat dropout antar kategori jurusan.

## **Menjalankan Sistem Machine Learning**
Langkah-langkah menggunakan sistem machine learning berbasis random forest adalah sebagai berikut.

1. Untuk akses secara online, aplikasi Streamlit versi Cloud telah tersedia dan dapat digunakan melalui tautan berikut ini: [Streamlit](https://submission-akhir-penerapan-data-science.streamlit.app/)
2. jika mengaksesnya Secara offline, anda bisa melakukan beberapa tahapan berikut:
- Unduh atau clone repositori berikut:
```
git clone https://github.com/Aryadibelorerung/submission-akhir-penerapan-data-science.git
```
- Masuk ke direktori "submission data science"
```
cd submission-akhir-penerapan-data-science
```
- Lalu jalankan perintah "streamlit run app.py" pada terminal.
3. Setelah itu, halaman web akan otomatis terbuka di browser melalui alamat localhost.
4. Lengkapi seluruh data yang diminta untuk memprediksi kemungkinan seorang mahasiswa mengalami Dropout, dan pastikan setiap bagian terisi dengan benar.

## **Conclusion**
Di Jaya Jaya Institut, tingkat persentase mahasiswa yang mengalami Dropout (DO) mencapai 32,1%, yang mana angka ini relatif tinggi jika dibandingkan dengan tingkat kelulusan yang mencapai 49,9%.

**Mahasiswa yang mengalami Dropout cenderung memiliki:**

- Nilai akademik yang lebih rendah (Curricular_units_1st/2nd_sem_grade) dibandingkan dengan mahasiswa yang berhasil lulus atau masih terdaftar.

- Jumlah mata kuliah yang disetujui (approved) lebih sedikit.

- Tingkat partisipasi dalam evaluasi yang lebih rendah.

**Faktor Non-Akademik yang Mempengaruhi:**

- Pembayaran uang kuliah yang tepat waktu (Tuition_fees_up_to_date): Mahasiswa yang terlambat membayar uang kuliah lebih rentan untuk mengalami Dropout.

- Pemegang beasiswa (Scholarship_holder): Mahasiswa yang menerima beasiswa memiliki tingkat kelulusan yang lebih tinggi.

**Faktor Demografi:**

- Usia pada saat pendaftaran (Age_at_enrollment): Mahasiswa yang lebih muda cenderung lebih sukses dalam studi mereka, sementara mahasiswa yang lebih tua memiliki risiko lebih tinggi untuk mengalami Dropout.

- Jenis Kelamin (Gender): Tidak ditemukan perbedaan signifikan terkait tingkat Dropout berdasarkan jenis kelamin.

**Perbedaan antar Program Studi:**

Beberapa program studi, seperti Sosial & Teknologi, menunjukkan tingkat Dropout yang lebih tinggi, sedangkan program studi lain seperti Bisnis & Kesehatan menunjukkan tingkat kelulusan yang lebih baik.

### **Rekomendasi Action Items**

Berdasarkan hasil analisis, beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan pada Jaya Jaya Institut:

**1. Pendekatan Akademik: Program Bimbingan Khusus**

Fokuskan upaya pada mahasiswa dengan nilai rendah pada semester pertama, karena mereka memiliki risiko tinggi untuk Dropout. Tawarkan sesi bimbingan tambahan untuk mata kuliah yang memiliki tingkat kegagalan tinggi.

**2. Sistem Peringatan Dini**

Implementasikan machine learning untuk memprediksi mahasiswa yang berisiko Dropout berdasarkan kinerja di semester pertama. Kirimkan notifikasi kepada dosen atau wali apabila mahasiswa memiliki nilai di bawah ambang batas yang ditentukan.

**3. Bantuan Finansial**

Berikan prioritas kepada mahasiswa yang berasal dari keluarga kurang mampu (Debtor = 1) untuk menerima bantuan biaya kuliah. Sediakan opsi pembayaran biaya kuliah yang lebih fleksibel untuk meringankan beban finansial. Selain itu, jalin kerjasama dengan industri untuk menyediakan pekerjaan paruh waktu bagi mahasiswa yang membutuhkan.

**4. Meningkatkan Keterlibatan Mahasiswa**

Dorong partisipasi dalam evaluasi akademik, karena mahasiswa yang tidak mengikuti evaluasi cenderung lebih berisiko untuk Dropout. Tawarkan insentif seperti poin tambahan atau sertifikat untuk meningkatkan kehadiran dalam ujian.

**5. Program Peer Mentoring dan Komunitas Belajar**

Bentuk komunitas belajar dan program mentoring antar teman sebaya untuk meningkatkan motivasi mahasiswa agar lebih terlibat dan termotivasi dalam proses belajar mereka.

**6. Segmentasi Mahasiswa**

Kelompokkan mahasiswa berdasarkan tingkat risiko Dropout (rendah, sedang, tinggi), dan berikan pendekatan yang lebih spesifik sesuai dengan kategori tersebut. Dengan cara ini, Jaya Jaya Institut dapat mengurangi angka Dropout dan meningkatkan tingkat kelulusan mahasiswa.
