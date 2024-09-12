import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Dummy API responses
def get_dummy_epic_response(epic_no):
    # Dummy response based on EPIC number
    return f"Dummy EPIC Response for {epic_no}: Voter ID found."

def get_dummy_details_response(state, first_name, last_name, relative_first_name, relative_last_name):
    # Dummy response based on input details
    return (f"Dummy Details Response:\n"
            f"State: {state}\n"
            f"First Name: {first_name}\n"
            f"Last Name: {last_name}\n"
            f"Relative First Name: {relative_first_name}\n"
            f"Relative Last Name: {relative_last_name}\n"
            f"Voter details found.")

def fetch_by_epic(epic_no):
    try:
        # Simulate API call and get dummy response
        result = get_dummy_epic_response(epic_no)
        result_label.config(text=result)
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def fetch_by_details(state, first_name, last_name, relative_first_name, relative_last_name):
    if not first_name or not state:
        messagebox.showerror("Input Error", "State and First Name are mandatory.")
        return
    
    try:
        # Simulate API call and get dummy response
        result = get_dummy_details_response(state, first_name, last_name, relative_first_name, relative_last_name)
        result_label.config(text=result)
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def on_search_by_epic():
    clear_widgets()
    epic_label.pack(pady=10)
    epic_entry.pack(pady=10)
    search_epic_button.pack(pady=10)
    clear_button.pack(pady=10)

def on_search_by_details():
    clear_widgets()
    state_label.pack(pady=10)
    state_combobox.pack(pady=10)
    first_name_label.pack(pady=10)
    first_name_entry.pack(pady=10)
    last_name_label.pack(pady=10)
    last_name_entry.pack(pady=10)
    relative_first_name_label.pack(pady=10)
    relative_first_name_entry.pack(pady=10)
    relative_last_name_label.pack(pady=10)
    relative_last_name_entry.pack(pady=10)
    search_details_button.pack(pady=10)
    clear_button.pack(pady=10)

def clear_widgets():
    epic_label.pack_forget()
    epic_entry.pack_forget()
    search_epic_button.pack_forget()
    state_label.pack_forget()
    state_combobox.pack_forget()
    first_name_label.pack_forget()
    first_name_entry.pack_forget()
    last_name_label.pack_forget()
    last_name_entry.pack_forget()
    relative_first_name_label.pack_forget()
    relative_first_name_entry.pack_forget()
    relative_last_name_label.pack_forget()
    relative_last_name_entry.pack_forget()
    search_details_button.pack_forget()
    result_label.pack_forget()
    clear_button.pack_forget()

def on_epic_search_click():
    epic_no = epic_entry.get()
    if epic_no:
        fetch_by_epic(epic_no)
    else:
        result_label.config(text="EPIC No cannot be empty.")

def on_details_search_click():
    state = state_combobox.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    relative_first_name = relative_first_name_entry.get()
    relative_last_name = relative_last_name_entry.get()
    fetch_by_details(state, first_name, last_name, relative_first_name, relative_last_name)

# Create the main window
root = tk.Tk()
root.title("ECI Voter Details")
print(f"Voter ECI Application Running...")

# Widgets
search_by_details_button = tk.Button(root, text="Search By Details", command=on_search_by_details)
search_by_epic_button = tk.Button(root, text="Search By EPIC", command=on_search_by_epic)

epic_label = tk.Label(root, text="Enter EPIC No:")
epic_entry = tk.Entry(root)
search_epic_button = tk.Button(root, text="Search", command=on_epic_search_click)

state_label = tk.Label(root, text="Select Your State:")
states = [
    ("Select Your State", ""), ("Andaman & Nicobar Islands", "U01"), ("Andhra Pradesh", "S01"),
    ("Arunachal Pradesh", "S02"), ("Assam", "S03"), ("Bihar", "S04"), ("Chandigarh", "U02"),
    ("Chattisgarh", "S26"), ("Dadra & Nagar Haveli and Daman & Diu", "U03"), ("Goa", "S05"),
    ("Gujarat", "S06"), ("Haryana", "S07"), ("Himachal Pradesh", "S08"), ("Jammu and Kashmir", "U08"),
    ("Jharkhand", "S27"), ("Karnataka", "S10"), ("Kerala", "S11"), ("Ladakh", "U09"),
    ("Lakshadweep", "U06"), ("Madhya Pradesh", "S12"), ("Maharashtra", "S13"), ("Manipur", "S14"),
    ("Meghalaya", "S15"), ("Mizoram", "S16"), ("Nagaland", "S17"), ("NCT OF Delhi", "U05"),
    ("Odisha", "S18"), ("Puducherry", "U07"), ("Punjab", "S19"), ("Rajasthan", "S20"),
    ("Sikkim", "S21"), ("Tamil Nadu", "S22"), ("Telangana", "S29"), ("Tripura", "S23"),
    ("Uttar Pradesh", "S24"), ("Uttarakhand", "S28"), ("West Bengal", "S25")
]
state_combobox = ttk.Combobox(root, values=[state[0] for state in states], state="readonly")
state_combobox.set("Select Your State")

first_name_label = tk.Label(root, text="First Name:")
first_name_entry = tk.Entry(root)
last_name_label = tk.Label(root, text="Last Name:")
last_name_entry = tk.Entry(root)
relative_first_name_label = tk.Label(root, text="Relative First Name:")
relative_first_name_entry = tk.Entry(root)
relative_last_name_label = tk.Label(root, text="Relative Last Name:")
relative_last_name_entry = tk.Entry(root)

search_details_button = tk.Button(root, text="Search", command=on_details_search_click)
clear_button = tk.Button(root, text="Clear", command=clear_widgets)

result_label = tk.Label(root, text="")

# Initial widgets
search_by_epic_button.pack(pady=10)
search_by_details_button.pack(pady=10)

root.mainloop()
