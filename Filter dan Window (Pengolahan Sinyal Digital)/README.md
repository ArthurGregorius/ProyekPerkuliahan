# Filter dan Window

### Filter

Filter adalah alat yang digunakan untuk memanipulasi sinyal dengan cara melewatkan atau menolak komponen-komponen tertentu dari sinyal tersebut. Filter dapat digunakan untuk berbagai tujuan seperti:

1. Reduksi Noise: Menghilangkan atau mereduksi komponen noise yang tidak diinginkan dari sinyal.
2. Pemisahan Komponen: Memisahkan komponen sinyal yang berbeda yang tumpang tindih dalam domain waktu atau frekuensi.
3. Emphasis Frekuensi: Memperjelas atau menekankan komponen frekuensi tertentu dalam sinyal.
4. Penghalusan Sinyal: Meratakan atau menghaluskan sinyal dengan menghapus fluktuasi cepat atau spike yang tidak diinginkan.

#### Jenis-jenis Filter:

Ada beberapa jenis filter yang umum digunakan dalam pengolahan sinyal digital:

1. **FIR (Finite Impulse Response)**:
   - Filter dengan respons impuls berhingga dalam jumlah sampel waktu.
   - Karakteristiknya ditentukan oleh koefisien yang tetap.
   - Umumnya lebih stabil dan lebih mudah diimplementasikan secara numerik.

2. **IIR (Infinite Impulse Response)**:
   - Filter dengan respons impuls yang dapat berlangsung dalam waktu tak terbatas.
   - Memiliki umpan balik yang dapat menyebabkan respons frekuensi yang lebih kompleks.
   - Dapat memperkenalkan resonansi atau osilasi jika tidak dirancang dengan hati-hati.

3. **Filter Linear dan Nonlinear**:
   - Filter linear mempertahankan sifat superposisi, sehingga outputnya adalah jumlah dari pengaruh setiap komponen masukan.
   - Filter nonlinear tidak mematuhi sifat superposisi.

### Window

Windowing adalah teknik yang digunakan dalam analisis sinyal untuk membatasi durasi sinyal dan mengurangi efek sisi dari sinyal tersebut. Ini dilakukan dengan mengalikan sinyal asli dengan fungsi window (jendela). Tujuan utama penggunaan window adalah untuk:

1. Mengurangi Efek Sisi: Mengurangi efek sisi atau distorsi yang muncul dalam hasil analisis sinyal akibat adanya tepian pada sinyal.
2. Membatasi Durasi: Memastikan bahwa analisis dilakukan pada bagian yang relevan dari sinyal dan mengurangi gangguan dari bagian sinyal yang tidak relevan.
3. Meminimalkan Aliasing: Meminimalkan efek aliasing yang terjadi saat sinyal yang dianalisis tidak representatif secara periodik.

#### Jenis-jenis Window:

Beberapa jenis fungsi window yang umum digunakan dalam pengolahan sinyal digital termasuk:

1. **Jendela Rektangular**: Sederhana, memberi bobot sama pada semua sampel dalam sinyal.
2. **Jendela Hamming**: Meningkatkan efisiensi dalam menekan sinyal tepian dengan mengurangi efek sisi.
3. **Jendela Hanning**: Mirip dengan Hamming, tetapi memiliki karakteristik yang sedikit berbeda dalam mengurangi efek sisi.
4. **Jendela Blackman**: Lebih kompleks daripada Hamming atau Hanning, memberikan kontrol yang lebih baik terhadap efek sisi.

### Penggunaan Bersama Filter dan Window:

Dalam banyak aplikasi, filter dan window sering digunakan bersama-sama. Misalnya, dalam analisis spektrum sinyal, sinyal sering kali di-window terlebih dahulu untuk meminimalkan efek tepian, kemudian filter FIR atau IIR dapat diterapkan untuk menekankan atau menolak komponen frekuensi tertentu. Dengan menggunakan teknik ini, informasi yang lebih baik dapat diekstraksi dari sinyal, dan efek dari tepian sinyal (seperti aliasing) dapat diminimalkan.
