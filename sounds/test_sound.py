from pydub import AudioSegment
from pydub.playback import play

# pydub doesn't have a stop feature
# sound = AudioSegment.from_mp3("sounds/forward_operating_base.mp3")
# play(sound)

# use simpleaudio to have a PlayObject() to get stop() method
import simpleaudio
from simpleaudio.shiny import PlayObject

sound = AudioSegment.from_mp3("sounds/forward_operating_base.mp3")
sound = sound[-5000:]
play_obj: PlayObject = simpleaudio.play_buffer(
    sound.raw_data,
    num_channels= sound.channels,
    bytes_per_sample= sound.sample_width,
    sample_rate= sound.frame_rate
)
# while True:
#     pass
play_obj.wait_done() # blocks main tread

print('Done')