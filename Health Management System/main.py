# Healthy programmer
# it is a kind of reminder program for programmers who spend 5-10 hours sitting in front of their computer.
# it remindes them to take water or do some eye exercise or physical exercise in a given interval of time.
# it also keeps the log of when water is drunk of exercises are done in three different .txt files which are:
# Exercise_log.txt  ||   Eye_log.txt   ||   Water_log.txt

# what the program does is it reminds us to take a break from programming
# Water break - water.mp3  - (enters) Wt_Done - keep a log in log.txt
# Eyes break - eyes.mp3 - Ey_done  - keep a log in log.txt
# Physical break - activity.mp3 -- Ex_Done - leep a log in log.txt


# Important ::
# used Pygame module to play audio
# checked the clash between two events in same time


# Module versions ::
# pygame==2.0.1


# ----------------------------------------PROGRAM---------------------------------------------
import time
from pygame import mixer

busy = False  # this is the pointer which denotes whether a reminder
    # is active or not. it is used to prevent a clash
    # between two reminders when they are called at the same time


def water_log():
    """this is a function to write the keep the log of when water is drunk in Water_log.txt file"""
    Time = time.ctime()
    with open("log/Water_log.txt", "a") as F:
        F.writelines(Time + " --> Water Drunk\n")


def eye_log():
    """this is a function to write the keep the log of when Eye exercise is done in Eye_log.txt file"""
    Time = time.ctime()
    with open("log/Eye_log.txt", "a") as F:
        F.writelines(Time + " --> Eye exercise Done\n")


def exercise_log():
    """this is a function to write the keep the log of when physical exercise is done in Exercise_log.txt file"""
    Time = time.ctime()
    with open("log/Exercise_log.txt", "a") as F:
        F.writelines(Time + " --> Physical exercise Done\n")


def water_reminder():
    """this is a function for water reminder  """
    mixer.init()  # initialising the mixer
    mixer.music.load("audio/water.mp3")  # loading the audio
    mixer.music.set_volume(1)  # setting the volume
    mixer.music.play(-1)  # playing the music for infinite number of time
    while True:
        water_inp = input("Enter 'W_done' if you have drunk water: ")
        if water_inp == "W_done":
            mixer.music.stop()
            water_log()
            return False
        else:
            continue


def eye_reminder():
    """this is a function for eye exercise reminder  """
    mixer.init()  # initialising the mixer
    mixer.music.load("audio/eye.mp3")  # loading the audio
    mixer.music.set_volume(1)  # setting the volume
    mixer.music.play(-1)  # playing the music for infinite number of time
    while True:
        water_inp = input("Enter 'Ey_done' if you have done Eye exercise: ")
        if water_inp == "Ey_done":
            mixer.music.stop()
            eye_log()
            return False
        else:
            continue


def exercise_reminder():
    """this is a function for Physical exercise reminder  """
    mixer.init()  # initialising the mixer
    mixer.music.load("audio/exercise.mp3")  # loading the audio
    mixer.music.set_volume(1)  # setting the volume
    mixer.music.play(-1)  # playing the music for infinite number of time
    while True:
        water_inp = input("Enter 'Ex_done' if you have done Physical exercise: ")
        if water_inp == "Ex_done":
            mixer.music.stop()
            exercise_log()
            return False
        else:
            continue



if __name__ == '__main__':
    water_dur = int(input("Enter the duration between two water reminder in min.: ")) * 60
    eye_dur = int(input("Enter the duration between two eye exercise reminder in min.: ")) * 60
    exercise_dur = int(input("Enter the duration between two physical exercise reminder in min.: ")) * 60
    end_time = int(input("Enter the duration for which the reminder program will run in hour: ")) * 3600

    last_water_time = 0
    last_eye_time = 0
    last_exercise_time = 0

    time_count = 0
    ti1 = int(time.strftime("%S", time.gmtime()))
    while True:
        ti2 = int(time.strftime("%S", time.gmtime()))
        time_count += (ti2-ti1)
        if ti2 == 59:
            ti1 = -1
        else:
            ti1 = ti2
        # check if its time for drinking water
        if time_count-last_water_time == water_dur:
            last_water_time = time_count
            if not busy:
                busy = True
                busy = water_reminder()

        # check if its time for eye exercise
        if time_count-last_eye_time == eye_dur:
            last_eye_time = time_count
            if not busy:
                busy = True
                busy = eye_reminder()

        # check if its time for physical exercise
        if time_count-last_exercise_time == exercise_dur:
            last_exercise_time = time_count
            if not busy:
                busy = True
                busy = exercise_reminder()


        if time_count // 3600 == end_time:
            break
        time.sleep(1)

