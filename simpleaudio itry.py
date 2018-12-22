import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file('path/to/Nightcore - Rockefeller Street - (Lyrics).wav')
play_obj = wave_obj.play()
play_obj.wait_done()

#s = Sound()
#s.read('Nightcore - Rockefeller Street - (Lyrics).wav')
#s.play()