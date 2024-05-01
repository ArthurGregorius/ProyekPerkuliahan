# Perancangan Security System dan Monitoring Berbasis Microcontroller ESP32-DOIT

Pada zaman modern ini, security (keamanan) adalah hal yang paling penting dan hal yang krusial untuk diperhatikan, baik dalam lingkungan rumah, perkantoran, ataupun industri. Adanya keinginan untuk menciptakan lingkungan ataupun suasana yang aman dan terkendali. Seiring berkembangnya teknologi dalam bidang keamanan, dengan adanya Microcontroller ESP-32 merupakan solusi yang cukup efektif untuk membuat sistem perancangan keamanan dan monitoring yang dapat terintegrasi.

Dalam kemajuan teknologi, khususnya dalam konteks IoT (Internet of Things), memberikan pengalaman yang baru dalam meningkatkan keamanan yang diterapkan melalui perangkat pintar. Dengan menggunakan ESP-32,dengan adanya komponen seperti Wi-Fi dan Bluetooth, dapat memberikan fleksibilitas dalam merancang sistem keamanan yang dapat diakses ataupun dimonitor secara jarak jauh. Dengan, hal ini memungkin pengguna dapat mengawasi situasi dengan sangat efektif tanpa harus berada di lokasi.

Sistem keamanan dan monitoring yang berbasis ESP-32 tak hanya menawarkan keunggulan dalam hal jangkauan, akan tetapi juga kemampuan untuk dapat terhubung dengan berbagai sensor dan perangkat pendukung lainnya. Pada alat yang kami buat, kami menggunakan Sensor PIR (Passive Infra red Receiver) dan dikombinasikan dengan pesan Bot Telegram. 

### Tujuan
1. Pada rancangan sistem yang dibuat, telah menggunakan beberapa komponen gabungan dan sensor yang akurat. Sehingga sistem dapat digunakan sebagai alat keamanan yang optimal. Sistem perancangan ini diharapkan dapat menjaga keamanan dan dapat digunakan untuk mengantisipasi kejadian-kejadian yang tidak diinginkan.
2. Sistem yang telah dibuat dapat diimplementasi dimana saja, sebagai contoh pada konteks lingkungan atau perkantoran dapat digunakan untuk mengantisipasi akan terjadinya pembobolan atau kemalingan. Sistem ini dapat digunakan untuk meminimalisir kejahatan yang terjadi di lingkungan sekitar.
3. Sistem keamanan yang dikombinasikan dari mikrokontroller dan juga sensor PIR dapat sangat membantu dalam hal keamanan. Dengan Rancangan Sistem ini dapat meminimalisir dari kejadian-kejadian kejahatan dan juga yang lainnya.

### Dasar Teori
1. Konsep Otomatisasi. Otomatisasi mengacu pada penggunaan teknologi untuk mengendalikan atau mengeksekusi tugas-tugas tertentu tanpa adanya intervensi manusia langsung. Dalam konteks Sistem Security, otomatisasi dapat mengoptimalkan keamanan pada suatu tempat tertentu serta memberikan kemudahan untuk pengguna dalam melakukan penjagaan dan pengawasan pada suatu tempat tanpa harus berada di tempat tersebut. Prinsip dasar otomatisasi adalah memanfaatkan sensor untuk mendeteksi kondisi tertentu dan menggunakan aktuator untuk merespons kondisi tersebut, semua dikendalikan oleh mikrokontroler.
2. ESP32-DOIT. ESP32 adalah modul mikrokontroler terintegrasi yang memiliki fitur lengkap dan kinerja tinggi. Modul ini merupakan pengembangan dari ESP8266, yang merupakan modul WiFi populer.ESP32 memiliki dua prosesor komputasi, satu prosesor untuk mengelola jaringan WIFI dan Bluetooth, serta satu prosesor lainnya untuk menjalankan aplikasi. Dilengkapi dengan memori RAM yang cukup besar untuk menyimpan data. Fitur yang berguna seperti TCP/IP, HTTP, dan FTP. Modul ini juga dilengkapi fitur pemrosesan sinyal analog, dukungan untuk sensor, dan dukungan untuk perangkat masukan/keluaran (I/O) digital. ESP32 juga memiliki dukungan untuk konektivitas Bluetooth. Dapat digunakan untuk mengendalikan perangkat yang terhubung dengan Bluetooth.

![esp32_wifi_bluetooth](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/8dafacda-88ce-414f-926e-4e4023d470e3)

3. Modul Sensor PIR (Passive Infrared Receiver). Sensor PIR atau Passive Infrared Receiver merupakan sensor yang digunakan untuk mendeteksi adanya pancaran sinar infra red dari suatu objek. Sensor PIR memiliki sifat pasif, yang berarti tidak memancarkan sinar infrared tetapi hanya dapat menerima radiasi sinar infra red dari luar. Sensor PIR dapat mendeteksi radiasi dari berbagai objek karena semua objek memancarkan energi radiasi, seperti ketika terdeteksi sebuah gerakan dari sumber infra red dengan suhu tertentu yaitu manusia mencoba melewati sumber infra red yang lain misalnya dinding, maka sensor akan membandingkan pancaran infra red yang diterima setiap satuan waktu, sehingga jika ada pergerakan maka akan terjadi perubahan pembacaan pada sensor. Sensor PIR terdiri dari beberapa bagian yaitu, Lensa Fresnel, Penyaring Infra Red, Sensor Pyroelektrik, Penguat Amplifier dan Komparator.

![download](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/28fb9066-fa25-4761-be00-d4b27dbb18fa)

5. Buzzer. Buzzer adalah sebuah komponen elektronika yang mengubah energy listrik menjadi energy Mekanik atau getaran. Energy getaran ini akan menghasilkan suara. Buzzer juga biasanya digunakan untuk indikator suara untuk alarm, input keypad, dan pemberitahuan kerusakan pada sebuah sistem elektronik, seperti di motherboard komputer. Buzzer ini biasanya memiliki tegangan kerja antara 3 volt sampai dengan 12 volt.

![buzzer](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/5c44103f-497d-4865-a802-043065424649)

### Desain

A. Skema Wiring

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/4d69294b-5783-4009-8698-c18f657fa998)

Rancangan Desain Sistem

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/d44d6d4b-32ac-4989-9586-32f2659ea90f)

Prototype Sistem

Penjelasan Cara Kerja :
1. Powerbank digunakan untuk memberikan sumber daya berupa tegangan ke dalam ESP32, buzzer, serta sensor PIR.
2. ESP32 digunakan sebagai mikrokontroler dari sistem yang akan dijalankan. ESP32 sudah diberikan program untuk menjalankan sistem.
3. Sensor gerak PIR berfungsi sebagai pendeteksi objek bergerak yang melewati area sensor tersebut. Sensor akan menghasilkan output berupa sinyal ke ESP32 dan akan diteruskan ke dalam buzzer pada waktu yang bersamaan. Selain itu, pesan peringatan juga akan dikirimkan kepada pengguna via Telegram.
4. ESP32 berfungsi untuk mengirimkan sinyal ke dua komponen, pertama yakni Buzzer dan kedua ke aplikasi Telegram yang akan dikirim secara bersamaan.
5. Buzzer berfungsi sebagai alarm peringatan jika ada objek yang melintas.

B. Diagram Blok

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/c3b8df29-ee4f-484a-b962-98a029c4da8e)

Penjelasan:
1. PIR SENSOR: Berperan sebagai pengindera gerakan. Ketika gerakan terdeteksi, sensor mengirimkan sinyal elektrik ke ESP-32 untuk memberi tahu bahwa ada gerakan yang terjadi.
2. ESP-32 DOIT: Bertanggung jawab untuk membaca nilai yang diberikan oleh sensor PIR. Ketika gerakan terdeteksi, ESP-32 mengeksekusi tindakan tertentu, seperti mengirim notifikasi melalui Telegram dan mengontrol buzzer untuk memberi peringatan.
3. PESAN NOTIFIKASI: Ketika ESP-32 mendeteksi gerakan melalui sensor PIR, itu memicu pengiriman pesan notifikasi melalui layanan Telegram. Pesan ini berfungsi sebagai peringatan kepada pengguna atau pihak yang terkait bahwa gerakan telah terdeteksi di area yang diamati.
4. BUZZER: Buzzer diaktifkan oleh ESP-32 ketika gerakan terdeteksi. Ini memberikan peringatan suara sebagai tambahan kepada notifikasi visual melalui Telegram. Tujuannya adalah untuk memberi peringatan kepada orang-orang di sekitar bahwa gerakan telah terdeteksi.

C. Diagram Flowchart

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/c59ed054-64c4-4e8c-b1cf-b2e3e53076c5)


1. SETUP: Merupakan proses insialisasi awal yang meiliputi koneksi Wi-Fi, pengaturan token Bot Telegram, dan pengaturan pin untuk buzzer dan sensor.
2. BACA SENSOR: Merupakan proses looping pada bagian utama dari program. Pada bagian loop ini, nilai sensor akan dibaca terus-menerus.
3. DECISION: Jika sensor mendeteksi gerakan, sistem akan mengirimkan pesan melalui Bot Telegram dan akan mengaktifkan Buzzer sebagai alarm. Jika tidak, program akan tetap berada dalam loop ini.

### Hasil & Analisa
1. Batasan jarak yang dapat dideteksi oleh sensor sejauh : 5 meter.
2. Sensor dapat mendeteksi objek yang bergerak cepat.
3. Sensor terhubung dengan internet dan dapat mengirim pesan peringatan ke device pengguna melalui aplikasi Telegram dimanapun device pengguna berada.
4. Sistem membutuhkan waktu kalibrasi untuk Sensor PIR selama: 10 - 60 Detik
5. Tabel Pengujian Sistem

   ![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/067f3113-1607-4a47-96e5-9506383ca581)

   ![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/bea15ee9-d39b-40ff-8b66-9647ad8fec38)
