import os
from datetime import date

today = date.today()

def record(handle, duration):
    os.system(f"""ffmpeg -f avfoundation -i "1:0" -t 00:00:{duration} -y -r 10 recordings/{handle + '-' + str(today)}.mov""")