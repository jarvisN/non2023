
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
print(noisy_sine_wave)

def kalman_filter(noisy_data, initial_estimate, estimation_error, measurement_error, process_error):
    estimate = initial_estimate
    estimation_error = estimation_error

    estimates = []
    for measurement in noisy_data:
        # Measurement Update
        kalman_gain = estimation_error / (estimation_error + measurement_error)
        estimate = estimate + kalman_gain * (measurement - estimate)
        estimation_error = (1 - kalman_gain) * estimation_error

        # Process Update
        estimation_error = estimation_error + process_error

        estimates.append(estimate)

    return estimates

# Kalman Filter Parameters
initial_estimate = 0  # Initial estimate
estimation_error = 1  # Initial estimation error
measurement_error = 1  # Error in measurements
process_error = 0.1   # Process error

# Applying Kalman Filter on the noisy sine wave data
kf_estimates = kalman_filter(noisy_sine_wave, initial_estimate, estimation_error, measurement_error, process_error)

# Plotting the original and filtered data
plt.figure(figsize=(10, 6))
plt.plot(wavelength_range, noisy_sine_wave, label='Noisy Data')
plt.plot(wavelength_range, kf_estimates, label='Kalman Filter Output', color='red')
plt.plot(wavelength_range,sine_wave, label = 'Sine', color='blue')
plt.title("Comparison of Noisy Data and Kalman Filter Output")
plt.xlabel("Wavelength")
plt.ylabel("Energy")
plt.grid(True)
plt.legend()
plt.show()
