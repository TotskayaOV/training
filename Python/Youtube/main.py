# pip install pytube

from pytube import YouTube

# Specify the URL of the YouTube video
video_url = "https://www.youtube.com/watch?v=HddMwKb-2q4"

# Create a YouTube object
yt = YouTube(video_url)

ys = yt.streams.get_highest_resolution()
ys.download()

print("Загрузка завершена!")

# get_throttling_function_name variable function_patterns to the following
#
# r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
# r'\([a-z]\s*=\s*([a-zA-Z0-9$]{2,3})(\[\d+\])?\([a-z]\)'
