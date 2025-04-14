import time
from playsound import playsound

def getUserInput():
    num_intervals = int(input("How many unique intervals would you like? "))
    intervals = []
    
    for i in range(num_intervals):
        name = input(f"Name for interval {i+1}: ")
        duration = int(input(f"Duration of '{name}' in seconds: "))
        intervals.append((name, duration))
        
    reps = int(input("How many reps would you like to repeat the sequence? "))
    
    restBool = bool(input("Would you like a rest period between intervals? (y/n): "))
    rest = 0
    if restBool == "y":
        rest = int(input("How long (in seconds) would you like the rest periods to be? "))
    
    return intervals, reps, rest, restBool

def playSound():
    playsound('chime.mp3')
    
def runTimer():
    intervals, reps, rest_bool, rest = getUserInput()
    
    print(f"\nStarting your interval timer for {reps} reps...\n")
    
    for rep in range(1, reps + 1):
        print(f"Rep {rep}/{reps}")
        for i, (name, duration) in enumerate(intervals):
            print(f"⏱️  {name} — {duration} seconds")
            time.sleep(duration)
            playSound()
            print(f"✅  Finished: {name}")
            
            if rest_bool and (i < len(intervals) - 1):  # Don't rest after last interval
                print(f"Rest for {rest} seconds...")
                time.sleep(rest)
                playSound()
    
    print("\nAll reps complete! Great job!")
    playSound()
    
# Run the timer
if __name__ == "__main__":
    runTimer()