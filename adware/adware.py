import tkinter as tk
import random
import threading
import time

# Adware Pop-up Simulation
def create_popup():
    """Function to create a pop-up window."""
    popup = tk.Tk()
    popup.title("Adware Simulation")
    
    # Set random size and position
    width = random.randint(200, 400)
    height = random.randint(100, 200)
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = random.randint(0, screen_width - width)
    y = random.randint(0, screen_height - height)
    
    popup.geometry(f"{width}x{height}+{x}+{y}")
    tk.Label(popup, text="This is a harmless pop-up ad!", font=("Arial", 12)).pack(pady=10)
    tk.Button(popup, text="Close", command=popup.destroy).pack(pady=5)
    
    # Keep the window on top
    popup.attributes("-topmost", True)
    popup.mainloop()

def simulate_adware():
    """Simulates adware by creating random pop-ups."""
    while True:
        time.sleep(random.randint(1, 5))  # Wait between 1 to 5 seconds
        threading.Thread(target=create_popup).start()

# Alternative game logic (fox, hunter, lord game)
def play_game():
    """A simple game of 'fox', 'hunter', 'lord'."""
    list1 = ["fox", "hunter", "lord"]
    print("This is an alternative game of rock, paper and scissors ")
    print("")
    win_count = 0
    lose_count = 0
    win = True
    start_time = time.time()  # Track the game start time

    while win:
        cpu = random.choice(list1)
        user = input("Enter your choice:[fox, hunter, lord] or exit :  ")
        user = user.lower()

        if time.time() - start_time >= 10:  # After 10 seconds, start showing the adware
            print("\nAdware simulation starting now!")
            threading.Thread(target=simulate_adware).start()

        if (user == "fox" and cpu == "lord") or (user == "hunter" and cpu == "fox") or (user == "lord" and cpu == "hunter"):
            print("computer choose ", cpu)
            print("You have won")
            win_count += 1

        elif (user == "lord" and cpu == "fox") or (user == "fox" and cpu == "hunter") or (user == "hunter" and cpu == "lord"):
            print("computer choose ", cpu)
            print("You lose")
            lose_count += 1

        elif user == cpu:
            print("computer choose ", cpu)
            print("It is a draw")

        elif user == "exit":
            print("Goodbye")
            print("You won ", win_count, "times.", "You lose ", lose_count, "times.")
            win = False

        else:
            print("Not valid input. Please enter 'fox', 'hunter', or 'lord'.")

# Start the game and adware simulation
if __name__ == "__main__":
    threading.Thread(target=play_game).start()  # Start the game in a separate thread
