import speech_recognition as sr

# This lists every device your computer is currently using for audio
print("--- Available Audio Devices ---")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Index {index}: {name}")