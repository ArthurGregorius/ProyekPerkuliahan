import librosa  # Import pustaka untuk analisis audio
import numpy as np  # Import pustaka untuk operasi matematika
import matplotlib.pyplot as plt  # Import pustaka untuk visualisasi

# Path ke file audio
audio_file = "Tarung Bebas (Perunggu).wav"

# Memuat file audio menggunakan librosa
signal, sr = librosa.load(audio_file, sr=None)  # Memuat file audio dan menyimpan sinyal serta sampling rate

# Tampilkan sinyal audio dalam domain waktu
plt.figure(figsize=(10, 4))  # Membuat gambar dengan ukuran 10x4 inci
plt.plot(np.arange(len(signal)) / sr, signal)  # Plot sinyal audio terhadap waktu
plt.xlabel('Waktu (detik)')  # Label sumbu x
plt.ylabel('Amplitudo')  # Label sumbu y
plt.title('Sinyal Audio')  # Judul plot
plt.show()  # Menampilkan plot

# Transformasi Fourier menggunakan fungsi bawaan numpy.fft
fft_signal = np.fft.fft(signal)  # Melakukan Transformasi Fourier
freq = np.fft.fftfreq(len(signal), 1/sr)  # Menghasilkan array frekuensi yang sesuai dengan Transformasi Fourier

# Tampilkan spektrum frekuensi hasil Transformasi Fourier
plt.figure(figsize=(10, 4))  # Membuat gambar dengan ukuran 10x4 inci
plt.plot(freq[:len(freq)//2], np.abs(fft_signal)[:len(freq)//2])  # Plot magnitude spektrum frekuensi
plt.xlabel('Frekuensi (Hz)')  # Label sumbu x
plt.ylabel('Amplitudo')  # Label sumbu y
plt.title('Spektrum Frekuensi Sinyal Audio')  # Judul plot
plt.show()  # Menampilkan plot

def discrete_fourier_transform(signal):
    # Implementasi manual Transformasi Fourier diskrit
    N = len(signal)  # Panjang sinyal
    n = np.arange(N)  # Array indeks dari 0 hingga N-1
    k = n.reshape((N, 1))  # Array indeks dalam bentuk kolom
    exp_term = np.exp(-2j * np.pi * k * n / N)  # Penghitungan eksponensial kompleks
    return np.dot(exp_term, signal)  # Hasil perkalian dot antara matriks eksponensial dan sinyal

# Panggil fungsi Transformasi Fourier diskrit yang diimplementasikan manual
fft_signal_manual = discrete_fourier_transform(signal)  # Memanggil fungsi Transformasi Fourier diskrit manual
