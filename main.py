import tkinter as tk
import numpy as np


def calculate_luminosity(star_type):  # Returns the luminosity score relative to the sun based on the star type
    if star_type.lower() == 'm':
        return 0.04
    elif star_type.lower() == 'k':
        return 0.34
    elif star_type.lower() == 'g':
        return 1.0
    elif star_type.lower() == 'f':
        return 3.25
    elif star_type.lower() == 'a':
        return 15
    elif star_type.lower() == 'b':
        return 15000
    elif star_type.lower() == 'o':
        return 30000
    else:
        return 0


def habitable_zone_boundaries(luminosity):  # Takes in the luminosity score and returns the inner and out radius
    r_inner = np.sqrt(luminosity / 1.1)
    r_outer = np.sqrt(luminosity / 0.53)
    return r_inner, r_outer


def habitability_score(orbital_distance, r_inner, r_outer):  # Calculates the habitable score from all info
    r_center = (r_inner + r_outer) / 2
    width = r_outer - r_inner
    if round(r_inner, 2) <= orbital_distance <= round(r_outer, 2):
        if orbital_distance == round(r_inner, 2) or orbital_distance == round(r_outer, 2):
            return 1
        else:
            return 100 * (1 - 2 * np.abs(orbital_distance - r_center) / width)
    else:
        return 0


def calculate():  # Connects the user input to the calculating functions
    star_type = star_type_entry.get()
    orbital_distance = float(orbital_distance_entry.get())
    luminosity = calculate_luminosity(star_type)
    r_inner, r_outer = habitable_zone_boundaries(luminosity)
    score = habitability_score(orbital_distance, r_inner, r_outer)

    result_text = f"Habitable Zone: {r_inner:.2f} AU to {r_outer:.2f} AU\n"
    result_text += f"Habitability Score: {score:.2f}"
    results_label.config(text=result_text)


# Set up the main window
root = tk.Tk()
root.title("Planetary Habitability Calculator for ASTRO-C12!")
# Layout/GUI stuff:
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)
tk.Label(frame, text="Enter your star type (M, K, G, F, A, B, O):").pack()
star_type_entry = tk.Entry(frame)
star_type_entry.pack()
tk.Label(frame, text="Enter your orbital distance (in AU):").pack()
orbital_distance_entry = tk.Entry(frame)
orbital_distance_entry.pack()
calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.pack()
results_label = tk.Label(frame, text="")
results_label.pack()
root.mainloop()
