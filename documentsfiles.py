# import pywhatkit
# import schedule
# import time
# import os
# import shutil
# import datetime

# def send_document(contact, document_path, scheduled_time):
#     """
#     This function sends a document to a specific contact at the scheduled time.
#     """
#     # Extract file extension to ensure it's not an image, video, or audio
#     file_extension = os.path.splitext(document_path)[1].lower()

#     # List of unsupported file types (images, videos, audio files)
#     unsupported_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.mp4', '.avi', '.mp3', '.wav']

#     # Check if the file type is supported
#     if file_extension in unsupported_extensions:
#         print("Unsupported file type. Please choose a document.")
#         return

#     # WhatsApp Web must be logged in before using this function
#     print(f"Scheduling document {document_path} to be sent to {contact} at {scheduled_time}")

#     # Schedule the task
#     schedule_time = datetime.datetime.strptime(scheduled_time, '%H:%M')
#     current_time = datetime.datetime.now()

#     delay = (schedule_time - current_time).seconds

#     def scheduled_send():
#         # Open WhatsApp Web
#         pywhatkit.sendwhats_document(contact, document_path)
#         print(f"Document {document_path} sent to {contact} at {datetime.datetime.now().strftime('%H:%M')}")

#     # Schedule the send at the exact time
#     schedule.every(delay).seconds.do(scheduled_send)

#     while True:
#         # Execute scheduled tasks
#         schedule.run_pending()
#         time.sleep(1)


# def main():
#     # Take inputs
#     contact = input("Enter the contact number with country code (e.g., +1234567890): ")
#     document_path = input("Enter the full path of the document you want to send: ")
#     scheduled_time = input("Enter the time to schedule the document in HH:MM format (24-hour clock): ")

#     # Check if the file exists
#     if not os.path.exists(document_path):
#         print("File not found. Please enter a valid file path.")
#         return

#     # Send the document at the scheduled time
#     send_document(contact, document_path, scheduled_time)


# if __name__ == "__main__":
#     main()




# # import datetime
# # import time
# # import os
# # import pyautogui
# # import webbrowser as web
# # from tkinter import Tk, filedialog

# # def schedule_image():
# #     """
# #     Schedule a WhatsApp image to be sent at a specific time using pyautogui to automate the upload process.
# #     This version removes the caption feature and uses pyautogui to handle the file dialog.
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

# #     # Step 6: Open WhatsApp Web
# #     print("\nOpening WhatsApp Web...")
# #     web.open(f"https://web.whatsapp.com/send?phone={full_phone_number}")
# #     time.sleep(15)  # Wait for WhatsApp Web to load

# #     # Step 7: Automate the file upload
# #     print("Uploading the image...")

# #     # Step 7.1: Click on the attachment icon (paperclip)
# #     pyautogui.click(x=1300, y=950)  # Adjust x, y coordinates based on your screen resolution
# #     time.sleep(2)  # Wait for the file upload window to appear

# #     # Step 7.2: Simulate pressing 'ctrl+v' to paste the file path in the dialog
# #     pyautogui.write(image_path)  # Type the image path
# #     time.sleep(1)  # Small delay before pressing 'Enter'
# #     pyautogui.press('enter')  # Press 'Enter' to select the file

# #     time.sleep(3)  # Wait for file to load into WhatsApp

# #     # Step 7.3: Press 'Enter' to send the message
# #     pyautogui.press('enter')

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
# #     caption = input("Enter a caption for the image (optional, press Enter to skip): ")

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
# #     if caption:
# #         pyautogui.write(caption)  # Write the caption
# #     pyautogui.press('enter')  # Send the message

# #     print("Image sent successfully!")

# # # Run the scheduling function
# # schedule_image()



# # import pywhatkit as kit
# # import datetime
# # import time
# # import os
# # import shutil
# # from tkinter import Tk
# # from tkinter.filedialog import askopenfilenames
# # import tempfile

# # def schedule_documents():
# #     """
# #     Schedule WhatsApp document uploads to multiple recipients with user inputs.
# #     This version uses temporary storage for file handling and avoids clipboard issues.
# #     """
# #     # Step 1: Clear the terminal screen
# #     os.system('cls' if os.name == 'nt' else 'clear')

# #     print("WhatsApp Document Scheduler".center(60, '-'))  # Title for clarity

# #     # Step 2: Get user input for country code and phone number
# #     country_code = input("Enter country code (e.g., +91 for India): ")
# #     phone_number = input("Enter mobile number: ")
    
# #     # Combine country code and phone number
# #     full_phone_number = country_code + phone_number

# #     # Step 2.1: Select multiple files
# #     Tk().withdraw()  # Hides the root window
# #     file_paths = askopenfilenames(title="Select Documents", filetypes=[("All Files", "*.*")])

# #     if not file_paths:  # Check if the user cancels the selection
# #         print("No files selected. Exiting.")
# #         return

# #     # Step 2.2: Create temporary directory for storing selected files
# #     temp_dir = tempfile.mkdtemp()
# #     total_size = 0  # Track total size of selected files

# #     print("\nCopying selected files to temporary storage...\n")
    
# #     for file_path in file_paths:
# #         # Copy the files to the temporary directory
# #         shutil.copy(file_path, temp_dir)
        
# #         # Calculate total size
# #         total_size += os.path.getsize(file_path)
# #         print(f"Copied: {os.path.basename(file_path)} | Size: {os.path.getsize(file_path) / (1024 * 1024):.2f} MB")

# #     print(f"\nTotal size of selected files: {total_size / (1024 * 1024):.2f} MB")

# #     # Check if the total size exceeds WhatsApp's limit (~100 MB per file)
# #     if any(os.path.getsize(file) > 100 * 1024 * 1024 for file in file_paths):
# #         print("Error: One or more files exceed WhatsApp's 100 MB file limit.")
# #         return

# #     # Step 3: Get and validate the time input (24-hour format)
# #     while True:
# #         try:
# #             time_input = input("Enter the time to send the documents (HH:MM in 24-hour format): ")
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
# #     buffer_time = 3  # Buffer time in minutes
# #     scheduled_time -= datetime.timedelta(minutes=buffer_time)

# #     print(f"\nDocuments to {full_phone_number} are scheduled for {scheduled_time.strftime('%H:%M')}\n")

# #     # Step 6: Open WhatsApp Web 3 minutes before scheduled time
# #     while datetime.datetime.now() < scheduled_time:
# #         remaining_time = (scheduled_time - datetime.datetime.now()).total_seconds()
# #         time.sleep(remaining_time)  # Wait until the scheduled time

# #     print("Opening WhatsApp Web...")
# #     kit.sendwhatmsg(full_phone_number, '', hour, minute + buffer_time, 20, True)  # Open WhatsApp Web
    
# #     # Step 7: Send the documents one by one after WhatsApp Web opens
# #     for file_name in os.listdir(temp_dir):
# #         file_path = os.path.join(temp_dir, file_name)
# #         print(f"Sending {file_name}...")
# #         kit.sendwhats_image(full_phone_number, file_path, caption="", wait_time=20)
# #         time.sleep(5)  # Add delay between sending files

# #     print("Documents sent successfully!")

# #     # Clean up temporary files after sending
# #     shutil.rmtree(temp_dir)
# #     print("Temporary files cleaned up.")

# # # Run the scheduling function
# # schedule_documents()


# # # import pywhatkit as kit
# # # import datetime
# # # import time
# # # import os
# # # from tkinter import Tk
# # # from tkinter.filedialog import askopenfilenames

# # # def schedule_documents():
# # #     """
# # #     Schedule WhatsApp document uploads to multiple recipients with user inputs.
# # #     """
# # #     # Step 1: Clear the terminal screen
# # #     os.system('cls' if os.name == 'nt' else 'clear')

# # #     print("WhatsApp Document Scheduler".center(60, '-'))  # Title for clarity

# # #     # Step 2: Get user input for country code and phone number
# # #     country_code = input("Enter country code (e.g., +91 for India): ")
# # #     phone_number = input("Enter mobile number: ")
    
# # #     # Combine country code and phone number
# # #     full_phone_number = country_code + phone_number

# # #     # Step 2.1: Select multiple files
# # #     Tk().withdraw()  # Hides the root window
# # #     file_paths = askopenfilenames(title="Select Documents", filetypes=[("All Files", "*.*")])

# # #     if not file_paths:  # Check if the user cancels the selection
# # #         print("No files selected. Exiting.")
# # #         return

# # #     # Step 3: Get and validate the time input (24-hour format)
# # #     while True:
# # #         try:
# # #             time_input = input("Enter the time to send the documents (HH:MM in 24-hour format): ")
# # #             hour, minute = map(int, time_input.split(':'))

# # #             # Validate the time
# # #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# # #                 break
# # #             else:
# # #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# # #         except ValueError:
# # #             print("Invalid format. Please enter the time in HH:MM format.")

# # #     # Step 4: Calculate scheduled time
# # #     now = datetime.datetime.now()
# # #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# # #     # If the scheduled time is in the past, adjust it to the next day
# # #     if scheduled_time < now:
# # #         scheduled_time += datetime.timedelta(days=1)

# # #     # Step 5: Add a buffer of 3 minutes to ensure WhatsApp Web has enough time to load
# # #     buffer_time = 3  # Buffer time in minutes
# # #     scheduled_time -= datetime.timedelta(minutes=buffer_time)

# # #     print(f"Documents to {full_phone_number} are scheduled for {scheduled_time.strftime('%H:%M')}")

# # #     # Step 6: Open WhatsApp Web 3 minutes before scheduled time
# # #     while datetime.datetime.now() < scheduled_time:
# # #         remaining_time = (scheduled_time - datetime.datetime.now()).total_seconds()
# # #         time.sleep(remaining_time)  # Wait until the scheduled time

# # #     print("Opening WhatsApp Web...")
# # #     kit.sendwhatmsg(full_phone_number, '', hour, minute + buffer_time, 20, True)  # Open WhatsApp Web
    
# # #     # Step 7: Send the documents one by one after WhatsApp Web opens
# # #     for file_path in file_paths:
# # #         kit.sendwhats_image(full_phone_number, file_path, caption="", wait_time=20)
# # #         time.sleep(5)  # Add delay between sending files

# # #     print("Documents sent successfully!")

# # # # Run the scheduling function
# # # schedule_documents()



# # # import pywhatkit as kit
# # # import time
# # # import datetime
# # # import os
# # # from tkinter import Tk
# # # from tkinter.filedialog import askopenfilenames
# # # import keyboard  # For the cancel button shortcut
# # # import pyautogui  # For file uploading via WhatsApp Web

# # # def schedule_documents():
# # #     """
# # #     Schedules sending multiple documents via WhatsApp at a specific time, 
# # #     with user inputs for phone number, document selection, and scheduling time.
# # #     """
# # #     # Step 1: Clear the terminal screen
# # #     os.system('cls' if os.name == 'nt' else 'clear')

# # #     print("WhatsApp Document Scheduler".center(60, '-'))

# # #     # Step 2: Get user input for country code and phone number
# # #     country_code = input("Enter country code (e.g., +91 for India): ")
# # #     phone_number = input("Enter mobile number: ")
# # #     full_phone_number = country_code + phone_number

# # #     # Step 3: File selection (allow multiple files)
# # #     Tk().withdraw()  # Hide Tkinter root window
# # #     file_paths = askopenfilenames(title="Select Documents", 
# # #                                   filetypes=[("All Files", "*.*"), 
# # #                                              ("PDF Files", "*.pdf"), 
# # #                                              ("Word Files", "*.doc;*.docx"),
# # #                                              ("Text Files", "*.txt")])

# # #     if not file_paths:  # If no files selected
# # #         print("No document selected. Exiting.")
# # #         return

# # #     # Step 4: Display file details
# # #     print("\nSelected documents:")
# # #     for file_path in file_paths:
# # #         file_size = os.path.getsize(file_path) / (1024 * 1024)  # Get file size in MB
# # #         print(f"{os.path.basename(file_path)} - Size: \033[93m{file_size:.2f} MB\033[0m")  # Yellow color for size

# # #     # Step 5: Get and validate the time input (24-hour format)
# # #     while True:
# # #         try:
# # #             time_input = input("Enter the time to send the documents (HH:MM in 24-hour format): ")
# # #             hour, minute = map(int, time_input.split(':'))

# # #             # Validate the time
# # #             if 0 <= hour <= 23 and 0 <= minute <= 59:
# # #                 break
# # #             else:
# # #                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
# # #         except ValueError:
# # #             print("Invalid format. Please enter the time in HH:MM format.")

# # #     # Step 6: Calculate scheduled time
# # #     now = datetime.datetime.now()
# # #     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

# # #     # If the scheduled time is in the past, adjust it to the next day
# # #     if scheduled_time < now:
# # #         scheduled_time += datetime.timedelta(days=1)

# # #     print(f"Documents scheduled to {full_phone_number} at {scheduled_time.strftime('%H:%M')}")

# # #     # Step 7: Countdown and open WhatsApp Web
# # #     while datetime.datetime.now() < scheduled_time:
# # #         remaining_time = scheduled_time - datetime.datetime.now()
# # #         print(f"\rTime remaining: {remaining_time}", end="")
# # #         time.sleep(1)

# # #     print("\nOpening WhatsApp Web...")
# # #     kit.sendwhatmsg(full_phone_number, '', hour, minute, 15, True)  # Open WhatsApp Web

# # #     # Step 8: Wait for WhatsApp Web to open
# # #     time.sleep(15)  # Time buffer for WhatsApp Web to open

# # #     # Step 9: Upload documents
# # #     for file_path in file_paths:
# # #         pyautogui.hotkey('ctrl', 'v')  # Paste the file path into WhatsApp
# # #         pyautogui.press('enter')  # Hit Enter to send the document
# # #         time.sleep(2)  # Wait for the file to be uploaded and sent

# # #     # Fail-safe: Hit Enter if the document wasn't sent
# # #     print("All documents sent successfully!")

# # # # Run the document scheduling function
# # # schedule_documents()



# # # import schedule
# # # import time
# # # import pyautogui
# # # import tkinter as tk
# # # from tkinter import filedialog
# # # from datetime import datetime

# # # def select_files():
# # #     root = tk.Tk()
# # #     root.withdraw()  # Hide the root window
# # #     file_paths = filedialog.askopenfilenames(
# # #         title="Select files",
# # #         filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
# # #     )
# # #     return file_paths

# # # def upload_files(file_paths):
# # #     for file_path in file_paths:
# # #         # This is where you would implement your upload logic
# # #         print(f"Uploading: {file_path}")
# # #         # Simulate a file upload (replace with your actual upload code)
# # #         time.sleep(1)  # Simulating time taken to upload

# # # def schedule_upload(upload_time):
# # #     file_paths = select_files()
# # #     if file_paths:
# # #         schedule.every().day.at(upload_time).do(upload_files, file_paths)

# # # def run_schedule():
# # #     while True:
# # #         schedule.run_pending()
# # #         time.sleep(1)

# # # if __name__ == "__main__":
# # #     upload_time = input("Enter the time to upload files (HH:MM in 24-hour format): ")
# # #     schedule_upload(upload_time)
# # #     print(f"Files scheduled to upload at {upload_time}.")
# # #     run_schedule()
