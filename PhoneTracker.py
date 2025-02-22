import phonenumbers
import tkinter as tk
from phonenumbers import geocoder, carrier, number_type
from tkinter import messagebox

# Function to get details of the phone number
def get_number_details():
    phone_number = entry.get().strip()
    
    try:
        parsed_number = phonenumbers.parse(phone_number)
        
        # Get location (Country or State)
        location = geocoder.description_for_number(parsed_number, "en")
        
        # Get carrier (Network Provider)
        carrier_name = carrier.name_for_number(parsed_number, "en")
        
        # Get card type (Mobile/Landline)
        num_type = number_type(parsed_number)
        if num_type == phonenumbers.PhoneNumberType.MOBILE:
            card_type = "Mobile"
        elif num_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            card_type = "Landline"
        else:
            card_type = "Unknown"
        
        # Display Results
        result_label.config(text=f"📍 Location: {location}\n📡 Carrier: {carrier_name}\n💳 Card Type: {card_type}", fg="white")

    except Exception as e:
        messagebox.showerror("Error", "Invalid Phone Number! Please enter a valid number with country code.")

# GUI Window Setup
root = tk.Tk()
root.title("Phone Number Tracker")
root.geometry("400x400")
root.config(bg="black")

# Heading
heading = tk.Label(root, text="📱 Phone Number Tracker", font=("Arial", 16, "bold"), fg="orange", bg="black")
heading.pack(pady=20)

# Input Field
entry = tk.Entry(root, font=("Arial", 14), width=25, fg="black", bg="orange", justify="center")
entry.pack(pady=10)
entry.insert(0, "+91 ")  # Default country code for India

# Submit Button
track_button = tk.Button(root, text="Track Number", font=("Arial", 12, "bold"), fg="black", bg="orange", command=get_number_details)
track_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="white", bg="black")
result_label.pack(pady=20)

# Run the App
root.mainloop()
