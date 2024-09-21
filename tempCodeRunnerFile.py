
import pywhatkit as kit
import datetime
import time
import os
import pyautogui
from tkinter import Tk, filedialog, messagebox
import os

def schedule_image():
    """
    Schedule a WhatsApp image to be sent at a specific time with user inputs.
    This version ensures the file selection window is on top, shows the file size, and includes a fail-safe mechanism.
    """
    # Step 1: Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

    # Step 2: Get user input for country code and phone number
    country_code = input("Enter country code (e.g., +91 for India): ")
    phone_number = input("Enter mobile number: ")

    # Step 2.1: Create a Tkinter root window (invisible) and open file dialog on top
    root = Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)  # Ensure the file dialog is on top

    # Open file dialog and allow the user to select an image
    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
    
    # Check if no image is selected
    if not image_path:
        print("No image selected. Exiting.")
        return

    # Step 2.2: Display the image size
    image_size = os.path.getsize(image_path) / 1024  # Convert to KB
    print(f"Selected image size: {image_size:.2f} KB")

    # Step 2.3: Get an optional caption for the image
    caption = input("Enter a caption for the image (or press Enter to skip): ")

    # Combine country code and phone number
    full_phone_number = country_code + phone_number

    # Step 3: Get and validate the time input (24-hour format)
    while True:
        try:
            time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
            hour, minute = map(int, time_input.split(':'))

            # Validate the time
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                break
            else:
                print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
        except ValueError:
            print("Invalid format. Please enter the time in HH:MM format.")

    # Step 4: Calculate scheduled time
    now = datetime.datetime.now()
    scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    # If the scheduled time is in the past, adjust it to the next day
    if scheduled_time < now:
        scheduled_time += datetime.timedelta(days=1)

    print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

    # Step 5: Wait until the scheduled time
    while datetime.datetime.now() < scheduled_time:
        time.sleep(1)  # Sleep for 1 second until scheduled time is reached

    # Step 6: Open WhatsApp Web and send the image
    print("\nOpening WhatsApp Web...")
    kit.sendwhats_image(full_phone_number, image_path, caption=caption)

    # Step 7: Fail-safe: After WhatsApp opens, wait 5 seconds and press 'Enter' to ensure the image is sent
    time.sleep(5)  # Wait for 5 seconds to ensure WhatsApp is loaded
    pyautogui.press('enter')  # Simulate pressing 'Enter' to send the message

    print("Image sent successfully!")

# Run the scheduling function
schedule_image()