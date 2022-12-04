import music

music.play(music.BADDY)
'''
BADDY           BA_DING         BIRTHDAY
BLUES           CHASE           DADADADUM       ENTERTAINER
FUNERAL         FUNK            JUMP_DOWN       JUMP_UP
NYAN            ODE             POWER_DOWN      POWER_UP
PRELUDE         PUNCHLINE       PYTHON          RINGTONE
WAWAWAWAA       WEDDING
'''

music.set_tempo(bpm=120, ticks=4)
(BPM, TICKS) = music.get_empo()

music.pitch(1000, 100)  # play pitch 1KHz 維持100ms
for freq in range(2000, 3000, 100):
    music.pitch(freq, 1)
