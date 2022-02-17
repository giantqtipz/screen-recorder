import os
import glob
from threading import Timer

x = 0
def record():
	global x
	fld = "H:\\ffmpeg\\output\\output"
	if not fld + str(x) + ".mp4" in glob.glob(fld + "*.mp4"):
		filename = fld + str(x) + ".mp4"
	else:
		x += 1
		record()
 
	audio = "Microfono (8- Logitech USB Headset)"
 
	os.system(f"""ffmpeg -f avfoundation -i "1:0" -t 00:00:05 -y -r 10 out.mov""")
 
 
record()

