# Filter dan Window

Filter dalam pemrosesan sinyal digital adalah algoritma atau perangkat lunak yang digunakan untuk memanipulasi sinyal input dengan cara tertentu. Tujuannya bisa bermacam-macam, misalnya untuk menghilangkan noise, menyoroti frekuensi tertentu, atau mengubah karakteristik sinyal. Filter dapat dibagi menjadi dua jenis utama: filter waktu (time-domain) dan filter frekuensi (frequency-domain).
- Filter Waktu: Filter yang beroperasi langsung pada domain waktu sinyal. Misalnya, filter rata-rata (moving average), filter Gaussian, atau filter deret Fourier.
- Filter Frekuensi: Filter yang beroperasi pada domain frekuensi sinyal. Contohnya termasuk filter low-pass, high-pass, band-pass, dan band-stop. Filter ini bekerja dengan cara memanipulasi komponen frekuensi dari sinyal.

Dalam konteks pemrosesan sinyal, jendela (window) adalah fungsi matematis yang digunakan untuk membatasi sinyal dalam interval waktu tertentu atau untuk memberikan bobot pada bagian tertentu dari sinyal. Jendela sering digunakan dalam teknik seperti analisis spektrum dengan Transformasi Fourier atau dalam teknik seperti Short-Time Fourier Transform (STFT) atau Discrete Fourier Transform (DFT).
- Jendela Waktu: Jendela yang digunakan untuk membatasi sinyal dalam interval waktu tertentu. Misalnya, jendela persegi (rectangular window), jendela Hamming, jendela Hanning, dan sebagainya. Masing-masing jendela memiliki karakteristik yang berbeda dalam hal resolusi frekuensi dan penurunan sinyal di tepi jendela.
