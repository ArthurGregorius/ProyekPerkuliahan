# Analisis Audio Dengan Transformasi Fourier

Transformasi Fourier adalah teknik matematis yang digunakan untuk menganalisis sinyal dalam domain waktu dan mentransformasikannya ke domain frekuensi. Konsep dasarnya didasarkan pada gagasan bahwa setiap sinyal kompleks dalam domain waktu dapat direpresentasikan sebagai jumlah dari sejumlah gelombang sinusoidal atau kosinusoidal dengan amplitudo dan frekuensi tertentu. Dengan kata lain, sinyal-sinyal yang kompleks dapat dipecah menjadi komponen-komponen sederhana dalam domain frekuensi. Proses kerja Transformasi Fourier dalam mengubah sinyal dari domain waktu ke domain frekuensi dapat dijelaskan sebagai berikut:

● Pemisahan Sinyal: Pertama, sinyal dalam domain waktu f(t) dipecah menjadi sejumlah komponen sinusoidal dan kosinusoidal dengan menggunakan fungsi-fungsi sinus dan kosinus.

● Pengukuran Amplitudo dan Frekuensi: Setiap komponen sinusoidal atau kosinusoidal memiliki amplitudo dan frekuensi tertentu. Amplitudo menyatakan seberapa besar gelombang tersebut, sedangkan frekuensi menunjukkan berapa kali gelombang tersebut berulang dalam satu unit waktu.

● Representasi dalam Domain Frekuensi: Kemudian, amplitudo dan frekuensi dari setiap komponen ini direpresentasikan dalam domain frekuensi. Ini memungkinkan kita untuk melihat kontribusi relatif dari setiap frekuensi terhadap sinyal keseluruhan.

● Spektrum Frekuensi: Hasil dari Transformasi Fourier adalah spektrum frekuensi, yang menunjukkan amplitudo dan fase dari setiap komponen frekuensi yang menyusun sinyal. Spektrum ini sering direpresentasikan dalam bentuk grafik, di mana sumbu horizontal menunjukkan frekuensi dan sumbu vertikal menunjukkan amplitudo atau kekuatan setiap frekuensi.

Dengan menggunakan Transformasi Fourier, kita dapat memahami struktur frekuensi dari sinyal-sinyal kompleks, yang berguna dalam berbagai aplikasi seperti pemrosesan sinyal, komunikasi, pengolahan gambar, dan banyak lagi. Ini memungkinkan kita untuk menganalisis, memanipulasi, dan memahami sinyal-sinyal yang kompleks dengan lebih baik.

Transformasi Fourier memiliki peran krusial dalam pengolahan sinyal digital dengan memberikan pemahaman yang mendalam tentang sinyal dalam domain frekuensi. Salah satu aplikasi utamanya adalah analisis sinyal, di mana Transformasi Fourier memungkinkan identifikasi komponen frekuensi yang dominan dalam sebuah sinyal, seperti frekuensi fundamental, harmonik, atau noise. Hal ini berguna dalam diagnosa gangguan atau karakterisasi sinyal dalam berbagai aplikasi seperti penginderaan jauh, pengolahan audio, dan pengolahan gambar medis. Selain analisis, Transformasi Fourier juga digunakan dalam pemfilteran sinyal. Dengan merancang dan menerapkan filter frekuensi, seperti filter rendah atau tinggi, kita dapat mengurangi atau menghilangkan komponen frekuensi yang tidak diinginkan dari sinyal. Ini meningkatkan kualitas sinyal, meningkatkan kejelasan informasi, dan mengurangi gangguan atau noise yang dapat mempengaruhi kinerja sistem.

Dalam konteks komunikasi digital, Transformasi Fourier memfasilitasi modulasi dan demodulasi sinyal. Modulasi mengubah sinyal informasi ke dalam frekuensi yang lebih tinggi untuk transmisi, sementara demodulasi mengembalikan sinyal ke domain waktu aslinya. Ini memungkinkan transmisi data secara efisien melalui saluran komunikasi dengan memanfaatkan kisaran frekuensi yang tersedia. Selain itu, Transformasi Fourier digunakan dalam kompresi data, di mana analisis frekuensi memungkinkan identifikasi komponen frekuensi yang kurang signifikan dalam sinyal. Dengan mengurangi representasi frekuensi yang tidak terlalu penting, kita dapat menciptakan versi yang lebih efisien dari sinyal asli, yang memungkinkan penyimpanan atau transmisi data dengan menggunakan lebih sedikit ruang penyimpanan atau bandwidth. Dengan demikian, Transformasi Fourier memberikan alat yang kuat dalam pengolahan sinyal digital, memungkinkan analisis mendalam, pemfilteran, modulasi/demodulasi, kompresi data, dan berbagai aplikasi lainnya, yang secara signifikan meningkatkan kinerja dan efisiensi sistem-sistem digital modern.

Dengan menggunakan teknik transformasi Fourier yang telah diimplementasikan secara efisien dalam program yang dikembangkan telah menghasilkan analisis mendalam terhadap sinyal suara yang diteliti. Proses analisis ini memungkinkan untuk secara akurat membedah sinyal suara menjadi domain frekuensi, mengungkapkan komponen-komponen penting yang tersembunyi di dalamnya. Melalui program yang dirancang khusus, dapat dengan cepat merespons perubahan dalam data sinyal suara dan menghasilkan visualisasi yang jelas tentang distribusi amplitudo dan frekuensi dari berbagai komponen dalam sinyal tersebut. Hasil analisis tersebut menunjukkan bahwa program yang dikembangkan mampu mengidentifikasi dan mengekstraksi fitur-fitur kunci, seperti amplitudo dominan dan pola periodik, yang menjadi fokus utama dalam pemrosesan lebih lanjut. Dengan demikian, dapat menghasilkan wawasan yang lebih mendalam tentang struktur dan karakteristik dari sinyal suara yang diamati, serta memungkinkan untuk membuat kesimpulan yang lebih meyakinkan dan relevan terkait dengan tujuan dan konteks penelitian ini.

Percobaan ini menggunakan lagu berjudul “Tarung Bebas” oleh grup band Perunggu, berikut adalah hasil dari program ketika dijalankan

![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/530ffb29-f0f5-4880-99b9-eedf7043d74a)

Gambar 1. Visualisasi Sinyal Audio “Tarung Bebas - Perunggu”


![image](https://github.com/ArthurGregorius/ProyekPerkuliahan/assets/147962819/2e106ae7-377c-4d01-9728-46be656ef886)

Gambar 2. Spektrum Frekuensi Audio “Tarung Bebas - Perunggu”


Gambar 1 di atas menunjukkan visualisasi sinyal audio yang dihasilkan oleh program. Sinyal audio tersebut direpresentasikan sebagai gelombang yang berosilasi di atas dan di bawah garis horizontal. Amplitudo gelombang menunjukkan kekuatan sinyal, sedangkan frekuensi gelombang menunjukkan seberapa sering siklus gelombang berulang. Pada gambar tersebut, terlihat bahwa sinyal audio memiliki frekuensi yang relatif konstan. Hal ini menunjukkan bahwa sinyal tersebut merupakan nada tunggal. Amplitudo sinyal juga relatif konstan, yang menunjukkan bahwa sinyal tersebut tidak terdistorsi. Informasi yang terdapat dalam gambar tersebut dapat digunakan untuk menganalisis kualitas sinyal audio

Berikut adalah beberapa detail yang dapat ditemukan dari gambar tersebut:

● Frekuensi: Frekuensi sinyal audio dapat dihitung dengan menghitung jumlah siklus gelombang dalam satu detik. Pada gambar tersebut, terdapat sekitar 25 siklus gelombang dalam satu detik. Oleh karena itu, frekuensi sinyal audio sekitar 25 Hz.

● Amplitudo: Amplitudo sinyal audio dapat diukur dengan melihat ketinggian gelombang dari garis horizontal. Pada gambar tersebut, amplitudo sinyal audio sekitar 0,75.

● Bentuk gelombang: Bentuk gelombang sinyal audio dapat dilihat dari pola osilasi gelombang. Pada gambar tersebut, bentuk gelombang sinyal audio adalah sinusoidal, yang menunjukkan bahwa sinyal tersebut merupakan nada tunggal.

Gambar 2 menunjukkan spektrum sinyal audio yang dihasilkan oleh sebuah program. Spektrum mewakili distribusi energi pada berbagai frekuensi dalam sinyal audio. Sumbu horizontal menunjukkan rentang frekuensi, sedangkan sumbu vertikal menunjukkan amplitudo atau tingkat energi pada setiap frekuensi. Pada gambar tersebut, spektrum menunjukkan puncak dominan di sekitar 1000 Hz, yang menunjukkan bahwa sinyal tersebut mengandung komponen kuat pada frekuensi ini. Ini sesuai dengan frekuensi fundamental sinyal, yang menentukan nada dasar dari suara yang dihasilkan. Selain itu, spektrum menunjukkan puncak yang lebih kecil pada harmonik dari frekuensi fundamental, seperti 2000 Hz, 3000 Hz, dan 4000 Hz. Harmonik ini berkontribusi pada timbre atau kualitas nada keseluruhan dari suara. Bentuk keseluruhan spektrum menunjukkan bahwa sinyal tersebut relatif murni, dengan energi minimal pada frekuensi di luar deret harmonik. Ini berarti sinyal tersebut bebas dari distorsi atau noise yang signifikan. Informasi yang terdapat dalam spektrum dapat digunakan untuk menganalisis karakteristik sinyal audio, seperti nada dasar, timbre, dan kemurniannya.

Berikut adalah beberapa detail yang dapat ditemukan dari gambar tersebut:

● Frekuensi Fundamental: Frekuensi fundamental dari sinyal audio kira-kira 1000 Hz.

● Harmonik: Spektrum menunjukkan harmonik dari frekuensi fundamental pada 2000 Hz, 3000 Hz, dan 4000 Hz.

● Timbre: Bentuk keseluruhan spektrum menunjukkan bahwa sinyal tersebut memiliki timbre yang relatif murni.
