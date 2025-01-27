import tkinter as tk
import psutil

class BatteryIcon:
    def __init__(self, root, x, y):
        self.root = root
        self.root.geometry(f"60x30+{x}+{y}")  # Set smaller window size and position
        self.root.overrideredirect(True)  # Remove title bar
        self.root.attributes('-topmost', True)  # Keep on top
        self.root.attributes('-transparentcolor', 'white')  # Make white transparent

        # Draggable functionality
        self.root.bind("<Button-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.do_move)

        # Create canvas for battery icon
        self.canvas = tk.Canvas(root, width=60, height=30, bg="white", highlightthickness=0)
        self.canvas.pack()

        # Draw battery outline
        self.battery_body = self.canvas.create_rectangle(5, 7, 50, 23, outline="black", width=1)
        self.battery_tip = self.canvas.create_rectangle(50, 10, 55, 20, outline="black", fill="black")

        # Fill rectangle for battery level
        self.battery_fill = self.canvas.create_rectangle(6, 8, 6, 22, outline="", fill="green")

        # Text for percentage
        self.battery_text = self.canvas.create_text(30, 15, text="", font=("Arial", 6, "bold"))

        # Refresh battery level
        self.update_battery_level()

    def update_battery_level(self):
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            charging = battery.power_plugged
            status = "⚡" if charging else ""
            color = "green" if percent > 50 else "orange" if percent > 20 else "red"

            # Update battery fill
            self.canvas.coords(self.battery_fill, 6, 8, 6 + percent * 0.44, 22)
            self.canvas.itemconfig(self.battery_fill, fill=color)

            # Update percentage text
            self.canvas.itemconfig(self.battery_text, text=f"{percent}% {status}", fill=color)
        else:
            # Handle cases where battery information isn't available
            self.canvas.itemconfig(self.battery_text, text="No Batt", fill="gray")
            self.canvas.itemconfig(self.battery_fill, fill="gray")

        # Schedule next update
        self.root.after(1000, self.update_battery_level)

    def start_move(self, event):
        self._drag_data = {"x": event.x, "y": event.y}

    def do_move(self, event):
        x = self.root.winfo_x() + event.x - self._drag_data["x"]
        y = self.root.winfo_y() + event.y - self._drag_data["y"]
        self.root.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    # Set initial position
    x = 100  # X coordinate
    y = 100  # Y coordinate

    root = tk.Tk()
    app = BatteryIcon(root, x, y)
    root.mainloop()
