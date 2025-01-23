import tkinter as tk
import random
import threading
import time

# Pop-up Simulation (Adware)
def r7v2():
    """Function to create a pop-up window."""
    p1b9 = tk.Tk()
    p1b9.title("Adware Simulation")
    
    # Set random size and position
    u3d7 = random.randint(200, 400)
    p3j2 = random.randint(100, 200)
    s8q5 = p1b9.winfo_screenwidth()
    t4h9 = p1b9.winfo_screenheight()
    y2s1 = random.randint(0, s8q5 - u3d7)
    y4h2 = random.randint(0, t4h9 - p3j2)
    
    p1b9.geometry(f"{u3d7}x{p3j2}+{y2s1}+{y4h2}")
    tk.Label(p1b9, text="This is a harmless pop-up ad!", font=("Arial", 12)).pack(pady=10)
    tk.Button(p1b9, text="Close", command=p1b9.destroy).pack(pady=5)
    
    # Keep the window on top
    p1b9.attributes("-topmost", True)
    p1b9.mainloop()

def q6d5():
    """Simulates adware by creating random pop-ups."""
    while True:
        time.sleep(random.randint(1, 5))  # Wait between 1 to 5 seconds
        threading.Thread(target=r7v2).start()

# Fox, Hunter, Lord game logic
def s8t0():
    """A simple game of 'fox', 'hunter', 'lord'."""
    x2b6 = ["fox", "hunter", "lord"]
    print("This is an alternative game of rock, paper, and scissors ")
    print("")
    h3f7 = 0
    v9l3 = 0
    r8e9 = True
    start_time = time.time()  # Track the game start time

    while r8e9:
        cpu_choice = random.choice(x2b6)
        user_input = input("Enter your choice:[fox, hunter, lord] or exit :  ")
        user_input = user_input.lower()

        if time.time() - start_time >= 10:  # After 10 seconds, start showing the adware
            print("\nAdware simulation starting now!")
            threading.Thread(target=q6d5).start()

        if (user_input == "fox" and cpu_choice == "lord") or (user_input == "hunter" and cpu_choice == "fox") or (user_input == "lord" and cpu_choice == "hunter"):
            print("computer choose ", cpu_choice)
            print("You have won")
            h3f7 += 1

        elif (user_input == "lord" and cpu_choice == "fox") or (user_input == "fox" and cpu_choice == "hunter") or (user_input == "hunter" and cpu_choice == "lord"):
            print("computer choose ", cpu_choice)
            print("You lose")
            v9l3 += 1

        elif user_input == cpu_choice:
            print("computer choose ", cpu_choice)
            print("It is a draw")

        elif user_input == "exit":
            print("Goodbye")
            print("You won ", h3f7, "times.", "You lose ", v9l3, "times.")
            r8e9 = False

        else:
            print("Not valid input. Please enter 'fox', 'hunter', or 'lord'.")

# Start the game and adware simulation
if __name__ == "__main__":
    threading.Thread(target=s8t0).start()  # Start the game in a separate thread
