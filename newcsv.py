import numpy as np
import wave
import csv
import argparse


def wav_to_csv(input_wav, output_csv, normalize=True):
    """
    Converts a .wav file to a .csv file with numeric data.

    Parameters:
        input_wav (str): Path to the input .wav file.
        output_csv (str): Path to the output .csv file.
        normalize (bool): Normalize waveform to [-1, 1] range if True.
    """
    # Open the .wav file
    with wave.open(input_wav, "rb") as wav_file:
        # Extract parameters
        n_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        n_frames = wav_file.getnframes()

        print(
            f"Channels: {n_channels}, Sample Width: {sample_width} bytes, Frame Rate: {frame_rate} Hz, Frames: {n_frames}"
        )

        # Read the waveform data
        raw_data = wav_file.readframes(n_frames)
        dtype = (
            np.int16 if sample_width == 2 else np.int8
        )  # Determine the data type based on sample width
        waveform = np.frombuffer(raw_data, dtype=dtype)

        # If stereo, average the channels
        if n_channels > 1:
            waveform = waveform.reshape(-1, n_channels).mean(axis=1)

        # Normalize the waveform to [-1, 1] if required
        if normalize:
            waveform = waveform / np.max(np.abs(waveform))

    # Save to CSV
    with open(output_csv, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for value in waveform:
            writer.writerow([value])

    print(f"Converted {input_wav} to {output_csv} successfully.")


if __name__ == "__main__":
    # Argument parser for command-line use
    parser = argparse.ArgumentParser(
        description="Convert .wav file to .csv for Keysight 33500B."
    )
    parser.add_argument("input_wav", help="Path to the input .wav file")
    parser.add_argument("output_csv", help="Path to the output .csv file")
    parser.add_argument(
        "--no-normalize", action="store_true", help="Disable normalization to [-1, 1]"
    )
    args = parser.parse_args()

    wav_to_csv(args.input_wav, args.output_csv, not args.no_normalize)
