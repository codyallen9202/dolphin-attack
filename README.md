# Dolphin Attack Research

#### dolphin_attack.ipynb is designed to shift the carrier frequency of an audio file formatted in .wav.

##### Steps to run dolphin_attack.ipynb:

- Step 1: Set up audio file names and directory locations (1st block of the
  jupyter notebook)
- Step 2: Make sure the audio is in .wav format
  - The second block of the jupyter notebook converts .m4a to .wav, however, all
    that is needed to change any different type of audio format is to replace
    the .m4a with one's own audio format (eg: .mp3)
- Step 3: Run all for the dolphin_attack.ipynb jupyter notebook and then the
  output will be the name of the audio file desired in the .wav format
  (output_file)

##### Testing the audio outputted by dolphin_attack.ipynb

- In order to test the ultra sonic audio, one must have a way to play such an
  audio at such a frequency with the correct amount of power
- In our case, through multiple testing with the ECE 569 lab, we moved towards
  our own approach
  - Macbook Pro with audio jack
  - 3.5 mm audio jack
  - TPA3116D2 Class D Stereo DC 5V-24V 2x50W Digital Audio Board
  - Goldwood Sound 75 Watts 8 ohm tweeter (Can play audio up to 27 kHz)
- With the equipment stated above, we were able to play inaudible audio
  frequencies, that could be picked up by iPhone's Siri
