import csv
import tkinter.messagebox
import math
import pandas as pd
import datetime as dt
import requests
import datetime
import time
import pygame
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from pyautogui import position
from time import sleep
from keyboard import is_pressed
from PIL import Image, ImageTk
from pathlib import Path
# ---------------------------- CONSTANTS AND SOME VARIABLES ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#77ed95"
YELLOW = "#f7f5dd"
ORANGE = "#fcba03"
DEEP_BLUE = "#281c3c"
DEEP_RED = "#249813"
FONT_NAME = "Courier"
TOMATO_COLOR = "#f26849"
WHITE = "#feffff"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "YOUR_GRAPH_ID"

DEPENDENCIES = Path("dependencies/")
IMAGES = f"{DEPENDENCIES}/images"
AUDIOS = f"{DEPENDENCIES}/audios"
TEXTS = f"{DEPENDENCIES}/texts"

SAVE_FILE_NAME = f"{TEXTS}/YOUR_CSV_FILE_NAME.txt" # ! Change this to your desired file name
BREAK_SOUND_PATH = f"{AUDIOS}/Ding.mp3"
APP_ICON_PATH = f"{IMAGES}/tomato_window.png" # ! THIS IS THE ICON STUFF SO CHANGE THIS
FLOATING_IMAGE_PATH = f"{IMAGES}/tomato.gif"
LOGO_IMAGE_PATH = f"{IMAGES}/logo.png"
MAIN_IMAGE_PATH = f"{IMAGES}/tomato.png"
FLOATING_WINDOW_CHECKER_PATH = f"{TEXTS}/floating_window_checker.txt"
TIME_CSV_PATH = f"{TEXTS}/time.csv"
# Load to audio file
pygame.mixer.init()
BREAK_SOUND = pygame.mixer.Sound(BREAK_SOUND_PATH)
#TODO CHANGE THE SAVE NOTE ICON
# ----------------------------- TIMER VARIABLES ------------------------------- #
now = str(datetime.datetime.now())
DATE = now.split(" ")[0].replace("-", "")

saved_data = {
    "date": [],
    "time": [],
    "notes": []
}

# ----------------------------- TIMER CONFIGS ------------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
resume = 0
start_timer_checker = 0
second = 0
minute = 0
hours = 0
count_downer = 0
count_upper = 0
HOURS_X=7
HOURS_Y=110
MINUTE_X=38
MINUTE_Y=110

show_hours = False
pomodoro_mode_activate = False
crono_mode_activate = False
condition_checker = True
paused = False
start_short_break= False
start_long_break = False
open_floating_window = False

#TODO: LONG_BREAK 05:00 TEXTİNİ DİNAMİK YAP

# ------------------------------ SOME BOOT-UPS --------------------------------- #

# Creating time.csv
try:
    with open(TIME_CSV_PATH, "r") as file:
        file.read()
except:
    with open(TIME_CSV_PATH, "w") as file:
        file.write("hours,minute,second\n0,0,0\n")

# -------------------------- CONECTION WITH PIXELA ------------------------------- #
def connect_to_pixela():
    global hours
    params = {
        "color": "momiji",
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    # creates user
    response = requests.post(url=PIXELA_ENDPOINT, json=params)
    print(response.text)
    # print(response.text)

    graphic_endpoint = f"{PIXELA_ENDPOINT}{USERNAME}/graphs"
    graphic_params = {
        "id": GRAPH_ID,
        "name": USERNAME,
        "unit": "hours",
        "type": "float",
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }

    # creates graph
    graph_response = requests.post(url=graphic_endpoint, json=graphic_params, headers=headers)
    add_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixels_params = {
        "date": DATE,
        "quantity": str(hours),
    }
    pixel_response = requests.post(url=add_pixel_endpoint, json=pixels_params, headers=headers)
    print(pixel_response.text)
    print(len(pixel_response.text))
    update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
    update_pixel_params = {
        "quantity": str(hours),
    }
    # updates pixel quantity
    update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)

    delete_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

    # delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    if len(pixel_response.text) == 341:
        print("Trying to connect to Pixela again...")
        time.sleep(0.5)
        connect_to_pixela()
# ----------------------------MODS---------------------------- #
def pomodoro_mode():
    global pomodoro_mode_activate, crono_mode_activate

    reset()
    crono_mode_activate = False
    pomodoro_mode_activate = True


def crono_mode():
    global crono_mode_activate, pomodoro_mode_activate, second, minute, hours, show_hours, crono_reset
    reset()
    crono_mode_activate = True
    pomodoro_mode_activate = False

    # get's the time in time file
    print("in crono_mode")
    df = pd.read_csv(TIME_CSV_PATH)
    second = df['second'].iloc[-1]
    minute = df['minute'].iloc[-1]
    hours = df['hours'].iloc[-1]
    if show_hours != "0":
        show_hours = True

    if not show_hours:
        canvas.itemconfig(timer, text=f"{minute:02d}:{second:02d}")
        floating_timer_label.congig(text=f"{minute:02d}:{second:02d}")
        floating_timer_label.place(x=MINUTE_X, y=MINUTE_Y)
    if show_hours:
        canvas.itemconfig(timer, text=f"{hours:02d}:{minute:02d}:{second:02d}", font=(FONT_NAME, 30, "bold"))
        floating_timer_label.config(text=f"{hours:02d}:{minute:02d}:{second:02d}", font=(FONT_NAME, 28, "bold"))
        floating_timer_label.place(x=HOURS_X, y=HOURS_Y)
def floating_window(**kwargs):
    global open_floating_window, checked_state
    print(open_floating_window)
    if open_floating_window == "True" or open_floating_window == "False":
        print(open_floating_window)
        print(type(open_floating_window))
        open_floating_window = open_floating_window.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
    open_floating_window = not open_floating_window
    print(open_floating_window)
    try:
        kwargs["check"]
    except Exception as e:
        print(f"Error: {e}")
    else:
        open_floating_window = kwargs.get("check") 
        print(open_floating_window)
        print(type(open_floating_window))
    if open_floating_window == "True" or open_floating_window == True:
        window.deiconify()
        checked_state.set(1)
    elif open_floating_window == "False" or open_floating_window == False:
        window.withdraw()
        checked_state.set(0)
    with open(FLOATING_WINDOW_CHECKER_PATH, "w") as f:
        f.write(str(open_floating_window))




# ----------------------------TIMER RESET ------------------------------- #
def reset():
    global reps, count_downer, count_upper, start_timer_checker, minute, second, pause_checker, \
        condition_checker, pomodoro_mode_activate, crono_mode_activate, hours, show_hours
    if pomodoro_mode_activate:
        try:
            root.after_cancel(count_downer)
        except Exception as e:
            print(f"Error: {e}")
    elif crono_mode_activate:
        try:
            root.after_cancel(count_upper)
        except Exception as e:
            print(f"Error: {e}")


    else:
        print("Error: No mode selected")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    reps = 1
    start_timer_checker = 0
    resume = 0
    hours = 0
    minute = 0
    second = 0
    condition_checker = True
    show_hours = False
    # pause_checker = 0
    pause_button.config(text=f"Pause")
    canvas.itemconfig(timer, text="00:00", font=(FONT_NAME, 30, "bold"))
    floating_timer_label.config(text="00:00", font=(FONT_NAME, 28, "bold"))
    floating_timer_label.place(x=38, y=110)
    

# ---------------------------- CRONOMETER MECHANISM ------------------------------- #
def crono():
    global count_upper, second, minute, hours, show_hours
    timer_label.config(text="WORK", fg=RED)
    if not show_hours:
        canvas.itemconfig(timer, text=f"{minute:02d}:{second:02d}")
        floating_timer_label.config(text=f"{minute:02d}:{second:02d}")
        floating_timer_label.place(x=MINUTE_X, y=MINUTE_Y)
    # Update the timer display every second
    second += 1
    if second == 60:
        second = 0
        minute += 1
    elif minute == 60:
        minute = 0
        hours += 1
        show_hours = True
    if show_hours:
        canvas.itemconfig(timer, text=f"{hours:02d}:{minute:02d}:{second:02d}", font=(FONT_NAME, 30, "bold"))
        floating_timer_label.config(text=f"{hours:02d}:{minute:02d}:{second:02d}", font=(FONT_NAME, 28, "bold"))
        floating_timer_label.place(x=HOURS_X, y=HOURS_Y)
    # you can change the speed of countup here
    count_upper = root.after(1000, crono)


# --------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    global start_timer_checker, pause_checker, condition_checker, pomodoro_mode_activate, crono_mode_activate, start_short_break, start_long_break
    condition_checker = False
    print("a")
    if pomodoro_mode_activate:
        start_timer_checker += 1
        pause_checker = 1
        if start_timer_checker == 1:
            global reps
            condition_checker = False
            work_sec = WORK_MIN * 60
            short_break_sec = SHORT_BREAK_MIN * 60
            long_break_sec = LONG_BREAK_MIN * 60
            print(reps)
            if reps % 8 == 0:
                BREAK_SOUND.play()
                variable = condition_checker
                condition_checker = False
                start_long_break = True
                pause_timer()
                condition_checker = variable
                timer_label.config(text="Break", fg=PINK)
                # if condition_checker:
                #     count_down(long_break_sec)
                canvas.itemconfig(timer, text=f"20:00")
                floating_timer_label.config(text="20:00")
                floating_timer_label.place(x=MINUTE_X, y=MINUTE_Y)
                condition_checker = variable
                check_mark.config(text="✔✔✔✔")
                check_mark.place(x=60, y=290)
                reps = 1
            elif reps % 2 == 1:
                if reps == 1:
                    check_mark.config(text="")
                timer_label.config(text="Work", fg=RED)
                count_down(work_sec)
                reps += 1

            else:
                if reps == 2:
                    check_mark.config(text="✔")
                    check_mark.place(x=90, y=290)
                elif reps == 4:
                    check_mark.config(text="✔✔")
                    check_mark.place(x=80, y=290)
                elif reps == 6:
                    check_mark.config(text="✔✔✔")
                    check_mark.place(x=70, y=290)
                BREAK_SOUND.play()
                variable = condition_checker
                condition_checker = False
                start_short_break = True
                pause_timer()
                # if condition_checker:
                #     count_down(short_break_sec)
                condition_checker = variable
                timer_label.config(text="Break", fg=PINK)
                canvas.itemconfig(timer, text=f"05:00")
                floating_timer_label.config(text="05:00")
                floating_timer_label.place(x=MINUTE_X, y=MINUTE_Y)
                reps += 1
                #TODO: reduce the volume of the break sound
    elif crono_mode_activate:
        start_timer_checker += 1
        pause_checker = 1
        condition_checker = False
        if start_timer_checker == 1:
            crono()
    else:
        tkinter.messagebox.showerror("Error", "No mode selected!")


def count_down(count):
    global second, minute, count_downer
    second = count % 60
    minute = math.floor(count / 60)
    second_int = count % 60
    minute_int = math.floor(count / 60)

    # for i in range(1, 10):
    #     if second == i:
    #         second = f"0{second}"
    # for i in range(1, 10):
    #     if minute == i:
    #         minute = f"0{minute}"
    # if second == 0:
    #     second = "00"
    # if minute == 0:
    #     minute = "00"
    canvas.itemconfig(timer, text=f"{minute:02d}:{second:02d}")
    floating_timer_label.config(text=f"{minute:02d}:{second:02d}")
    floating_timer_label.place(x=MINUTE_X, y=MINUTE_Y)

    second = second_int
    minute = minute_int
    if count > 0:
        global count_downer
        # you can change the speed of countdown here
        count_downer = root.after(1000, count_down, count - 1)
    else:
        global start_timer_checker
        start_timer_checker = 0
        start_timer()


def pause_timer():
    # if pause_checker == 1:
    global pomodoro_mode_activate, crono_mode_activate, resume, count_downer, count_upper, minute, second, paused,start_short_break, start_long_break,short_break_sec, long_break_sec
    if pomodoro_mode_activate:
        if not condition_checker:
            print("hiiiiiiiiii")
            root.after_cancel(count_downer)
            second_int = second
            minute_int = minute
            paused = True
            resume += 1
            # for i in range(1, 10):
            #     if second == i:
            #         second = f"0{second}"
            # for i in range(1, 10):
            #     if minute == i:
            #         minute = f"0{minute}"
            # if second == 0:
            #     second = "00"
            # if minute == 0:
            #     minute = "00"
            canvas.itemconfig(timer, text=f"{minute:02d}:{second:02d}")
            floating_timer_label.config(text=f"{minute:02d}:{second:02d}")
            floating_timer_label.place(x=MINUTE_X, y=MINUTE_Y)

            second = second_int
            minute = minute_int
            timer_label.config(text=f"Paused", fg=DEEP_BLUE)
            pause_button.config(text=f"Resume")
            if resume == 2:
                paused = False
                resume = 0
                pause_button.config(text=f"Pause")
                if start_short_break:
                    start_short_break = False
                    count_down(SHORT_BREAK_MIN * 60 + second)
                    timer_label.config(text="Break", fg=PINK)
                    root.after(301000, pause_timer)
                elif start_long_break:
                    start_long_break = False
                    count_down(LONG_BREAK_MIN * 60 + second)
                    timer_label.config(text="Break", fg=PINK)
                    root.after(1201000, pause_timer)
                else:
                    count_down(minute * 60 + second)
                    timer_label.config(text="Work", fg=RED)
                print("hi")


    elif crono_mode_activate:
        if not condition_checker:
            root.after_cancel(count_upper)
            timer_label.config(text=f"Paused", fg=DEEP_BLUE)
            pause_button.config(text=f"Resume")
            second_int = second
            minute_int = minute
            paused = True
            resume += 1
            # for i in range(1, 10):
            #     if second == i:
            #         second = f"0{second}"
            # for i in range(1, 10):
            #     if minute == i:
            #         minute = f"0{minute}"
            # if second == 0:
            #     second = "00"
            # if minute == 0:
            #     minute = "00"
            if show_hours:

                canvas.itemconfig(timer, text=f"{hours:02d}:{minute:02d}:{second:02d}")
                floating_timer_label.config(text=f"{hours:02d}:{minute:02d}:{second:02d}")
                floating_timer_label.place(x=HOURS_X, y=HOURS_Y)
            elif not show_hours:
                canvas.itemconfig(timer, text=f"{minute:02d}:{second:02d}")
                floating_timer_label.config(text=f"{minute:02d}:{second:02d}")
                floating_timer_label.place(x=MINUTE_X, y=MINUTE_Y)
            else:
                print("Error: There's a problem with the show_hours")
                return
            if resume == 2:
                paused = False
                resume = 0
                print("hi")
                timer_label.config(text="WORK", fg=RED)
                pause_button.config(text=f"Pause")
                count_upper = root.after(500, crono)
    else:
        print("Error: No mode selected")


def save_data():
    global hours, minute, second, crono_mode_activate, show_hours, saved_data, crono_reset, paused
    if not paused:
        pause_timer()
    if crono_mode_activate:
        crono_reset = False
        with open(TIME_CSV_PATH, mode='a') as file:
            file.write(f"{hours},{minute},{second}\n")

        if show_hours:
            saved_note = askstring('Save your note', 'Write your note:')
            if saved_note == "pass" or saved_note == "":
                return
            if saved_note != "":
                showinfo("Saved!", 'Your note: {}'.format(saved_note))
            saved_data["date"].append(dt.datetime.now().strftime("%Y-%m-%d"))
            saved_data["time"].append(f"{hours:02d}:{minute:02d}:{second:02d}")
            saved_data["notes"].append(saved_note)
            print("lalaalalal")
        else:
            # add_note = tkinter.messagebox.Messagebox("Add note:", f"Time: {minute:02d}:{second:02}")
            saved_note = askstring('Save your note', 'Write your note:')
            if saved_note == "pass" or saved_note == "":
                return
            if saved_note != "":
                showinfo("Saved!", 'Your note: {}'.format(saved_note))
            saved_data["date"].append(dt.datetime.now().strftime("%Y-%m-%d"))
            saved_data["time"].append(f"{minute:02d}:{second:02d}")
            saved_data["notes"].append(saved_note)
        # when pressing the 'Save' button, it saves the data to a CSV file and for not to do overwrite the file:
        try:
            print(saved_data)
            with open(SAVE_FILE_NAME, 'a', encoding='utf-8') as file:
                # writer = csv.writer(file)
                if not show_hours:
                    file.write(
                        f"\n{dt.datetime.now().strftime("%m/%d/%Y")}\n{minute:02d}:{second:02d} {saved_note}\n")
                else: # ? 'Save your note', 'Write your note: ")'
                    file.write(
                        f"\n{dt.datetime.now().strftime("%m/%d/%Y")}\n{hours:02d}:{minute:02d}:{second:02d} {saved_note}\n")
        except e:
            print(f"!!!!!!!!!!!! {e}")
        # [f"\n{dt.datetime.now().strftime("%m/%d/%Y")}" f"\n{hours:02d}:{minute:02d}:{second:02d} ", saved_note])

        # It's actually unpause the timer
    else:
        tkinter.messagebox.showerror("Error", "You need to be in stopwatch mode to use save button.")
    # save this data to a pixela website
    try:
        if crono_mode_activate():
            connect_to_pixela()
    except requests.exceptions.ConnectionError:
        print("Connection Error: Unable to connect to Pixela.")
        time.sleep(1)
        connect_to_pixela()
    except Exception as e:
        print(f"An error occurred: {e}")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("gh auth MODORO")
root.config(padx=100, pady=50, bg=YELLOW)
ico = Image.open(APP_ICON_PATH) 
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.geometry("+700+300") 
# ---------------------------- FLOATING WINDOW SETUP ------------------------------- #
class DraggableWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Draggable Window")
        # self.geometry("300x300")
        
        # Bind mouse events to the window
        self.bind("<Button-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        
        # Load the image and keep a reference to it
        self.image = ImageTk.PhotoImage(Image.open(FLOATING_IMAGE_PATH))
        label = Label(self, image=self.image, bg='white', highlightthickness=0)
        self.overrideredirect(True)
        self.geometry("+250+250")
        self.lift()
        self.wm_attributes("-topmost", True)
        # self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")
        label.pack()

        self.start_x = 0
        self.start_y = 0

    def on_press(self, event):
        # Record the start position of the mouse
        self.start_x = event.x_root
        self.start_y = event.y_root

    def on_drag(self, event):
        # Calculate the distance moved
        delta_x = event.x_root - self.start_x
        delta_y = event.y_root - self.start_y
        
        # Move the window
        new_x = self.winfo_x() + delta_x
        new_y = self.winfo_y() + delta_y
        
        self.geometry(f"+{new_x}+{new_y}")
        
        # Update the start position
        self.start_x = event.x_root
        self.start_y = event.y_root

# Create the window
window = DraggableWindow()  # Hide the main window
window.configure(bg='')
window.overrideredirect(True)
window.resizable(False, False)
window.geometry("+1150+440")

floating_timer_label = Label(window, text="00:00", font=(FONT_NAME, 28, "bold"), foreground=WHITE, background=TOMATO_COLOR)
floating_timer_label.pack()
floating_timer_label.place(x=MINUTE_X, y=MINUTE_Y)

# Kegan Software
logo = Canvas(width=600, height=224, bg=YELLOW, highlightthickness=0)
logo_img = PhotoImage(file=LOGO_IMAGE_PATH)
logo.create_image(300, 112, image=logo_img)
logo.grid(column=1, row=0)
logo.place(x=-300, y=230)

# Tomato
canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=MAIN_IMAGE_PATH)
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# labels
timer_label = Label(text="TIMER", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

modes_label = Label(text="Modes", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=ORANGE)
modes_label.grid(column=1, row=0)
modes_label.place(x=200, y=-50)

check_mark = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)
check_mark.place(x=120, y=300)

# buttons
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
start_button.place(x=-30, y=291)

pause_button = Button(text="Pause", command=pause_timer, highlightthickness=0)
pause_button.grid(column=0, row=2)
pause_button.place(x=4, y=291)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)
reset_button.place(x=175, y=291)

save_button = Button(text="Save", highlightthickness=0, command=save_data)
save_button.grid(column=2, row=2)
save_button.place(x=213, y=291)

checked_state = IntVar()
checkbutton = Checkbutton(text="SmallWindow", variable=checked_state, command=floating_window, background=YELLOW)
checkbutton.place(x=200, y=20)

# radio buttons
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Pomodoro", value=1, variable=radio_state, command=pomodoro_mode, bg=YELLOW,
                           highlightthickness=0)
radiobutton2 = Radiobutton(text="Stopwatch", value=2, variable=radio_state, command=crono_mode, bg=YELLOW,
                           highlightthickness=0)
radiobutton1.place(x=200, y=-20)
radiobutton2.place(x=200, y=-0)

# Floating timer remebers the mode
window.withdraw()
try:
    with open(FLOATING_WINDOW_CHECKER_PATH, "r") as file:
        floating_window_boolean = file.readline()
        print(floating_window_boolean)
        floating_window(check = floating_window_boolean)
except FileNotFoundError as e:
    with open(FLOATING_WINDOW_CHECKER_PATH, "w") as file:
        file.write("")

root.mainloop()