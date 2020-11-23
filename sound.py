from playsound import playsound
from pydub import AudioSegment

src = 'bensound-ukulele.mp3'

# playsound(src)

'''
Would to work in MacOS except after installling
"PyObjC" via `pip` per https://github.com/TaylorSMarks/playsound/issues/51
'''

# converting MP3 into .wav

sound = AudioSegment.from_mp3(src)

sound.export('bensound.wav', format='wav')