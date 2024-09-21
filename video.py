import datetime
import time
import os
import pyautogui
import webbrowser as web
from tkinter import Tk, filedialog

def schedule_image():
    """
    Schedule a WhatsApp image to be sent at a specific time using pyautogui to automate the upload process.
    This version removes the caption feature and uses pyautogui to handle the file dialog.
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

    # Step 7.2: Simulate pressing 'ctrl+v' to paste the file path in the dialog
    pyautogui.write(image_path)  # Type the image path
    time.sleep(1)  # Small delay before pressing 'Enter'
    pyautogui.press('enter')  # Press 'Enter' to select the file

    time.sleep(3)  # Wait for file to load into WhatsApp

    # Step 7.3: Press 'Enter' to send the message
    pyautogui.press('enter')

    print("Image sent successfully!")

# Run the scheduling function
schedule_image()



# import pywhatkit as kit
# import datetime
# import time
# import os
# import shutil
# from tkinter import Tk
# from tkinter.filedialog import askopenfilenames
# import tempfile

# def schedule_documents():
#     """
#     Schedule WhatsApp document uploads to multiple recipients with user inputs.
#     This version uses temporary storage for file handling and avoids clipboard issues.
#     """
#     # Step 1: Clear the terminal screen
#     os.system('cls' if os.name == 'nt' else 'clear')

#     print("WhatsApp Document Scheduler".center(60, '-'))  # Title for clarity

#     # Step 2: Get user input for country code and phone number
#     country_code = input("Enter country code (e.g., +91 for India): ")
#     phone_number = input("Enter mobile number: ")
    
#     # Combine country code and phone number
#     full_phone_number = country_code + phone_number

#     # Step 2.1: Select multiple files
#     Tk().withdraw()  # Hides the root window
#     file_paths = askopenfilenames(title="Select Documents", filetypes=[("All Files", "*.*")])

#     if not file_paths:  # Check if the user cancels the selection
#         print("No files selected. Exiting.")
#         return

#     # Step 2.2: Create temporary directory for storing selected files
#     temp_dir = tempfile.mkdtemp()
#     total_size = 0  # Track total size of selected files

#     print("\nCopying selected files to temporary storage...\n")
    
#     for file_path in file_paths:
#         # Copy the files to the temporary directory
#         shutil.copy(file_path, temp_dir)
        
#         # Calculate total size
#         total_size += os.path.getsize(file_path)
#         print(f"Copied: {os.path.basename(file_path)} | Size: {os.path.getsize(file_path) / (1024 * 1024):.2f} MB")

#     print(f"\nTotal size of selected files: {total_size / (1024 * 1024):.2f} MB")

#     # Check if the total size exceeds WhatsApp's limit (~100 MB per file)
#     if any(os.path.getsize(file) > 100 * 1024 * 1024 for file in file_paths):
#         print("Error: One or more files exceed WhatsApp's 100 MB file limit.")
#         return

#     # Step 3: Get and validate the time input (24-hour format)
#     while True:
#         try:
#             time_input = input("Enter the time to send the documents (HH:MM in 24-hour format): ")
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

#     # Step 5: Add a buffer of 3 minutes to ensure WhatsApp Web has enough time to load
#     buffer_time = 3  # Buffer time in minutes
#     scheduled_time -= datetime.timedelta(minutes=buffer_time)

#     print(f"\nDocuments to {full_phone_number} are scheduled for {scheduled_time.strftime('%H:%M')}\n")

#     # Step 6: Open WhatsApp Web 3 minutes before scheduled time
#     while datetime.datetime.now() < scheduled_time:
#         remaining_time = (scheduled_time - datetime.datetime.now()).total_seconds()
#         time.sleep(remaining_time)  # Wait until the scheduled time

#     print("Opening WhatsApp Web...")
#     kit.sendwhatmsg(full_phone_number, '', hour, minute + buffer_time, 20, True)  # Open WhatsApp Web
    
#     # Step 7: Send the documents one by one after WhatsApp Web opens
#     for file_name in os.listdir(temp_dir):
#         file_path = os.path.join(temp_dir, file_name)
#         print(f"Sending {file_name}...")
#         kit.sendwhats_image(full_phone_number, file_path, caption="", wait_time=20)
#         time.sleep(5)  # Add delay between sending files

#     print("Documents sent successfully!")

#     # Clean up temporary files after sending
#     shutil.rmtree(temp_dir)
#     print("Temporary files cleaned up.")

# # Run the scheduling function
# schedule_documents()



# import pywhatkit as kit
# import datetime
# import time
# import os
# import threading
# import keyboard
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename

# # Global variable to control the cancellation
# cancel_process = False

# def check_cancel():
#     global cancel_process
#     keyboard.add_hotkey('ctrl+alt+2', lambda: setattr(cancel_process, 'cancel', True))

# def internet_speed_test():
#     print("Testing internet speed...")
#     time.sleep(5)  # Simulate the time taken for speed test
#     return 10  # Simulated speed in Mbps

# def schedule_video():
#     global cancel_process
#     cancel_process = False

#     # Clear the terminal screen
#     os.system('cls' if os.name == 'nt' else 'clear')

#     print("WhatsApp Video Scheduler".center(60, '-'))  # Title for clarity

#     # Get user input for country code and phone number
#     country_code = input("Enter country code (e.g., +91 for India): ")
#     phone_number = input("Enter mobile number: ")

#     # Create a Tkinter root window (invisible) and open file dialog
#     Tk().withdraw()  # Hides the root window
#     video_path = askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])

#     if not video_path:  # Check if the user cancels the selection
#         print("No video selected. Exiting.")
#         return

#     # Combine country code and phone number
#     full_phone_number = country_code + phone_number

#     # Display video file size
#     video_size = os.path.getsize(video_path) / (1024 * 1024)  # Convert to MB
#     print(f"\nFile size: {video_size:.2f} MB\n")

#     # Get and validate the time input (24-hour format)
#     while True:
#         try:
#             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
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

#     # Perform internet speed test
#     speed = internet_speed_test()
#     print(f"Estimated upload speed: {speed} Mbps")

#     # Open WhatsApp Web
#     print("\nOpening WhatsApp Web...")
#     kit.sendwhatmsg(full_phone_number, '', hour, minute - 3)  # Open WhatsApp Web 3 minutes before
#     time.sleep(10)  # Give time for WhatsApp to load

#     # Copy the video file to clipboard
#     os.system(f'clip < "{video_path}"')

#     # Notify user and start countdown
#     print("\nPress 'Ctrl+Alt+2' to cancel the process. \n")
#     while datetime.datetime.now() < scheduled_time and not cancel_process:
#         time.sleep(1)  # Sleep for a second

#         # Show a persistent notification at the top
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print("WhatsApp Video Scheduler".center(60, '-'))
#         print("\nPress 'Ctrl+Alt+2' to cancel the process.\n")

#     if not cancel_process:
#         # Wait for the scheduled time and send the video
#         print("\nUploading video...")
#         time.sleep(5)  # Allow time for the file to paste
#         keyboard.press('enter')  # Simulate pressing Enter to send the video
#         print("Video uploaded successfully!")

#     if cancel_process:
#         print("\nProcess canceled by the user.")

# # Start the cancel check in a separate thread
# threading.Thread(target=check_cancel, daemon=True).start()

# # Run the scheduling function
# schedule_video()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # import threading
# # import keyboard
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename

# # # Global variable to control the cancellation
# # cancel_process = False

# # def check_cancel():
# #     global cancel_process
# #     keyboard.add_hotkey('ctrl+alt+2', lambda: setattr(cancel_process, 'cancel', True))

# # def internet_speed_test():
# #     print("Testing internet speed...")
# #     time.sleep(5)  # Simulate the time taken for speed test
# #     return 10  # Simulated speed in Mbps

# # def schedule_video():
# #     global cancel_process
# #     cancel_process = False

# #     # Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Video Scheduler".center(60, '-'))  # Title for clarity

# #     # Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Create a Tkinter root window (invisible) and open file dialog
# #     Tk().withdraw()  # Hides the root window
# #     video_path = askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])

# #     if not video_path:  # Check if the user cancels the selection
# #         print("No video selected. Exiting.")
# #         return

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Display video file size
# #     video_size = os.path.getsize(video_path) / (1024 * 1024)  # Convert to MB
# #     print(f"\nFile size: {video_size:.2f} MB\n")

# #     # Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Calculate scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     # If the scheduled time is in the past, adjust it to the next day
# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     # Perform internet speed test
# #     speed = internet_speed_test()
# #     print(f"Estimated upload speed: {speed} Mbps")

# #     # Open WhatsApp Web
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhatmsg(full_phone_number, '', hour, minute - 3)  # Open WhatsApp Web 3 minutes before
# #     time.sleep(10)  # Give time for WhatsApp to load

# #     # Copy the video file to clipboard
# #     os.system(f'clip < "{video_path}"')

# #     # Notify user and start countdown
# #     print("\nPress 'Ctrl+Alt+2' to cancel the process. \n")
# #     while datetime.datetime.now() < scheduled_time and not cancel_process:
# #         time.sleep(1)  # Sleep for a second

# #         # Show a persistent notification at the top
# #         os.system('cls' if os.name == 'nt' else 'clear')
# #         print("WhatsApp Video Scheduler".center(60, '-'))
# #         print("\nPress 'Ctrl+Alt+2' to cancel the process.\n")

# #     if not cancel_process:
# #         # Wait for the scheduled time and send the video
# #         print("\nUploading video...")
# #         time.sleep(5)  # Allow time for the file to paste
# #         keyboard.press('enter')  # Simulate pressing Enter to send the video
# #         print("Video uploaded successfully!")

# #     if cancel_process:
# #         print("\nProcess canceled by the user.")

# # # Start the cancel check in a separate thread
# # threading.Thread(target=check_cancel, daemon=True).start()

# # # Run the scheduling function
# # schedule_video()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # import threading
# # import keyboard
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename
# # from tqdm import tqdm

# # # Global variable to control the cancellation
# # cancel_process = False

# # def check_cancel():
# #     global cancel_process
# #     keyboard.add_hotkey('ctrl+alt+2', lambda: setattr(cancel_process, 'cancel', True))

# # def internet_speed_test():
# #     # Simulated speed test; replace with actual logic if needed
# #     print("Testing internet speed...")
# #     time.sleep(5)  # Simulated time for the test
# #     speed_mbps = 10  # Simulated speed; replace with actual speed
# #     return speed_mbps

# # def schedule_video():
# #     global cancel_process
# #     cancel_process = False

# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Video Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog
# #     Tk().withdraw()  # Hides the root window
# #     video_path = askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])

# #     if not video_path:  # Check if the user cancels the selection
# #         print("No video selected. Exiting.")
# #         return

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Display video file size
# #     video_size = os.path.getsize(video_path) / (1024 * 1024)  # Convert to MB
# #     print(f"\nFile size: {video_size:.2f} MB\n")

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
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

# #     # Step 5: Internet speed test
# #     speed = internet_speed_test()
# #     print(f"Estimated upload speed: {speed} Mbps")

# #     # Step 6: Open WhatsApp Web and start uploading the video
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhatmsg(full_phone_number, '', hour, minute - 3)  # Open WhatsApp Web 3 minutes before
# #     time.sleep(5)  # Give time for WhatsApp to load

# #     # Copy the video file to clipboard
# #     os.system(f'clip < "{video_path}"')

# #     # Step 7: Notify user and countdown
# #     while datetime.datetime.now() < scheduled_time and not cancel_process:
# #         time.sleep(1)  # Sleep for a second to avoid busy waiting

# #         # Check remaining time
# #         remaining_time = scheduled_time - datetime.datetime.now()
# #         if remaining_time.seconds <= 0:
# #             break

# #         # Show a persistent notification
# #         print("\rPress 'Ctrl+Alt+2' to cancel the process.                   ", end="")

# #     if not cancel_process:
# #         print("\nUploading video...")
# #         # Paste and send video
# #         time.sleep(5)  # Wait for the user to see the upload (if necessary)
# #         print("Video uploaded successfully!")

# #     if cancel_process:
# #         print("\nProcess canceled by the user.")
        
# # # Start the cancel check in a separate thread
# # threading.Thread(target=check_cancel, daemon=True).start()

# # # Run the scheduling function
# # schedule_video()
 










# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # import pyperclip  # For clipboard operations
# # import speedtest
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename
# # from threading import Thread
# # import keyboard
# # from tkinter import Button
# # import sys


# # cancel_process = False  # Global variable to handle cancelation

# # # Function to handle process cancelation
# # def cancel():
# #     global cancel_process
# #     cancel_process = True
# #     print("\nProcess Canceled.")
# #     sys.exit()

# # # Function to perform internet speed test and return upload speed
# # def perform_speed_test():
# #     st = speedtest.Speedtest()
# #     print("Starting Internet Speed Test...")
    
# #     # Progress for speed test
# #     print("Testing Download Speed...")
# #     st.download()  # Testing download speed

# #     print("Testing Upload Speed...")
# #     upload_speed = st.upload()  # Testing upload speed in bps

# #     # Convert speed from bits per second to Mbps
# #     upload_speed_mbps = upload_speed / 1_000_000
# #     return upload_speed_mbps

# # # Function to calculate approximate upload time based on file size and upload speed
# # def calculate_upload_time(file_size_mb, upload_speed_mbps):
# #     if upload_speed_mbps == 0:
# #         return float('inf')  # Infinite time if no upload speed

# #     return file_size_mb / upload_speed_mbps  # Time in seconds

# # def schedule_video():
# #     global cancel_process

# #     os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
# #     print("WhatsApp Video Scheduler".center(60, '-'))

# #     # Get user inputs for country code, phone number, and video file
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # File selection using Tkinter
# #     Tk().withdraw()  # Hide the root window
# #     video_path = askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.mkv;*.avi;*.mov")])

# #     if not video_path:
# #         print("No video selected. Exiting.")
# #         return

# #     # Display the file size in yellow
# #     file_size = os.path.getsize(video_path) / (1024 * 1024)  # Size in MB
# #     print(f"\033[93mFile Size: {file_size:.2f} MB\033[0m\n")

# #     # Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Calculate scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     # If scheduled time is in the past, adjust to next day
# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     print(f"Video scheduled for {scheduled_time.strftime('%H:%M:%S')}")

# #     # Perform internet speed test to calculate upload time
# #     upload_speed_mbps = perform_speed_test()
# #     print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")

# #     upload_time_estimate = calculate_upload_time(file_size, upload_speed_mbps)
# #     print(f"Estimated Upload Time: {upload_time_estimate:.2f} seconds")

# #     # Open WhatsApp Web 3 minutes before the scheduled time
# #     time_before_upload = 180  # 3 minutes in seconds
# #     time_to_wait = (scheduled_time - datetime.datetime.now()).total_seconds() - time_before_upload

# #     if time_to_wait > 0:
# #         print(f"Waiting for {int(time_to_wait)} seconds before opening WhatsApp Web.")
# #         time.sleep(time_to_wait)

# #     # Open WhatsApp Web
# #     print("Opening WhatsApp Web...")
# #     os.system("start https://web.whatsapp.com")

# #     # Start uploading the video before the scheduled time
# #     print("Uploading video...")

# #     # Copy the video path to clipboard
# #     pyperclip.copy(video_path)

# #     # Wait until the scheduled time is reached
# #     while datetime.datetime.now() < scheduled_time:
# #         if cancel_process:
# #             return
# #         time.sleep(1)

# #     # Paste and send the video at the scheduled time
# #     pyperclip.paste()
# #     time.sleep(5)  # Give some buffer time
# #     print("Sending the video...")
# #     keyboard.press_and_release('enter')
# #     print("Video sent successfully!")

# # # Start the cancel button thread
# # def run_cancel_button():
# #     root = Tk()
# #     root.geometry("200x100")
# #     root.title("Cancel Process")

# #     button = Button(root, text="Cancel", command=cancel, padx=20, pady=10)
# #     button.pack(pady=20)
# #     root.mainloop()

# # # Create a thread for the cancel button window
# # cancel_thread = Thread(target=run_cancel_button)
# # cancel_thread.daemon = True  # Ensure the thread closes with the main program
# # cancel_thread.start()

# # # Run the video scheduling function
# # schedule_video()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # import pyperclip
# # import keyboard
# # import threading
# # from tkinter import Tk, filedialog, Button
# # import speedtest

# # # To perform an internet speed test
# # def perform_speed_test():
# #     print("Performing internet speed test...")
# #     st = speedtest.Speedtest()
# #     st.get_best_server()
# #     upload_speed = st.upload() / 1_000_000  # Convert to Mbps
# #     print(f"Upload speed: {upload_speed:.2f} Mbps")
# #     return upload_speed

# # # To estimate file upload time based on internet speed
# # def estimate_upload_time(file_size_mb, upload_speed_mbps):
# #     # Upload time in seconds
# #     return file_size_mb / upload_speed_mbps

# # # Dedicated cancel button function
# # cancel_process = False
# # def cancel_upload():
# #     global cancel_process
# #     cancel_process = True
# #     print("\nUpload process canceled by the user.")

# # # Function to handle the video scheduling and sending process
# # def schedule_video():
# #     global cancel_process
# #     cancel_process = False
    
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Video Scheduler".center(60, '-'))

# #     # Step 2: Get user input for country code, phone number, and time
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")
# #     full_phone_number = country_code + phone_number

# #     # Step 3: Ask user to select a video file
# #     Tk().withdraw()  # Hide root window
# #     file_path = filedialog.askopenfilename(
# #         title="Select a Video",
# #         filetypes=[("Video Files", "*.mp4;*.mov;*.avi;*.mkv;*.flv;*.wmv")]
# #     )
# #     if not file_path:
# #         print("No file selected. Exiting.")
# #         return
    
# #     # Show the file size
# #     file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB
# #     print(f"\033[93mVideo file size: {file_size_mb:.2f} MB\033[0m")

# #     # Perform the internet speed test and estimate upload time
# #     upload_speed = perform_speed_test()
# #     estimated_time = estimate_upload_time(file_size_mb, upload_speed)
# #     print(f"Estimated upload time: {estimated_time:.2f} seconds")

# #     # Get the scheduled time
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")
    
# #     # Step 4: Calculate the scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     print(f"Video to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

# #     # Step 5: Start WhatsApp Web and begin the upload process
# #     def start_whatsapp():
# #         if cancel_process:
# #             return
# #         print("\nOpening WhatsApp Web...")
# #         kit.sendwhatmsg(full_phone_number, " ", hour, minute - 3)  # Open WhatsApp 3 minutes earlier
# #         time.sleep(5)  # Wait for WhatsApp to load

# #         # Step 6: Copy the video file to clipboard
# #         pyperclip.copy(file_path)
# #         print("File copied to clipboard.")

# #         # Step 7: Wait until the scheduled time
# #         while datetime.datetime.now() < scheduled_time:
# #             time.sleep(1)
# #             remaining_time = scheduled_time - datetime.datetime.now()
# #             print(f"\rTime remaining: {remaining_time}", end="")

# #         # Paste the file and send it when the time is reached
# #         if not cancel_process:
# #             print("\nSending video...")
# #             keyboard.press_and_release('ctrl+v')
# #             time.sleep(1)
# #             keyboard.press_and_release('enter')  # Hit 'Enter' to send the file
# #             print("Video sent successfully!")

# #     # Launch the WhatsApp process in a new thread
# #     whatsapp_thread = threading.Thread(target=start_whatsapp)
# #     whatsapp_thread.start()

# #     # Step 8: Add a cancel button in the terminal (for user cancellation)
# #     def create_cancel_button():
# #         cancel_btn = Tk()
# #         cancel_btn.geometry("300x100")
# #         cancel_btn.title("Cancel Upload")
# #         button = Button(cancel_btn, text="Cancel Upload", command=cancel_upload, padx=20, pady=10)
# #         button.pack(expand=True)
# #         cancel_btn.mainloop()

# #     # Run the cancel button in a separate thread
# #     cancel_thread = threading.Thread(target=create_cancel_button)
# #     cancel_thread.start()

# # # Run the scheduling function
# # schedule_video()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # import threading
# # import sys
# # from tkinter import Tk, filedialog
# # import pyautogui as pag
# # import subprocess

# # cancel_flag = False  # Global flag to cancel the operation

# # def check_for_cancel():
# #     """
# #     This function checks if the user wants to cancel the operation by pressing 'c' in the terminal.
# #     """
# #     global cancel_flag
# #     while True:
# #         user_input = input("\nPress 'c' to cancel: ")
# #         if user_input.lower() == 'c':
# #             cancel_flag = True
# #             print("\nOperation canceled by user.")
# #             break

# # def schedule_video():
# #     """
# #     Schedule a WhatsApp video to be sent at a specific time with user inputs.
# #     Opens WhatsApp Web instantly after the video is selected, uploads the video,
# #     and sends it at the scheduled time by pressing 'Enter'.
# #     """
# #     global cancel_flag

# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Video Scheduler".center(60, '-'))

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog
# #     root = Tk()
# #     root.withdraw()  # Hides the root window
# #     root.attributes("-topmost", True)  # Ensure file dialog is on top
# #     video_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")], parent=root)

# #     if not video_path:
# #         print("No video selected. Exiting.")
# #         return

# #     # Get file size and display it in yellow
# #     file_size = os.path.getsize(video_path)
# #     print(f"\n\033[93mFile size: {file_size / (1024 * 1024):.2f} MB\033[0m\n")  # Size in MB

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
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

# #     print(f"Video to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

# #     # Step 5: Open WhatsApp Web instantly after video selection
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhatmsg(full_phone_number, "", now.hour, (now.minute + 2) % 60, wait_time=2)  # Open WhatsApp without sending a message
# #     time.sleep(10)  # Wait for WhatsApp Web to load

# #     # Step 6: Automate the file upload by simulating file selection
# #     print("Uploading the video...")
# #     pag.hotkey('ctrl', 'v')  # Assuming the video path is copied to the clipboard
# #     time.sleep(1)  # Wait a moment for the file dialog to appear
# #     pag.press('enter')  # Simulate pressing 'Enter' to upload

# #     # Step 7: Start a separate thread to check for cancellation
# #     cancel_thread = threading.Thread(target=check_for_cancel)
# #     cancel_thread.daemon = True  # Make it a daemon thread so it exits with the main program
# #     cancel_thread.start()

# #     # Step 8: Wait until the scheduled time to send the video
# #     while datetime.datetime.now() < scheduled_time:
# #         if cancel_flag:
# #             return  # If the operation is canceled, exit the function
# #         remaining_time = scheduled_time - datetime.datetime.now()
# #         if remaining_time.seconds % 60 == 0:
# #             print(f"Time remaining: {remaining_time.seconds // 60} minutes")
# #         time.sleep(1)

# #     # Step 9: At the scheduled time, hit 'Enter' to send the video
# #     if not cancel_flag:
# #         print("\nSending the video...")
# #         subprocess.call(['powershell', '-Command', '[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")'])
# #         print("Video sent successfully!")
# #     else:
# #         print("Operation was canceled before sending the video.")

# # # Run the scheduling function
# # schedule_video()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename
# # import pyautogui as pag
# # import subprocess

# # def schedule_video():
# #     """
# #     Schedule a WhatsApp video to be sent at a specific time with user inputs.
# #     Opens WhatsApp Web instantly after the video is selected, uploads the video,
# #     and sends it at the scheduled time by pressing 'Enter'.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Video Scheduler".center(60, '-'))

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog
# #     Tk().withdraw()
# #     video_path = askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])

# #     if not video_path:
# #         print("No video selected. Exiting.")
# #         return

# #     # Get file size and display it in yellow
# #     file_size = os.path.getsize(video_path)
# #     print(f"\n\033[93mFile size: {file_size / (1024 * 1024):.2f} MB\033[0m\n")  # Size in MB

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
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

# #     print(f"Video to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

# #     # Step 5: Open WhatsApp Web instantly after video selection
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhatmsg(full_phone_number, "", now.hour, (now.minute + 2) % 60, wait_time=2)  # Open WhatsApp without sending a message
# #     time.sleep(10)  # Wait for WhatsApp Web to load

# #     # Step 6: Automate the file upload by simulating file selection
# #     print("Uploading the video...")
# #     pag.hotkey('ctrl', 'v')  # Assuming the video path is copied to the clipboard
# #     time.sleep(1)  # Wait a moment for the file dialog to appear
# #     pag.press('enter')  # Simulate pressing 'Enter' to upload

# #     # Step 7: Wait until the scheduled time to send the video
# #     while datetime.datetime.now() < scheduled_time:
# #         remaining_time = scheduled_time - datetime.datetime.now()
# #         if remaining_time.seconds % 60 == 0:
# #             print(f"Time remaining: {remaining_time.seconds // 60} minutes")
# #         time.sleep(1)

# #     # Step 8: At the scheduled time, hit 'Enter' to send the video
# #     print("\nSending the video...")
# #     subprocess.call(['powershell', '-Command', '[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")'])
    
# #     print("Video sent successfully!")

# # # Run the scheduling function
# # schedule_video()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename
# # import subprocess

# # def schedule_video():
# #     """
# #     Schedule a WhatsApp video to be sent at a specific time with user inputs.
# #     Opens WhatsApp Web 3 minutes before the scheduled time and uploads the video.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Video Scheduler".center(60, '-'))

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Step 2.1: Create a Tkinter root window (invisible) and open file dialog
# #     Tk().withdraw()
# #     video_path = askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])

# #     if not video_path:
# #         print("No video selected. Exiting.")
# #         return

# #     # Get file size and display it in yellow
# #     file_size = os.path.getsize(video_path)
# #     print(f"\n\033[93mFile size: {file_size / (1024 * 1024):.2f} MB\033[0m\n")  # Size in MB

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
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

# #     # Open WhatsApp Web 3 minutes before the scheduled time
# #     buffer_time = 3  # 3 minutes
# #     pre_open_time = scheduled_time - datetime.timedelta(minutes=buffer_time)
# #     print(f"Video to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')} (WhatsApp opens at {pre_open_time.strftime('%H:%M')})")

# #     # Step 5: Wait until pre_open_time
# #     while datetime.datetime.now() < pre_open_time:
# #         time.sleep(1)

# #     # Open WhatsApp Web and start the upload
# #     print("\nOpening WhatsApp Web...")
# #     kit.sendwhatmsg(full_phone_number, "", hour, minute, wait_time=buffer_time)  # Open WhatsApp without sending a message
# #     time.sleep(10)  # Wait for WhatsApp Web to load

# #     # Start uploading the video
# #     kit.sendwhats_video(full_phone_number, video_path, wait_time=buffer_time)

# #     # Wait until the scheduled time to send
# #     while datetime.datetime.now() < scheduled_time:
# #         time.sleep(1)

# #     # Hit 'Enter' at the scheduled time to send the video
# #     print("\nSending the video...")
# #     subprocess.call(['powershell', '-Command', '[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")'])

# #     print("Video sent successfully!")

# # # Run the scheduling function
# # schedule_video()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilename
# # import win32clipboard

# # def schedule_video():
# #     """
# #     Schedule a WhatsApp video to be sent at a specific time with user inputs.
# #     Includes file size display and fail-safe features.
# #     """
# #     # Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Video Scheduler".center(60, '-'))  # Title for clarity

# #     # Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")

# #     # Create a Tkinter root window (invisible) and open file dialog
# #     Tk().withdraw()  # Hides the root window
# #     video_path = askopenfilename(title="Select a Video", filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])
    
# #     if not video_path:  # Check if the user cancels the selection
# #         print("No video selected. Exiting.")
# #         return

# #     # Display video file size
# #     file_size = os.path.getsize(video_path) / (1024 * 1024)  # Convert bytes to MB
# #     print(f"\nSelected video size: {file_size:.2f} MB\n")

# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the video (HH:MM in 24-hour format): ")
# #             hour, minute = map(int, time_input.split(':'))

# #             # Validate the time
# #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# #                 break
# #             else:
# #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# #         except ValueError:
# #             print("Invalid format. Please enter the time in HH:MM format.")

# #     # Calculate scheduled time
# #     now = datetime.datetime.now()
# #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# #     # If the scheduled time is in the past, adjust it to the next day
# #     if scheduled_time < now:
# #         scheduled_time += datetime.timedelta(days=1)

# #     # Add a buffer of 3 minutes to ensure WhatsApp Web has enough time to load
# #     wait_time = 3  # wait time in minutes
# #     scheduled_time += datetime.timedelta(minutes=wait_time)

# #     print(f"Video to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M')}")

# #     # Countdown and notification every minute until the scheduled time
# #     while datetime.datetime.now() < scheduled_time:
# #         remaining_time = scheduled_time - datetime.datetime.now()
# #         if remaining_time.seconds % 60 == 0:
# #             minutes_left = remaining_time.seconds // 60
# #             print(f"Time remaining: {minutes_left} minute(s)")
# #         time.sleep(1)  # Just wait until the time arrives

# #     # Open WhatsApp Web and send the video
# #     print("\nOpening WhatsApp Web...")
# #     win32clipboard.OpenClipboard()
# #     win32clipboard.EmptyClipboard()
# #     win32clipboard.SetClipboardText(video_path)
# #     win32clipboard.CloseClipboard()

# #     # Use pywhatkit to send the video
# #     try:
# #         kit.sendwhatmsg(full_phone_number, "Sending video now...", hour, minute)
# #         time.sleep(5)  # Wait for the page to load

# #         # Simulate pressing Enter after 5 seconds to send the video
# #         os.system("echo | set /p dummy= | clip")  # Clear clipboard
# #         kit.send_video(full_phone_number, video_path)
# #         print("Video sent successfully!")
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         print("Attempting to hit 'Enter' as fail-safe.")
# #         os.system("echo | set /p dummy= | clip")  # Clear clipboard
# #         time.sleep(5)  # Wait before pressing Enter

# # # Run the scheduling function
# # schedule_video()
