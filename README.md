Battery Widget

This project provides a small, draggable battery widget for Windows, built using Python and Tkinter. The widget displays the current battery percentage and changes its color dynamically based on the battery level.

Features

Battery Indicator: Displays the current battery percentage and charging status.

Dynamic Colors:

Green: Battery level > 50%

Orange: Battery level between 20% and 50%

Red: Battery level < 20%

Draggable Widget: The widget can be dragged to any position on the screen.

Position Persistence: The widget saves its position to a file and restores it upon restart.

Customizable Position File: Specify a custom file path for position storage using a command-line argument.

Requirements

To run the project, you need the following dependencies:

Python 3.x

Required Python packages:

pip install -r requirements.txt

requirements.txt

tkinter
psutil

Usage

Running the Script

Clone the repository:

git clone https://github.com/Matt-K-TCR/Tablet_Battery.git
cd battery-widget

Install the required dependencies:

pip install -r requirements.txt

Run the script:

python battery_widget.py

Optional Argument

You can specify a custom file path for the widget's position:

python battery_widget.py --position-file /path/to/your_position_file.txt

How It Works

Battery Level Detection: The script uses the psutil library to retrieve battery status and percentage.

Dynamic Styling: The battery indicator changes its color and text color based on the battery level:

Green: Above 50%

Orange: Between 20% and 50%

Red: Below 20%

Position Persistence: The widget saves its current position to a file when moved, ensuring it reopens in the same position.

Text Visibility: The widget adjusts the text color for visibility, adding a shadow effect for white text when displayed on a green background.

Preview



Customization

Position File: By default, the position is stored in battery_position.txt. Use the --position-file argument to specify a custom location.

Size and Appearance: Modify the BatteryIcon class in the battery_widget.py file to adjust the widget's dimensions or styling.

License

This project is licensed under the  GNU GENERAL PUBLIC LICENSE. See the LICENSE file for details.

Feel free to contribute or raise issues for improvements!
