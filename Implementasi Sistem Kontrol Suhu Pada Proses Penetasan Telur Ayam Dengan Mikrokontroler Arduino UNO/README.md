# Implementasi Sistem Kontrol Suhu Pada Proses Penetasan Telur Ayam Dengan Mikrokontroler Arduino UNO

Penetasan telur ayam merupakan salah satu proses yang penting dalam industri peternakan ayam. Proses ini dapat dilakukan secara alami oleh induk ayam, tetapi juga dapat dilakukan secara buatan dengan menggunakan mesin penetas telur ayam. Pada proses penetasan telur ayam, suhu merupakan salah satu faktor yang penting. Suhu yang sesuai, yaitu 38,3°C hingga 39°C, diperlukan untuk perkembangan embrio telur ayam. Suhu yang terlalu rendah dapat menyebabkan embrio telur ayam tidak berkembang dengan baik, sedangkan suhu yang terlalu tinggi dapat menyebabkan embrio telur ayam mati.

Kondisi peternakan ayam saat ini masih banyak yang menggunakan sistem penetasan telur ayam secara tradisional. Sistem ini memiliki kelemahan, yaitu suhu di dalam mesin penetas telur ayam tidak dapat dikontrol secara akurat. Hal ini dapat menyebabkan kegagalan penetasan telur ayam. Kegagalan penetasan telur ayam dapat disebabkan oleh berbagai faktor, salah satunya adalah suhu yang tidak sesuai. Suhu yang terlalu rendah dapat menyebabkan embrio telur ayam tidak berkembang dengan baik, sedangkan suhu yang terlalu tinggi dapat menyebabkan embrio telur ayam mati. Oleh karena itu, diperlukan sistem kontrol suhu yang dapat menjaga suhu di dalam mesin penetas telur ayam tetap stabil pada rentang suhu yang sesuai. Sistem kontrol suhu dapat diimplementasikan dengan menggunakan berbagai metode, salah satunya dengan menggunakan mikrokontroler.

### Tujuan
Tujuan dari penelitian ini adalah untuk mengimplementasikan sistem kontrol suhu pada proses penetasan telur ayam dengan menggunakan mikrokontroler Arduino UNO R3. Sistem kontrol ini menggunakan sensor suhu Lm35 untuk mengukur suhu di dalam mesin penetas telur ayam. Data suhu yang diperoleh dari sensor kemudian diolah oleh mikrokontroler untuk menentukan tindakan yang harus diambil, yaitu menyalakan atau mematikan elemen pemanas.

### Dasar Teori
1. Suhu. Suhu merupakan salah satu faktor penting dalam proses penetasan telur ayam. Suhu yang ideal untuk perkembangan embrio ayam adalah antara 38,3°C dan 39°C. Suhu di luar rentang ini dapat menyebabkan kelainan embrio atau bahkan kematian. Metode penetasan telur ayam tradisional sering mengandalkan pengaturan suhu alami, yang dapat tidak dapat diandalkan dan menyebabkan fluktuasi suhu. Hal ini dapat mengakibatkan berkurangnya keberhasilan penetasan dan kualitas anak ayam yang buruk. Untuk mengatasi keterbatasan ini, sistem kontrol suhu otomatis telah dikembangkan menggunakan mikrokontroler. Sistem ini menggunakan sensor untuk memantau suhu di dalam mesin penetas telur dan mengontrol elemen pemanas untuk mempertahankan rentang suhu yang diinginkan.
2. Mikrokontroler. Mikrokontroler adalah komputer kecil yang dapat diprogram yang dapat digunakan untuk mengendalikan berbagai perangkat elektronik. Mikrokontroler sangat cocok untuk aplikasi kontrol suhu karena kemampuannya untuk:
- Mengukur suhu: Mikrokontroler dapat dihubungkan ke sensor suhu, seperti Lm35 , untuk mengukur suhu lingkungan dengan akurat.
- Memproses data: Mikrokontroler dapat menganalisis data suhu dan menentukan apakah perlu dilakukan penyesuaian. Mikrokontroler yang kami gunakan pada sistem kontrol ini adalah Arduino Uno.
- Mengontrol elemen pemanas: Mikrokontroler dapat mengirimkan sinyal untuk mengontrol elemen pemanas, menyalakannya atau mematikannya untuk mempertahankan suhu yang diinginkan. Pada sistem ini kamu menggunakan elemen pemanas berupa lampu pijar yang disambungkan ke relay agar dapat dikendalikan oleh mikrokontroler.
3. Arduino UNO. Arduino UNO adalah papan mikrokontroler yang populer dan mudah digunakan. Papan ini dirancang untuk pemula dan dapat digunakan untuk berbagai proyek elektronik, termasuk sistem kontrol suhu. Arduino Uno memiliki beberapa fitur utama, antara lain:
- Mikrokontroler ATmega328P
- 14 pin digital
- 6 pin analog
- Port USB
- Pin reset
- Pin GND
- Pin 5V

![Arduino_Uno_-_R3](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/8ccac93d-5d0f-470a-ab46-2323865fbffa)

4. Sensor Suhu (LM35). Sensor suhu LM35 adalah sensor suhu analog yang dapat digunakan untuk mengukur suhu dalam rentang -55°C hingga 150°C. Sensor ini memiliki output tegangan yang linier dengan suhu, yaitu 10 mV per derajat Celcius. Sensor suhu LM35 memiliki beberapa fitur utama, antara lain:
- Rentang suhu: -55°C hingga 150°C
- Output: 10 mV per derajat Celcius
- Tegangan operasi: 4,5 V hingga 20 V

![Gambar-931-Module-sensor-LM-35-LM35-adalah-sensor-suhu-yang-dapat-mengukur-suhu-pada](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/5e846df1-4378-4f02-8205-dcf17a693108)

5. Bola Lampu. Bola Lampu adalah alat yang dapat digunakan untuk menghasilkan panas. Bola lampu yang digunakan dalam sistem kontrol suhu umumnya adalah bola lampu pijar atau bola lampu halogen. Bola lampu pijar bekerja dengan memanaskan filamen tungsten hingga mencapai suhu yang tinggi. Filamen tungsten kemudian akan memancarkan panas ke lingkungan. Bohlam halogen bekerja dengan menggunakan gas halogen untuk meningkatkan suhu filamen tungsten. Filamen tungsten kemudian akan memancarkan panas ke lingkungan.

![lampu-pijar-vintage-model-bohlam-edison](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/71c1234d-2ee0-423e-91c6-46baa8f2467d)

6. Liquid Crystal Display (LCD). LCD adalah layar yang menggunakan teknologi kristal cair untuk menampilkan gambar. LCD yang digunakan dalam sistem kontrol suhu umumnya adalah LCD 16x2 atau LCD 20x4. LCD 16x2 memiliki 16 karakter per baris dan 2 baris. LCD 20x4 memiliki 20 karakter per baris dan 4 baris.

![f2da2ec1-c8d9-4f37-82a8-9414a06e04e2](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/95d66c44-bcb3-45ed-ae60-475ff3949944)

### Desain

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/da0a1627-184b-4405-b421-9f5d38b4229a)

Rancangan Desain Sistem


![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/0ea6b2fb-7904-43cc-8218-6eca7577001a)

Protoype Sistem

Tabel Komponen

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/d3ba491c-1063-4baf-a22a-1eb4632333db)

Cara Kerja
1. Arduino akan membaca nilai analog dari sensor suhu LM35 setiap 5 detik.
2. Nilai analog tersebut kemudian akan dikonversi ke suhu dalam derajat Celcius.
3. Jika suhu di bawah 37.5°C, maka Arduino akan menyalakan Relay untuk menaikkan suhu.
4. Jika suhu di atas 39.5°C, maka Arduino akan mematikan Relay untuk menurunkan suhu.

### Hasil dan Analisa

Dari sistem kontrol yang telah dirancang, hasil signifikan yang diperoleh yaitu, pertama, lampu pijar di dalam inkubator akan menyala ketika sensor suhu membaca nilai yang kurang atau sama dengan 37.5℃. Sebaliknya, lampu akan padam apabila suhu yang terdeteksi oleh sensor mencapai atau melebihi 39.5℃. Rentang suhu ideal yaitu antara 37.5℃ hingga 39.5℃, dianggap sebagai kondisi optimal untuk pengeraman telur ayam. Di luar rentang tersebut, baik suhu yang terlalu rendah maupun terlalu tinggi dapat menghambat proses pengeraman secara optimal. Penting untuk dicatat bahwa lampu memiliki delay selama 5 detik sebelum menyala atau padam setelah sensor membaca suhu. Keputusan ini diambil dengan tujuan agar panas dari lampu dapat merambat dan merubah temperatur di dalam kandang inkubator dengan lebih gradual.

Berdasarkan hasil dan analisis tersebut, dapat disimpulkan bahwa sistem kontrol suhu yang telah dirancang dapat beroperasi dengan baik dan memiliki potensi besar untuk memberikan manfaat yang signifikan bagi peternak ayam. Kemampuan sistem ini untuk menjaga suhu dalam rentang optimal, didukung oleh akurasi sensor, kinerja relay yang handal, dan tampilan suhu yang jelas pada LCD, menjadikan alat ini sebagai solusi yang efektif dan efisien dalam mendukung proses pengeraman telur ayam.

Tabel Pengujian Sistem
1. Pengujian pada kondisi siang hari (didalam ruangan)

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/a77b6f84-0de2-4604-95a8-70b4459e1921)

Pada pengujian pertama, sistem di uji pada kondisi siang hari di dalam kamar kos dengan kondisi ada satu kipas angina yang menyala sehingga suhu dalam ruangan tidak begitu panas.

2. Pengujian pada kondisi malam hari (didalam ruangan)

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/f6ba739f-913c-4cd2-a9ac-f81418b329e4)

Pada kondisi kedua, sistem di uji di dalam ruangan dalam kondisi malam hari sehabis hujan. Suhu terdeteksi lebih dingin dikarenakan suhu ruangan yang juga semakin dingin dikarenakan habis hujan.

3. Pengujian pada kondisi siang hari (di luar ruangan)

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/b49a935c-7ae8-4671-833d-899c6869257f)

Pada kondisi ketiga, sistem di uji di luar ruangan pada kondisi siang hari tepatnya sekitar jam 12 siang dimana suhu sekitar lebih panas karena terik matahari di daerah Semarang. Suhu yang terdeteksi cenderung stabil, hal ini dikarenakan suhu yang panas merupakan suhu yang efektif untuk proses pengeraman telur ayam.

4. Pengujian pada kondisi malam hari (di luar ruangan)

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/197994fe-0182-48f1-bb75-c6a764d3fd1c)

Pada kondisi keempat, sistem di uji di kondisi malam hari yang biasa (tidak ada hujan), namun suhu yang terdeteksi tetap terpengaruh karena kondisi diluar ruangan dimana langsung terasa dinginnya.

Proyek ini merupakan upaya yang inovatif dan relevan dalam pengembangan teknologi pertanian. Sistem ini dirancang untuk memberikan solusi otomatis dalam menjaga suhu optimal untuk pengeraman telur ayam, sebuah aspek kritis dalam keberhasilan penetasan dan kesehatan embrio. Melalui pembacaan suhu yang terus-menerus dari sensor LM35, sistem dapat
merespons perubahan suhu dengan cepat, memastikan bahwa kondisi ideal tetap terjaga.

Penggunaan lampu pijar sebagai elemen pemanas yang dikontrol oleh relay memberikan kontrol suhu yang lebih terukur dan tepat. Adanya delay 5 detik sebelum lampu menyala atau padam setelah pembacaan suhu bertujuan agar panas dapat merambat dengan lebih gradual di dalam inkubator. Selain itu, penggunaan LCD sebagai antarmuka pengguna memungkinkan pemantauan real-time suhu di dalam mesin penetas, memberikan transparansi dan kontrol langsung kepada pengguna. Optimasi integrasi dan interaksi antara mikrokontroler Arduino, sensor suhu LM35, lampu bohlam, serta LCD penting untuk mencapai suhu yang maksimal dalam sistem pengeraman telur ayam. Pemrograman yang cermat untuk pembacaan suhu, koordinasi efisien dengan relay untuk mengontrol lampu bohlam, dan integrasi LCD untuk tampilan informasi real-time. Interaksi yang baik antara mikrokontroler dan komponen lainnya memberikan stabilitas suhu yang diperlukan untuk keberhasilan pengeraman.

Analisis komponen sistem menunjukkan bahwa sensor suhu LM35 memiliki akurasi yang memadai, relay dapat diandalkan untuk mengontrol daya listrik pada lampu pijar, dan LCD memberikan informasi suhu yang jelas. Implementasi sistem kontrol suhu menggunakan mikrokontroler dapat signifikan meningkatkan efisiensi dalam proses penetasan telur ayam. Sistem ini memungkinkan pengawasan otomatis dan presisi terhadap suhu dalam inkubator, yang merupakan faktor kritis untuk keberhasilan penetasan. Mikrokontroler, seperti Arduino, membaca secara terus-menerus nilai suhu dari sensor LM35 dengan interval waktu yang singkat, memberikan respons cepat terhadap perubahan suhu.

Secara keseluruhan, proyek ini memberikan kontribusi positif terhadap efisiensi dan keberhasilan proses penetasan telur ayam. Sistem ini dapat dianggap sebagai solusi yang baik untuk mendukung kegiatan peternakan dengan teknologi yang canggih dan otomatis, meningkatkan peluang keberhasilan penetasan, serta memberikan manfaat bagi para peternak ayam dalam mengoptimalkan kondisi lingkungan inkubasi
