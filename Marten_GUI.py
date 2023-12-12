import tkinter as tk


class SensorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sensor Status")
        self.attributes('-fullscreen', True)  # Gehe in den Vollbildmodus

        self.selection_frame = None
        self.sensor_frames = []

        self.sensor_statuses = {
            "Kompressor IPT": {
                "Sensor 1": "OK",
                "Sensor 2": "Warnung",
                "Sensor 3": "Fehler"
            },
            "Kompressor Ostfalia": {
                "Sensor 1": "OK",
                "Sensor 2": "OK",
                "Sensor 3": "OK"
            },
            "Device 3": {
                "Sensor 1": "Warnung",
                "Sensor 2": "OK",
                "Sensor 3": "OK"
            }
        }

        self.create_device_buttons()

    def create_device_buttons(self):
        devices = list(self.sensor_statuses.keys())
        self.selection_frame = tk.Frame(self)
        self.selection_frame.pack(padx=20, pady=20)

        for device_name in devices:
            button = tk.Button(self.selection_frame, text=device_name,
                               command=lambda dev=device_name: self.show_sensor_status(dev),
                               width=20, height=5, font=("Arial", 15))
            button.pack(padx=10, pady=(10, 60))  # Ändere hier das pady für Y-Richtung

        close_button = tk.Button(self, text="X", command=self.close_app, bg="red", fg="white", width=3, height=1,
                                 font=("Arial", 20))
        close_button.pack(side=tk.TOP, anchor=tk.NE, pady=(60, 0))  # Ändere hier das pady für Y-Richtung

    def show_sensor_status(self, selected_device):
        self.selection_frame.pack_forget()

        current_frame = tk.Frame(self)

        back_button = tk.Button(current_frame, text="Zurück", command=self.show_device_selection, width=10, height=2,
                                font=("Arial", 20))
        back_button.pack(pady=(20, 60))  # Ändere hier das pady für Y-Richtung

        sensor_labels = list(self.sensor_statuses[selected_device].keys())

        for sensor_label in sensor_labels:
            status = self.sensor_statuses[selected_device][sensor_label]
            label = tk.Label(current_frame, text=f"{sensor_label} - Status: {status}", font=("Arial", 14))
            label.pack()

        current_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        current_frame.pack()
        self.sensor_frames.append(current_frame)

    def show_device_selection(self):
        for frame in self.sensor_frames:
            frame.pack_forget()

        self.selection_frame.pack(padx=20, pady=20)

    def close_app(self):
        self.destroy()


if __name__ == "__main__":
    app = SensorApp()
    app.mainloop()
