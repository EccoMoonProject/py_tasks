import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft


def sinusoidal_signal(day, month):
    N = 2**12
    fs = 10000
    amplitude = month
    frequency = day

    time = np.arange(0, N/fs, 1.0/fs)
    signal = amplitude * np.sin(2 * np.pi * time * frequency)

    return time, signal


# Przykładowe użycie funkcji sinusoidal_signal z parametrami day=5 i month=3
time, my_sinus = sinusoidal_signal(5, 3)


def plot_signal(time, signal, amplitude, frequency):
    plt.figure(figsize=(12, 6))
    plt.plot(time, signal)
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.title(
        f"Sygnał sinusoidalny o amplitudzie {amplitude} i częstotliwości {frequency} Hz")
    plt.grid(True)
    plt.show()


# Rysowanie wykresu dla sygnału my_sinus
plot_signal(time, my_sinus, 3, 5)

# Generowanie sygnałów z różnymi parametrami
time1, signal1 = sinusoidal_signal(10, 4)
time2, signal2 = sinusoidal_signal(15, 7)

# Rysowanie wykresów dla sygnałów z różnymi parametrami
plot_signal(time1, signal1, 4, 10)
plot_signal(time2, signal2, 7, 15)


# Sumowanie dwóch sygnałów
signal_sum = signal1 + signal2

# Rysowanie wykresu dla sumy sygnałów
plt.figure(figsize=(12, 6))
plt.plot(time1, signal_sum)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Suma dwóch sygnałów sinusoidalnych")
plt.grid(True)
plt.show()


def fourier_transform(signal):
    return fft.rfft(signal)


# Obliczenie transformacji sygnałów
transform_my_sinus = fourier_transform(my_sinus)
transform_signal1 = fourier_transform(signal1)
transform_signal2 = fourier_transform(signal2)
transform_signal_sum = fourier_transform(signal_sum)


def plot_fourier_transform(freqs, transform, title):
    plt.figure(figsize=(12, 6))
    plt.plot(freqs, 2 * np.abs(transform) / len(transform))
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    plt.title(title)
    plt.grid(True)
    plt.show()


# Obliczenie skali częstotliwości
N = 2**12
fs = 10000
freqs = fft.rfftfreq(N, 1.0/fs)

# Rysowanie wykresów transformat
plot_fourier_transform(freqs, transform_my_sinus,
                       "Transformata Fouriera - sinusoida urodzinowa")
plot_fourier_transform(freqs, transform_signal1,
                       "Transformata Fouriera - sygnał testowy 1")
plot_fourier_transform(freqs, transform_signal2,
                       "Transformata Fouriera - sygnał testowy 2")
plot_fourier_transform(freqs, transform_signal_sum,
                       "Transformata Fouriera - suma sygnałów testowych")


# W przypadku analizy wykresów transformaty Fouriera, możemy zauważyć, że amplitudy na wykresach są zgodne z amplitudami sygnałów pierwotnych. Wykresy pokazują również, że transformaty mają wartości niezerowe tylko w okolicach częstotliwości pierwotnych sygnałów sinusoidalnych.

# Dla sinusoidy urodzinowej, sygnałów testowych i ich sumy, transformaty Fouriera pokazują charakterystyczne piki na częstotliwościach odpowiadających częstotliwościom sygnałów pierwotnych. To pokazuje, że transformaty Fouriera mogą być używane do analizy składu częstotliwościowego sygnałów.
