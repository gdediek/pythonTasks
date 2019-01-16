import subprocess

result = subprocess.getoutput('ffmpeg -i VID_20180619_195915619.mp4 -c:v libx264 -preset slow -crf 22 -c:a copy VID_20180619_195915619_enc.mp4')

#ffmpeg -i input.mov -c:v libx264 -preset slow -crf 22 -c:a copy output.mp4
print(result)
