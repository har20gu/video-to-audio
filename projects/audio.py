from moviepy import VideoFileClip

def video_audio(video_path,audio_path):
   video = VideoFileClip(video_path)
   audio = video.audio
   audio.write_audiofile(audio_path)
   audio.close()
   video.close()



video_audio("video.mp4.mp4","ouptut.mp3")