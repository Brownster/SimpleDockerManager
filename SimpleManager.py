import tkinter as tk
from tkinter import ttk
import subprocess

########################  install medusa  ############################################
def install_medusa(puid, pgid, timezone, config_path, downloads_path, tv_shows_path):
    # Pull the latest Medusa Docker image
    subprocess.run(["docker", "pull", "linuxserver/medusa:latest"])

    # Run a new Medusa container with the specified parameters
    subprocess.run([
        "docker", "run", "-d",
        "--name=medusa",
        f"-e PUID={puid}",
        f"-e PGID={pgid}",
        f"-e TZ={timezone}",
        "-p 8081:8081",
        f"-v {config_path}:/config",
        f"-v {downloads_path}:/downloads",
        f"-v {tv_shows_path}:/tv",
        "--restart", "unless-stopped",
        "lscr.io/linuxserver/medusa:latest"
    ])

def start_medusa():
    subprocess.run(["docker", "start", "medusa"])

def stop_medusa():
    subprocess.run(["docker", "stop", "medusa"])

def delete_medusa():
    subprocess.run(["docker", "rm", "medusa"])

def update_medusa():
    stop_medusa()
    delete_medusa()
    # Retrieve the existing parameters from the GUI
    puid = app.puid_entry.get()
    pgid = app.pgid_entry.get()
    timezone = app.timezone_entry.get()
    config_path = app.config_path_entry.get()
    downloads_path = app.downloads_path_entry.get()
    tv_shows_path = app.tv_shows_path_entry.get()
    # Reinstall Medusa with the updated image and existing parameters
    install_medusa(puid, pgid, timezone, config_path, downloads_path, tv_shows_path)

############################## LIDAR #######################################

def install_lidarr(puid, pgid, timezone, config_path, music_path, downloads_path):
    subprocess.run([
        "docker", "pull", "lscr.io/linuxserver/lidarr:latest"
    ])
    subprocess.run([
        "docker", "create",
        "--name=lidarr",
        f"-e PUID={puid}",
        f"-e PGID={pgid}",
        f"-e TZ={timezone}",
        "-p 8686:8686",
        f"-v {config_path}:/config",
        f"-v {music_path}:/music",
        f"-v {downloads_path}:/downloads",
        "lscr.io/linuxserver/lidarr:latest"
    ])
    subprocess.run(["docker", "start", "lidarr"])    

    
def start_lidarr():
    subprocess.run(["docker", "start", "lidarr"])

def stop_lidarr():
    subprocess.run(["docker", "stop", "lidarr"])

def delete_lidarr():
    subprocess.run(["docker", "rm", "lidarr"])

def update_lidarr():
    stop_lidarr()
    delete_lidarr()
    # Retrieve the existing parameters from the GUI
    puid = app.puid_entry.get()
    pgid = app.pgid_entry.get()
    timezone = app.timezone_entry.get()
    config_path = app.config_path_entry.get()
    music_path = app.music_path_entry.get()
    downloads_path = app.downloads_path_entry.get()
    # Reinstall Lidarr with the updated image and existing parameters
    install_lidarr(puid, pgid, timezone, config_path, music_path, downloads_path)

########################################### INSTALL SELECTED #####################
def install_selected(self):
    if self.install_medusa_var.get():
        install_medusa(
            self.puid_entry.get(),
            self.pgid_entry.get(),
            self.timezone_entry.get(),
            self.medusa_config_path_entry.get(),
            self.medusa_tv_path_entry.get(),
            self.medusa_downloads_path_entry.get()
        )
    if self.install_lidarr_var.get():
        install_lidarr(
            self.puid_entry.get(),
            self.pgid_entry.get(),
            self.timezone_entry.get(),
            self.config_path_entry.get(),
            self.music_path_entry.get(),
            self.downloads_path_entry.get()
        )






class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack()

        # Create a frame for each tab
        self.general_frame = ttk.Frame(self.notebook)
        self.medusa_frame = ttk.Frame(self.notebook)
        self.lidarr_frame = ttk.Frame(self.notebook)

        # Add the frames as tabs to the notebook
        self.notebook.add(self.general_frame, text="General")
        self.notebook.add(self.medusa_frame, text="Medusa")
        self.notebook.add(self.lidarr_frame, text="Lidarr")

        # General settings (checkboxes)
        self.install_medusa_var = tk.BooleanVar()
        self.install_lidarr_var = tk.BooleanVar()

        self.install_medusa_checkbox = ttk.Checkbutton(self.general_frame, text="Install Medusa", variable=self.install_medusa_var)
        self.install_medusa_checkbox.pack()

        self.install_lidarr_checkbox = ttk.Checkbutton(self.general_frame, text="Install Lidarr", variable=self.install_lidarr_var)
        self.install_lidarr_checkbox.pack()

        # Button to run the selected installations
        self.install_selected_button = ttk.Button(self.general_frame, text="Install Selected", command=self.install_selected)
        self.install_selected_button.pack()

        # Medusa settings
        self.medusa_label = ttk.Label(self.medusa_frame, text="Medusa Settings")
        self.medusa_label.pack()
        # ... (other Medusa widgets)

        # Lidarr settings
        self.lidarr_label = ttk.Label(self.lidarr_frame, text="Lidarr Settings")
        self.lidarr_label.pack()
        # ... (other Lidarr widgets)

    def install_selected(self):
        if self.install_medusa_var.get():
            # Call the install_medusa function with the required parameters
            pass

        if self.install_lidarr_var.get():
            # Call the install_lidarr function with the required parameters
            pass

root = tk.Tk()
root.title("Media Installer")
app = Application(master=root)
app.mainloop()
