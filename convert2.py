from pydub import AudioSegment

def convert_mp4_to_mp3(mp4_file, mp3_file):
    try:
        audio = AudioSegment.from_file(mp4_file, format="mp4")
        audio.export(mp3_file, format="mp3")
        print(f"Conversion successful! MP3 saved at: {mp3_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

convert_mp4_to_mp3("Video.mp4", "Song.mp3")
