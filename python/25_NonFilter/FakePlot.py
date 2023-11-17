import random
import matplotlib.pyplot as plt
import numpy as np

# Parameters for the sine wave
wavelength_range = np.linspace(370, 870, 500)  # Wavelength range from 370 to 870
amplitude = 10  # Amplitude of the sine wave
frequency = 0.01  # Frequency of the sine wave

# Creating the sine wave with noise
sine_wave = amplitude * np.sin(frequency * wavelength_range)
noise = np.random.normal(0, 1, sine_wave.shape)
noisy_sine_wave = sine_wave + noise

# Plotting the noisy sine wave
plt.figure(figsize=(10, 6))
plt.plot(wavelength_range, noisy_sine_wave, label='Noisy Sine Wave')
plt.title("Noisy Sine Wave for Kalman Filter Practice")
plt.xlabel("Wavelength")
plt.ylabel("Energy")
plt.grid(True)
plt.legend()
plt.show()
