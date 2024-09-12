# watch_reload.py
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command, shell=True)

    def on_any_event(self, event):
        if event.event_type in {'modified', 'created', 'moved'}:
            print("Change detected, restarting...")
            self.process.terminate()
            self.process = subprocess.Popen(self.command, shell=True)

if __name__ == "__main__":
    script_to_run = "python your_script.py"  # Replace with your Tkinter script
    event_handler = ChangeHandler(script_to_run)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
