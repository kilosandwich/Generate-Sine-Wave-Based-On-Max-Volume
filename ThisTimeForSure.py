import sounddevice as sd
import numpy as np

def generate_sine_wave(duration, frequency, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return sine_wave

def callback(indata, frames, time, status):
    if status:
        print(f"Error in audio stream: {status}")
    maxfreq = np.max(indata) #I'm not actually sure if this is the max in the sampling period, but it sure is.
    print(maxfreq)
    # Generate a sine wave with the same size as the sampled block
    #duration is measured in seconds
    #duration = frames / sample_rate
    duration = 0.5 #the duration of the sine wave generated
    frequency = 1000 * maxfreq  # Set the desired frequency of the sine wave
    sine_wave = generate_sine_wave(duration, frequency, sample_rate) #generate the sine wave

    # Play the generated sine wave
    sd.play(sine_wave, sample_rate, blocking=False)

# Set the sample rate and block size
sample_rate = 44100 /10 #this represents how many samples are taken
block_size = 1024 * 4 #this represents how many of those samples are passed to the callback function

# Start the audio stream with an increased block size
with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate, blocksize=block_size):
    print("Listening and generating sine wave...")
    sd.sleep(10000000)  # Adjust the sleep duration based on your requirements