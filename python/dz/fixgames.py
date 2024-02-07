import os
import time
import psutil
import json
from tkinter import filedialog
from tkinter import Tk

def check_if_process_running(process_names):
    for proc in psutil.process_iter():
        try:
            for process_name in process_names:
                if process_name.lower() in proc.name().lower():
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def close_explorer():
    os.system("taskkill /f /im explorer.exe")

def start_explorer():
    os.system("start explorer.exe")

def load_games():
    try:
        with open('games.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_games(games):
    with open('games.json', 'w') as f:
        json.dump(games, f)

def add_game_from_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])  # Open the file dialog
    if file_path:
        game_exe = os.path.basename(file_path)
        print(f"Добавлена игра: {game_exe}")
        return game_exe
    else:
        print("Файл не выбран.")
        return None

# Load the list of games
games = load_games()

# If the list is empty, ask the user to add a game
if not games:
    game_exe = add_game_from_file()
    if game_exe is not None:
        games.append(game_exe)

explorer_running = True

while True:
    if check_if_process_running(games):
        if explorer_running:
            close_explorer()
            explorer_running = False
    else:
        if not explorer_running:
            start_explorer()
            explorer_running = True
    time.sleep(1)

# Save the list of games
save_games(games)