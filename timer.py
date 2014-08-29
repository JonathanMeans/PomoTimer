import Tkinter as tk
import datetime
import random
import pygame

class App():
    def __init__(self):
        #Set up window
        self.root = tk.Tk()
        self.label = tk.Label(text="", font=("Helvetica", 150))
        self.label.pack()
        self.done_time = datetime.timedelta(seconds=0)

        self.pomo_count = 0
        self.is_break = False

        #Set up playlist
        self.tunes = ['sound.wav']
        for i in range(1, 6):
            self.tunes.append("sound%d.wav" % i)


        self.reset_timer()
        self.root.mainloop()

    def reset_timer(self):

        #Set timer for break
        #A longer, 10-minute break occurs every 4 pomodoros
        if self.is_break:
            if self.pomo_count is 4:
                difference = datetime.timedelta(seconds=60*10)
                self.pomo_count = 0
            else:
                difference = datetime.timedelta(seconds=60*5)

            self.is_break = False

        #Set 25-minute pomo-timer
        #If this were a serious project, there'd be fewer
        #magic number
        else:
            self.pomo_count += 1
            difference = datetime.timedelta(seconds=60*25)
            self.is_break = True

        self.done_time = datetime.datetime.now() + difference
        self.update_clock()

    def update_clock(self):
        elapsed = self.done_time - datetime.datetime.now()
        m, s = elapsed.seconds/60, elapsed.seconds%60
        self.label.configure(text="%02d:%02d" % (m, s))

        #Timer has hit the bottom
        if m <=0 and s <= 0:
            self.reset_timer()
            self.play_tune()

        #Wait for 1 second to pass and run again
        self.root.after(1000, self.update_clock)

    def play_tune(self):
        soundfile = random.choice(self.tunes)
        pygame.init()
        pygame.mixer.Sound(soundfile).play()

app=App()
