import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess the number (between 1 and 100):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.check_button = tk.Button(master, text="Check", command=self.check_guess)
        self.check_button.pack()

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif user_guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You've guessed the number {self.secret_number} correctly in {self.attempts} attempts.")
                self.check_button.config(state=tk.DISABLED)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()