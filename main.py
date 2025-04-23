import time
import pygame

def getUserInput():
    num_intervals = int(input("How many unique intervals would you like? "))
    intervals = []
    
    for i in range(num_intervals):
        name = input(f"Name for interval {i+1}: ")
        duration = int(input(f"Duration of '{name}' in seconds: "))
        intervals.append((name, duration))
        
    reps = int(input("How many reps would you like to repeat the sequence? "))
    
    return intervals, reps

def playSound():
    pygame.mixer.init()
    pygame.mixer.music.load("chime.mp3")  # Make sure this file exists
    pygame.mixer.music.play()

    # Wait until the sound finishes playing
    while pygame.mixer.music.get_busy():
        continue

def runTimer():
    intervals, reps = getUserInput()
    
    print(f"\nStarting your interval timer for {reps} reps...\n")
    
    for rep in range(1, reps + 1):
        print(f"Rep {rep}/{reps}")
        for i, (name, duration) in enumerate(intervals):
            print(f"⏱️  {name} — {duration} seconds")
            time.sleep(duration)
            playSound()
            print(f"✅  Finished: {name}")
    
    print("\nAll reps complete! Great job!")
    # playSound()
    
# Run the timer
if __name__ == "__main__":
    runTimer()