import datetime
import time
import os
import pyautogui
import webbrowser as web
from tkinter import Tk, filedialog

def schedule_image():
    """
    Schedule a WhatsApp image to be sent at a specific time using pyautogui to automate the upload process.
    This version removes the caption feature.
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

    # Step 6: Open WhatsApp Web
    print("\nOpening WhatsApp Web...")
    web.open(f"https://web.whatsapp.com/send?phone={full_phone_number}")
    time.sleep(15)  # Wait for WhatsApp Web to load

    # Step 7: Automate the file upload
    print("Uploading the image...")

    # Step 7.1: Click on the attachment icon (paperclip)
    pyautogui.click(x=1300, y=950)  # Adjust x, y coordinates based on your screen resolution
    time.sleep(2)  # Wait for the file upload window to appear
    
    # Step 7.2: Type the image path in the file upload dialog and hit 'Enter'
    pyautogui.write(image_path)
    pyautogui.press('enter')

    time.sleep(3)  # Wait for file to load into WhatsApp

    # Step 7.3: Press 'Enter' to send the message
    pyautogui.press('enter')

    print("Image sent successfully!")

# Run the scheduling function
schedule_image()



# import datetime
# import time
# import os
# import pyautogui
# import webbrowser as web
# from tkinter import Tk, filedialog

# def schedule_image():
#     """
#     Schedule a WhatsApp image to be sent at a specific time using pyautogui to automate the upload process.
#     """
#     # Step 1: Clear the terminal screen
#     os.system('cls' if os.name == 'nt' else 'clear')

#     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

#     # Step 2: Get user input for country code and phone number
#     country_code = input("Enter country code (e.g., +91 for India): ")
#     phone_number = input("Enter mobile number: ")

#     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog on top
#     root = Tk()
#     root.withdraw()  # Hide the root window
#     root.attributes('-topmost', True)  # Ensure the file dialog is on top

#     # Open file dialog and allow the user to select an image
#     image_path = filedialog.askopenfilename(
#         title="Select an Image",
#         filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
#     )
    
#     # Check if no image is selected
#     if not image_path:
#         print("No image selected. Exiting.")
#         return

#     # Step 2.2: Display the image size
#     image_size = os.path.getsize(image_path) / 1024  # Convert to KB
#     print(f"Selected image size: {image_size:.2f} KB")

#     # Step 2.3: Get an optional caption for the image
#     caption = input("Enter a caption for the image (or press Enter to skip): ")

#     # Combine country code and phone number
#     full_phone_number = country_code + phone_number

#     # Step 3: Get and validate the time input (24-hour format)
#     while True:
#         try:
#             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
#             hour, minute = map(int, time_input.split(':'))

#             # Validate the time
#             if 0 <= hour <= 23 and 0 <= minute <= 59:
#                 break
#             else:
#                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
#         except ValueError:
#             print("Invalid format. Please enter the time in HH:MM format.")

#     # Step 4: Calculate scheduled time
#     now = datetime.datetime.now()
#     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

#     # If the scheduled time is in the past, adjust it to the next day
#     if scheduled_time < now:
#         scheduled_time += datetime.timedelta(days=1)

#     print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

#     # Step 5: Wait until the scheduled time
#     while datetime.datetime.now() < scheduled_time:
#         time.sleep(1)  # Sleep for 1 second until scheduled time is reached

#     # Step 6: Open WhatsApp Web
#     print("\nOpening WhatsApp Web...")
#     web.open(f"https://web.whatsapp.com/send?phone={full_phone_number}")
#     time.sleep(15)  # Wait for WhatsApp Web to load

#     # Step 7: Automate the file upload
#     print("Uploading the image...")

#     # Step 7.1: Click on the attachment icon (paperclip)
#     pyautogui.hotkey('ctrl', 'alt', 'u')  # Open the file upload dialog
#     time.sleep(2)  # Wait for the upload window to appear
    
#     # Step 7.2: Type the image path in the file upload dialog and hit 'Enter'
#     pyautogui.write(image_path)
#     pyautogui.press('enter')

#     time.sleep(3)  # Wait for file to load into WhatsApp

#     # Step 7.3: If a caption is provided, write the caption
#     if caption:
#         pyautogui.write(caption)

#     # Step 7.4: Press 'Enter' to send the message
#     pyautogui.press('enter')

#     print("Image sent successfully!")

# # Run the scheduling function
# schedule_image()



# # import pyautogui
# # import webbrowser as web
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename

# # def schedule_image():
# #     """
# #     Schedule sending an image on WhatsApp without typing the file path directly.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 2.1: Select the image file
# #     Tk().withdraw()  # Hides the root window
# #     image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

# #     if not image_path:
# #         print("No image selected. Exiting.")
# #         return

# #     # Display the size of the image file
# #     image_size = os.path.getsize(image_path) / (1024 * 1024)  # Convert size to MB
# #     print(f"\nSelected image size: {image_size:.2f} MB\n")

# #     # Step 3: Get user input for the scheduled time
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Step 4: Calculate the scheduled time
# #     now = time.localtime()
# #     scheduled_time_in_seconds = (hour * 3600 + minute * 60) - (now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec)

# #     if scheduled_time_in_seconds < 0:
# #         print("Scheduled time is in the past. Adjusting to the next day.")
# #         scheduled_time_in_seconds += 86400  # Add a day's worth of seconds

# #     print(f"Image scheduled to be sent in {scheduled_time_in_seconds // 60} minutes.")

# #     # Wait until the scheduled time
# #     time.sleep(scheduled_time_in_seconds)

# #     # Step 5: Open WhatsApp Web and send the image
# #     print("Opening WhatsApp Web...")
# #     web.open(f"https://web.whatsapp.com/send?phone={full_phone_number}")
# #     time.sleep(15)  # Give some time for WhatsApp Web to load

# #     # Step 6: Automate the process to attach and send the image
# #     print("Uploading the image...")

# #     # Simulate clicking the attachment icon (adjust position if needed)
# #     attachment_position = pyautogui.locateCenterOnScreen('attachment_icon.png', confidence=0.8)
# #     if attachment_position:
# #         pyautogui.click(attachment_position)
# #     else:
# #         print("Attachment icon not found on screen.")
# #         return

# #     time.sleep(2)  # Wait for the file upload window to appear

# #     # Let the system dialog handle the file selection
# #     pyautogui.write(image_path)
# #     pyautogui.press('enter')  # Confirm file selection

# #     time.sleep(3)  # Wait for file to load
# #     pyautogui.press('enter')  # Send the message

# #     print("Image sent successfully!")

# # # Run the scheduling function
# # schedule_image()



# # import pyautogui
# # import webbrowser as web
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename

# # def schedule_image():
# #     """
# #     Schedule sending an image on WhatsApp without using the clipboard.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 2.1: Select the image file
# #     Tk().withdraw()  # Hides the root window
# #     image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

# #     if not image_path:
# #         print("No image selected. Exiting.")
# #         return

# #     # Display the size of the image file
# #     image_size = os.path.getsize(image_path) / (1024 * 1024)  # Convert size to MB
# #     print(f"\nSelected image size: {image_size:.2f} MB\n")

# #     # Step 3: Get user input for the scheduled time
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Optional caption input
# #     # caption = input("Enter a caption for the image (optional, press Enter to skip): ")

# #     # Step 4: Calculate the scheduled time
# #     now = time.localtime()
# #     scheduled_time_in_seconds = (hour * 3600 + minute * 60) - (now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec)

# #     if scheduled_time_in_seconds < 0:
# #         print("Scheduled time is in the past. Adjusting to the next day.")
# #         scheduled_time_in_seconds += 86400  # Add a day's worth of seconds

# #     print(f"Image scheduled to be sent in {scheduled_time_in_seconds // 60} minutes.")

# #     # Wait until the scheduled time
# #     time.sleep(scheduled_time_in_seconds)

# #     # Step 5: Open WhatsApp Web and send the image
# #     print("Opening WhatsApp Web...")
# #     web.open(f"https://web.whatsapp.com/send?phone={full_phone_number}")
# #     time.sleep(15)  # Give some time for WhatsApp Web to load

# #     # Step 6: Automate the process to attach and send the image
# #     print("Uploading the image...")
    
# #     # Click the attachment icon
# #     pyautogui.hotkey('ctrl', 'alt', 'u')  # Open file upload dialog

# #     time.sleep(2)  # Wait for the upload window to appear
# #     pyautogui.write(image_path)  # Enter the image file path
# #     pyautogui.press('enter')  # Confirm file selection
    
# #     time.sleep(3)  # Wait for file to load
# #     # if caption:
# #     #     pyautogui.write(caption)  # Write the caption
# #     pyautogui.press('enter')  # Send the message

# #     print("Image sent successfully!")

# # # Run the scheduling function
# # schedule_image()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # import pyautogui
# # from tkinter import Tk, filedialog, messagebox
# # import os

# # def schedule_image():
# #     """
# #     Schedule a WhatsApp image to be sent at a specific time with user inputs.
# #     This version ensures the file selection window is on top, shows the file size, and includes a fail-safe mechanism.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog on top
# #     root = Tk()
# #     root.withdraw()  # Hide the root window
# #     root.attributes('-topmost', True)  # Ensure the file dialog is on top

# #     # Open file dialog and allow the user to select an image
# #     image_path = filedialog.askopenfilename(
# #         title="Select an Image",
# #         filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
# #     )
    
# #     # Check if no image is selected
# #     if not image_path:
# #         print("No image selected. Exiting.")
# #         return

# #     # Step 2.2: Display the image size
# #     image_size = os.path.getsize(image_path) / 1024  # Convert to KB
# #     print(f"Selected image size: {image_size:.2f} KB")

# #     # Step 2.3: Get an optional caption for the image
# #     caption = input("Enter a caption for the image (or press Enter to skip): ")

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Step 4: Calculate scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     # If the scheduled time is in the past, adjust it to the next day
# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

# #     # Step 5: Wait until the scheduled time
# #     while datetime.datetime.now() < scheduled_time:
# #         time.sleep(1)  # Sleep for 1 second until scheduled time is reached

# #     # Step 6: Open WhatsApp Web and send the image
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhats_image(full_phone_number, image_path, caption=caption)

# #     # Step 7: Fail-safe: After WhatsApp opens, wait 5 seconds and press 'Enter' to ensure the image is sent
# #     time.sleep(5)  # Wait for 5 seconds to ensure WhatsApp is loaded
# #     pyautogui.press('enter')  # Simulate pressing 'Enter' to send the message

# #     print("Image sent successfully!")

# # # Run the scheduling function
# # schedule_image()



# import pywhatkit as kit
# import datetime
# import time
# import os
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename
# import pyautogui

# def schedule_image():
#     """
#     Schedule a WhatsApp image to be sent at a specific time with user inputs.
#     """
#     # Clear the terminal screen
#     os.system('cls' if os.name == 'nt' else 'clear')

#     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

#     # Get user input for country code and phone number
#     country_code = input("Enter country code (e.g., +91 for India): ")
#     phone_number = input("Enter mobile number: ")

#     # Tkinter root window (invisible) and file dialog to select image
#     Tk().withdraw()  # Hides the root window
#     image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
#     if not image_path:  # Check if the user cancels the selection
#         print("No image selected. Exiting.")
#         return

#     # Get optional caption from the user
#     caption = input("Enter a caption for the image (or press Enter to skip): ")

#     # Combine country code and phone number
#     full_phone_number = country_code + phone_number

#     # Get and validate the time input (24-hour format)
#     while True:
#         try:
#             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
#             hour, minute = map(int, time_input.split(':'))

#             # Validate the time
#             if 0 <= hour <= 23 and 0 <= minute <= 59:
#                 break
#             else:
#                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
#         except ValueError:
#             print("Invalid format. Please enter the time in HH:MM format.")

#     # Calculate scheduled time
#     now = datetime.datetime.now()
#     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

#     # If the scheduled time is in the past, adjust it to the next day
#     if scheduled_time < now:
#         scheduled_time += datetime.timedelta(days=1)

#     print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

#     # Wait until the scheduled time
#     while datetime.datetime.now() < scheduled_time:
#         time.sleep(1)  # Sleep for 1 second

#     # Open WhatsApp Web and send the image
#     print("\nOpening WhatsApp Web...")
#     kit.sendwhats_image(full_phone_number, image_path, caption=caption)

#     # Wait for 5 seconds to ensure WhatsApp Web is open
#     time.sleep(5)

#     # Fail-safe: Simulate pressing 'Enter' if the image isn't sent automatically
#     print("Sending the image...")
#     time.sleep(10)  # Wait for WhatsApp to process
#     pyautogui.press('enter')  # Simulates hitting 'Enter' to confirm message

#     print("Image sent successfully!")

# # Run the scheduling function
# schedule_image()


# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename
# # import win32clipboard as wc
# # from PIL import ImageGrab

# # def copy_image_to_clipboard(image_path):
# #     """
# #     Copies the selected image to the clipboard so that it can be pasted into WhatsApp.
# #     """
# #     # Open the image and copy it to the clipboard
# #     image = ImageGrab.grabclipboard()  # Take the image from the clipboard
# #     img = ImageGrab.grab(bbox=None)
# #     img.show()

# #     wc.OpenClipboard()
# #     wc.EmptyClipboard()
# #     wc.SetClipboardData(wc.CF_DIB, img.tobytes())
# #     wc.CloseClipboard()

# # def schedule_image():
# #     """
# #     Schedule a WhatsApp image to be sent at a specific time with user inputs.
# #     The terminal screen is cleared upon running.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog as a pop-up
# #     root = Tk()  # Create root window
# #     root.withdraw()  # Hide the root window
# #     root.attributes('-topmost', True)  # Ensure the file dialog is on top of all other windows

# #     # Open the file dialog to select an image
# #     image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
# #     # Destroy the root window after selection
# #     root.destroy()

# #     if not image_path:  # Check if the user cancels the selection
# #         print("No image selected. Exiting.")
# #         return

# #     # Optional: Ask for caption input (if any)
# #     caption = input("Enter a caption for the image (optional, press Enter to skip): ")

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Step 4: Calculate scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     # If the scheduled time is in the past, adjust it to the next day
# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     # Step 5: Add a buffer of 3 minutes to ensure WhatsApp Web has enough time to load
# #     min_buffer_time = 3  # Buffer time in minutes
# #     scheduled_time += datetime.timedelta(minutes=min_buffer_time)

# #     print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')} with a {min_buffer_time}-minute buffer.")

# #     # Step 6: Active countdown until the scheduled time
# #     while datetime.datetime.now() < scheduled_time:ūC:/Users/pakac/OneDrive/ictures/Screenshots/Screenshot (23).png

# #         remaining_time = scheduled_time - datetime.datetime.now()
# #         hours, remainder = divmod(remaining_time.seconds, 3600)
# #         minutes, seconds = divmod(remainder, 60)
# #         print(f"\rTime remaining: {hours:02}:{minutes:02}:{seconds:02}", end="")
# #         time.sleep(1)  # Sleep for 1 second and update countdown

# #     # Step 7: Open WhatsApp Web and send the image
# #     print("\nOpening WhatsApp Web...")
# #     copy_image_to_clipboard(image_path)  # Copy image to clipboard
    
# #     if caption.strip():
# #         # Send with caption if provided
# #         kit.sendwhats_image(full_phone_number, image_path, caption=caption, wait_time=min_buffer_time)
# #     else:
# #         # Send without caption
# #         kit.sendwhats_image(full_phone_number, image_path, wait_time=min_buffer_time)

# #     # Wait for 5 seconds to ensure WhatsApp Web is open
# #     time.sleep(5)
# #     print("Image sent successfully!")

# # # Run the scheduling function
# # schedule_image()



# import pywhatkit as kit
# import datetime
# import time
# import os
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename
# import win32clipboard as wc
# from PIL import ImageGrab

# def copy_image_to_clipboard(image_path):
#     """
#     Copies the selected image to the clipboard so that it can be pasted into WhatsApp.
#     """
#     # Open the image and copy it to the clipboard
#     image = ImageGrab.grabclipboard()  # Take the image from the clipboard
#     img = ImageGrab.grab(bbox=None)
#     img.show()

#     wc.OpenClipboard()
#     wc.EmptyClipboard()
#     wc.SetClipboardData(wc.CF_DIB, img.tobytes())
#     wc.CloseClipboard()

# def schedule_image():
#     """
#     Schedule a WhatsApp image to be sent at a specific time with user inputs.
#     The terminal screen is cleared upon running.
#     """
#     # Step 1: Clear the terminal screen
#     os.system('cls' if os.name == 'nt' else 'clear')

#     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

#     # Step 2: Get user input for country code and phone number
#     country_code = input("Enter country code (e.g., +91 for India): ")
#     phone_number = input("Enter mobile number: ")

#     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog as a pop-up
#     root = Tk()  # Create root window
#     root.withdraw()  # Hide the root window
#     root.attributes('-topmost', True)  # Ensure the file dialog is on top of all other windows

#     # Open the file dialog to select an image
#     image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
#     # Destroy the root window after selection
#     root.destroy()

#     if not image_path:  # Check if the user cancels the selection
#         print("No image selected. Exiting.")
#         return

#     # Combine country code and phone number
#     full_phone_number = country_code + phone_number

#     # Step 3: Get and validate the time input (24-hour format)
#     while True:
#         try:
#             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
#             hour, minute = map(int, time_input.split(':'))

#             # Validate the time
#             if 0 <= hour <= 23 and 0 <= minute <= 59:
#                 break
#             else:
#                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
#         except ValueError:
#             print("Invalid format. Please enter the time in HH:MM format.")

#     # Step 4: Calculate scheduled time
#     now = datetime.datetime.now()
#     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

#     # If the scheduled time is in the past, adjust it to the next day
#     if scheduled_time < now:
#         scheduled_time += datetime.timedelta(days=1)

#     # Step 5: Add a buffer of at least 7 minutes to ensure WhatsApp Web has enough time to load
#     min_buffer_time = 7  # Minimum buffer time in minutes
#     wait_time = max(min_buffer_time, 3)  # Ensure at least 7 minutes is given

#     print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')} with a {wait_time}-minute buffer.")

#     # Step 6: Open WhatsApp Web and send the image
#     print("\nOpening WhatsApp Web...")
#     copy_image_to_clipboard(image_path)  # Copy image to clipboard
#     kit.sendwhats_image(full_phone_number, image_path, wait_time=wait_time)

#     # Wait for 5 seconds to ensure WhatsApp Web is open
#     time.sleep(5)
#     print("Image sent successfully!")

# # Run the scheduling function
# schedule_image()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename

# # def schedule_image():
# #     """
# #     Schedule a WhatsApp image to be sent at a specific time with user inputs.
# #     The terminal screen is cleared upon running.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog as a pop-up
# #     root = Tk()  # Create root window
# #     root.withdraw()  # Hide the root window
# #     root.attributes('-topmost', True)  # Ensure the file dialog is on top of all other windows

# #     # Open the file dialog to select an image
# #     image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
# #     # Destroy the root window after selection
# #     root.destroy()

# #     if not image_path:  # Check if the user cancels the selection
# #         print("No image selected. Exiting.")
# #         return

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Step 4: Calculate scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     # If the scheduled time is in the past, adjust it to the next day
# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     # Step 5: Add a buffer of at least 7 minutes to ensure WhatsApp Web has enough time to load
# #     min_buffer_time = 7  # Minimum buffer time in minutes
# #     wait_time = max(min_buffer_time, 3)  # Ensure at least 7 minutes is given

# #     print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')} with a {wait_time}-minute buffer.")

# #     # Step 6: Open WhatsApp Web and send the image
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhats_image(full_phone_number, image_path, wait_time=wait_time)

# #     # Wait for 5 seconds to ensure WhatsApp Web is open
# #     time.sleep(5)
# #     print("Image sent successfully!")

# # # Run the scheduling function
# # schedule_image()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename

# # def schedule_image():
# #     """
# #     Schedule a WhatsApp image to be sent at a specific time with user inputs.
# #     The terminal screen is cleared upon running.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 3: Create a Tkinter root window (invisible) and open file dialog as a pop-up
# #     root = Tk()  # Create root window
# #     root.withdraw()  # Hide the root window
# #     root.attributes('-topmost', True)  # Ensure the file dialog is on top of all other windows

# #     # Open the file dialog to select an image
# #     image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
# #     # Destroy the root window after selection
# #     root.destroy()

# #     if not image_path:  # Check if the user cancels the selection
# #         print("No image selected. Exiting.")
# #         return

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 4: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Step 5: Calculate scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     # If the scheduled time is in the past, adjust it to the next day
# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     # Add a buffer of 3 minutes to ensure WhatsApp Web has enough time to load
# #     wait_time = 3  # wait time in minutes
# #     scheduled_time += datetime.timedelta(minutes=wait_time)

# #     print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

# #     # Step 6: Open WhatsApp Web and send the image
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhats_image(full_phone_number, image_path, wait_time=wait_time)

# #     # Wait for 5 seconds to ensure WhatsApp Web is open
# #     time.sleep(5)
# #     print("Image sent successfully!")

# # # Run the scheduling function
# # schedule_image()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename

# # def schedule_image():
# #     """
# #     Schedule a WhatsApp image to be sent at a specific time with user inputs,
# #     including an active countdown display. The terminal screen is cleared upon running.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Image Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog
# #     Tk().withdraw()  # Hides the root window
# #     image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    
# #     if not image_path:  # Check if the user cancels the selection
# #         print("No image selected. Exiting.")
# #         return

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the image (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Step 4: Calculate scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     # If the scheduled time is in the past, adjust it to the next day
# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     # Add a buffer of 3 minutes to ensure WhatsApp Web has enough time to load
# #     wait_time = 3  # wait time in minutes
# #     scheduled_time += datetime.timedelta(minutes=wait_time)

# #     print(f"Image to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

# #     # Step 5: Active countdown until the scheduled time
# #     while datetime.datetime.now() < scheduled_time:
# #         remaining_time = scheduled_time - datetime.datetime.now()
# #         hours, remainder = divmod(remaining_time.seconds, 3600)
# #         minutes, seconds = divmod(remainder, 60)

# #         # Color coding for countdown
# #         if remaining_time.seconds <= 30:
# #             color_code = "\033[91m"  # Red
# #         elif remaining_time.seconds <= 60:
# #             color_code = "\033[93m"  # Orange
# #         else:
# #             color_code = "\033[0m"    # Reset to default color
        
# #         print(f"\r{color_code}Time remaining: {hours:02}:{minutes:02}:{seconds:02}\033[0m", end="")
# #         time.sleep(1)  # Sleep for 1 second and update countdown

# #     # Step 6: Open WhatsApp Web and send the image
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhats_image(full_phone_number, image_path, wait_time=wait_time)

# #     # Wait for 5 seconds to ensure WhatsApp Web is open
# #     time.sleep(5)
# #     print("Image sent successfully!")

# # # Run the scheduling function
# # schedule_image()
