import tkinter as tk
import psutil

class BatteryWidget:
    def __init__(self, root, x, y):
        self.root = root
        self.root.geometry(f"200x100+{x}+{y}")  # Set position and size
        self.root.overrideredirect(True)  # Remove title bar
        self.root.attributes('-topmost', True)  # Keep on top
        
        # Draggable functionality
        self.root.bind("<Button-1>", self.start_move)
        self.root.bind("<B1-Motion>", self.do_move)
        
        # Battery Label
        self.battery_label = tk.Label(root, text="", font=("Arial", 18), fg="green")
        self.battery_label.pack(expand=True)

        # Refresh battery level
        self.update_battery_level()
    
    def update_battery_level(self):
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            charging = battery.power_plugged
            status = "Charging" if charging else "Discharging"
            color = "green" if percent > 50 else "orange" if percent > 20 else "red"
            
            self.battery_label.config(
                text=f"{percent}%\n{status}", fg=color
            )
        else:
            self.battery_label.config(
                text="No Battery Info", fg="gray"
            )
        
        # Schedule next update
        self.root.after(1000, self.update_battery_level)
    
    def start_move(self, event):
        self._drag_data = {"x": event.x, "y": event.y}
    
    def do_move(self, event):
        x = self.root.winfo_x() + event.x - self._drag_data["x"]
        y = self.root.winfo_y() + event.y - self._drag_data["y"]
        self.root.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    # Define the initial position
    x = 100  # Set X position
    y = 100  # Set Y position

    root = tk.Tk()
    app = BatteryWidget(root, x, y)
    root.mainloop()
