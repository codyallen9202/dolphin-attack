import numpy as np
import scipy.signal as signal
import soundfile as sf
import matplotlib.pyplot as plt

def shift_frequency(audio, sample_rate, shift_hz):
    """
    Shift the frequency of an audio signal by a specified amount.
    Args:
        audio (numpy.ndarray): Audio signal data.
        sample_rate (int): Sample rate of the audio signal.
        shift_hz (float): Amount to shift the frequency (in Hz).
    Returns:
        numpy.ndarray: Frequency-shifted audio signal.
    """
    t = np.arange(len(audio)) / sample_rate  # Time array
    shifted_audio = audio * np.exp(2j * np.pi * shift_hz * t)  # Apply frequency shift
    return np.real(shifted_audio)  # Take the real part to keep it as audio

def plot_waveform(audio, sample_rate, title):
    """
    Plot the waveform of an audio signal.
    Args:
        audio (numpy.ndarray): Audio signal data.
        sample_rate (int): Sample rate of the audio signal.
        title (str): Title of the plot.
    """
    t = np.arange(len(audio)) / sample_rate
    plt.figure(figsize=(10, 4))
    plt.plot(t, audio)
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

def main():
    input_file = "hey_siri.wav"  # Path to the input audio file
    output_file = "hey_siri_ultrasonic.wav"  # Path to the output audio file
    frequency_shift = 20000  # Frequency shift in Hz

    # Load audio file
    audio, sample_rate = sf.read(input_file)
    if len(audio.shape) > 1:  # If stereo, convert to mono
        audio = audio.mean(axis=1)

    # Plot original waveform
    plot_waveform(audio, sample_rate, "Original Audio Waveform")

    # Shift the frequency
    shifted_audio = shift_frequency(audio, sample_rate, frequency_shift)

    # Normalize to prevent clipping
    shifted_audio = shifted_audio / np.max(np.abs(shifted_audio))

    # Save the frequency-shifted audio
    sf.write(output_file, shifted_audio, sample_rate)

    # Plot shifted waveform
    plot_waveform(shifted_audio, sample_rate, "Frequency-Shifted Audio Waveform")

    print(f"Frequency-shifted audio saved to {output_file}")

if __name__ == "__main__":
    main()
