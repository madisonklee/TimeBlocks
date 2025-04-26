import time
import pygame

'''
def getUserInput():
    num_intervals = int(input("How many unique intervals would you like? "))
    intervals = []
    
    for i in range(num_intervals):
        name = input(f"Name for interval {i+1}: ")
        duration = int(input(f"Duration of '{name}' in seconds: "))
        intervals.append((name, duration))
        
    reps = int(input("How many reps would you like to repeat the sequence? "))
    
    return intervals, reps
'''

def playSound():
    pygame.mixer.init()
    pygame.mixer.music.load("chime.mp3")  # make sure this file exists
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

def runTimer(intervals, reps):
    # intervals, reps = getUserInput()
    
    # print(f"\nStarting your interval timer for {reps} reps...\n")
    log = []
    for rep in range(1, reps + 1):
        log.append(f"Rep {rep}/{reps}")
        for i, (name, duration) in enumerate(intervals):
            log.append(f"⏱️  {name} — {duration} seconds")
            time.sleep(duration)
            playSound()
            log.append(f"✅  Finished: {name}")
    
    log.append("\nAll reps complete! Great job!")
    return log
    
