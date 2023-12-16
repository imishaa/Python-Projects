import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Recording Started…")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording Finished")
secs=int(input("Enter the number of seconds you wish to record your voice: "))
fnm=input("Enter the name of the file after recording: ")
fnm=fnm+'.wav'
voice_recorder(secs,fnm)
