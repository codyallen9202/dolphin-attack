import wave
import csv
import struct
import os


def wav_to_csv(wav_file, csv_file):
    try:
        # Open the .wav file
        with wave.open(wav_file, "rb") as wav:
            n_channels = wav.getnchannels()
            sample_width = wav.getsampwidth()
            framerate = wav.getframerate()
            n_frames = wav.getnframes()

            print(f"Processing {wav_file}...")
            print(f"Channels: {n_channels}")
            print(f"Sample Width: {sample_width} bytes")
            print(f"Framerate: {framerate} Hz")
            print(f"Total Frames: {n_frames}")

            # Read the frames
            frames = wav.readframes(n_frames)

            # Determine the format string for unpacking
            if sample_width == 2:  # 16-bit audio
                fmt = f"<{n_frames * n_channels}h"
            elif sample_width == 1:  # 8-bit audio
                fmt = f"<{n_frames * n_channels}B"
            else:
                raise ValueError(f"Unsupported sample width: {sample_width}")

            # Unpack the frames into amplitude values
            amplitude_values = struct.unpack(fmt, frames)

            # If stereo or multichannel, split channels; otherwise, keep it as is
            if n_channels > 1:
                amplitude_values = [
                    amplitude_values[i::n_channels] for i in range(n_channels)
                ]
            else:
                amplitude_values = [amplitude_values]

            # Write amplitude values to the CSV file
            with open(csv_file, "w", newline="") as csv_out:
                writer = csv.writer(csv_out)
                writer.writerow(
                    ["Sample"] + [f"Channel {i+1}" for i in range(n_channels)]
                )
                for i, values in enumerate(zip(*amplitude_values)):
                    writer.writerow([i] + list(values))

            print(f"Converted {wav_file} to {csv_file} successfully!")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
wav_file_path = "hey_siri.wav"  # Replace with your .wav file path
csv_file_path = os.path.splitext(wav_file_path)[0] + ".csv"
wav_to_csv(wav_file_path, csv_file_path)
