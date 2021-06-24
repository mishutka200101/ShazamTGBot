import base64
import subprocess
import librosa
import soundfile as sf


def convert_audio():
    src_filename = 'voice.ogg'
    dest_filename = 'voice.wav'

    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])

    x, sr = librosa.load(dest_filename, sr=48000)
    y = librosa.resample(x, 48000, 41100)
    sf.write("result.wav", y, 41100, subtype='PCM_16')

    with open("result.wav", "rb") as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode("utf-8")

    return base64_message
