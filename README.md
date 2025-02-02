# KEGOMODORO – Customizable Pomodoro & Stopwatch Timer ⏳

Welcome to **KEGOMODORO**! A completely open-source Pomodoro and Stopwatch timer designed to improve your time management and make working more fun. Whether you're studying, working, or just need a reliable timer, KEGOMODORO is here to keep you on track. Best of all, it's highly customizable, so you can make it fit your exact needs!

**TOMATO AND BERSERK THEME!**
![image](https://github.com/user-attachments/assets/ee38a43d-438e-4d9c-8320-29097d6b5b5f)




### **Behelit Feature (from *Berserk*)**
- For fans of *Berserk*, a Behelit feature has been added to the cronometer. When activated, it serves as a special timer with a visual reference to the Behelit, adding a touch of *Berserk* magic to your experience!

## 💡 Key Features

- **Pomodoro & Stopwatch Mode**: Toggle between Pomodoro and Stopwatch timers easily.
- **Always on Top**: Keep your timer visible with the "Always on Top" feature.
- **Quick Notes & Session Logging**: Record your notes and working hours in a jiffy.
- **Work Hours Graph**: Visualize your productivity with a graph of your work hours 📊.
- **Behelit Mode (Berserk Theme)**: For fans of Berserk, a Behelit-inspired timer with a dark twist!
- **Lightweight & Simple**: Developed in Python with no unnecessary dependencies.

## 🎨 Custom Themes & Personalization

KEGOMODORO is all about **customization**. Easily create your own themes, change colors, and adjust the look of your timer. The goal is to make time management not only effective but visually appealing too.

The image below shows just a few of the many customizable options you can apply.

## 🐍 Built with Python

KEGOMODORO is developed in **Python**, making it easy to modify, extend, and understand. Whether you’re a beginner or an expert, the code is simple to follow, and the project is perfect for learning how to build your own timers.

## 💻 Fully Open Source

This project is completely open-source! You can fork it, contribute, and make improvements or adapt it for your own use. Let’s make time management even better, together!

![368684829-96e1a41d-dc5d-40f3-a429-2cf6b6a2a41d](https://github.com/user-attachments/assets/f0dba28e-92f4-4bfa-80c6-5e5dbfab07fa)
- **Take Notes**: Take notes and save your work **automatically**.

![image](https://github.com/user-attachments/assets/5793db64-fa98-4971-a193-4ffd78c406c2)
- **Example**: **Automatically** saved notes:

![image](https://github.com/user-attachments/assets/0b669bc0-d472-4dcd-a5e7-9979df36786a)
- **Pixela Integration**: Uploads time data to Pixela for **visualization** and **tracking**.
- Here is mine: https://pixe.la/v1/users/kegan/graphs/graph1.html
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

To use Pixela, follow these steps:

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
