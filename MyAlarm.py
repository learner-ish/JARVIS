import datetime
import pygame

def alarm(Timing, sound_file):
    pygame.init()
    pygame.mixer.init()
    
    altime = datetime.datetime.strptime(Timing, "%I:%M %p")
    Horeal = altime.hour
    Mireal = altime.minute
    print(f"Done, alarm is set for {Timing}")

    # Load the music file
    pygame.mixer.music.load(sound_file)

    while True:
        if Horeal == datetime.datetime.now().hour and Mireal == datetime.datetime.now().minute:
            print("Alarm is ringing")
            pygame.mixer.music.play()  # Start playing the music

            # Wait for the music to finish playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  # Adjust tick value as needed

            # Once finished, rewind and play again if the time condition is still true
            pygame.mixer.music.rewind()
            
        elif Mireal < datetime.datetime.now().minute:
            pygame.mixer.music.stop()
            pygame.quit()
            break

if __name__ == '__main__':
    alarm('1:47 PM', 'Bhajan.mp3')  # Replace with your MP3 file path
