# KEGOMODORO - Pomodoro Timer Application

## Overview

KEGOMODORO is a Pomodoro timer application designed to help you manage your time effectively using the Pomodoro Technique. This application includes a countdown timer, pause and resume functionality, and a floating window feature. It also integrates with Pixela to track and visualize your time management data.

![image](https://github.com/user-attachments/assets/3a2548d7-a839-417f-b0ee-02f87c302018)
![image](https://github.com/user-attachments/assets/03f6b559-2e03-44c9-9f9e-eaf5a2991da7)


## Features

- **Pomodoro Mode**: Track work and break periods using the **Pomodoro Technique**.
- **Stopwatch Mode**: Use the **timer** as a simple stopwatch.
- **Pause and Resume**: Pause and resume your timer **easily**.
- **Floating Timer**: Keep a floating window timer on top of **other applications**.

![368684829-96e1a41d-dc5d-40f3-a429-2cf6b6a2a41d](https://github.com/user-attachments/assets/f0dba28e-92f4-4bfa-80c6-5e5dbfab07fa)
- **Take Notes**: Take notes and save your work **automatically**.

![image](https://github.com/user-attachments/assets/0d16e654-c04e-4a1a-87b2-845b87be7f40)
- **Example**: **Automatically** saved notes:

![image](https://github.com/user-attachments/assets/0b669bc0-d472-4dcd-a5e7-9979df36786a)
- **Pixela Integration**: Uploads time data to Pixela for **visualization** and **tracking**.

![image](https://github.com/user-attachments/assets/6eb448b2-4fb5-4b39-9b36-377fc235a731)
**Example** of mine: https://pixe.la/v1/users/kegan/graphs/graph1.html


## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Required Python libraries:
  - `tkinter`
  - `Pillow`
  - `requests`
  - `datetime`
  - `csv`

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Kagankakao/KEGOMODORO.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd KEGOMODORO
   ```

3. **Install Dependencies**

   If you don't have the required libraries, you can install them using pip:

   ```bash
   pip install pillow requests
   ```

### Usage

1. **Run the Application**

   Execute the following command to start the application:

   ```bash
   python main.py
   ```

2. **Using the Timer**

   - **Start**: Click the "Start" button to begin the timer.
   - **Pause**: Click the "Pause" button to pause the timer. Click again to resume.
   - **Reset**: Click the "Reset" button to reset the timer to zero.
   - **Save**: Click the "Save" button to save the current time and notes to a CSV file.

3. **Floating Window**

   - Use the "SmallWindow" checkbox to toggle the floating timer window. This window will stay on top of other applications.

### Pixela Integration

To use Pixela integration, follow these steps:

1. **Create a Pixela Account**

   Sign up at [Pixela](https://pixe.la/) and create a new graph to track your time.

2. **Configure Pixela in Your Code**

   Open `main.py` and locate the `connect_to_pixela` function. Replace the placeholder values with your Pixela API token, user ID, and graph details.

3. **Save Data to Pixela**

   When you click the "Save" button, the application will attempt to upload your time data to Pixela. Ensure your Pixela configuration is correct to enable this feature.

### Configuration

You can customize the timer settings by adjusting the following variables in `main.py`:

- `SHORT_BREAK_MIN`: Duration of the short break in minutes.
- `LONG_BREAK_MIN`: Duration of the long break in minutes.
- `SAVE_FILE_NAME`: Name of the CSV file where your time data is saved.
- `MINUTE_X`, `MINUTE_Y`, `HOURS_X`, `HOURS_Y`: Coordinates for the floating window timer.

### Troubleshooting
    
- **Pixela Connection Issues**: Ensure you have a valid Pixela account and that your API token and graph details are correct.
- **Missing Libraries**: Make sure all required libraries are installed.

### Contributing

If you'd like to contribute to this project, please fork the repository, create a branch for your changes, and submit a pull request. For detailed contributing guidelines, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
