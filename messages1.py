import pywhatkit as kit
import datetime
import time

def schedule_message():
    # Step 1: Get user input for country code, phone number, and message
    country_code = input("Enter country code (e.g., +1 for USA, +91 for India): ")
    phone_number = input("Enter mobile number: ")
    message = input("Enter the message to be sent: ")

    # Combine country code and phone number
    full_phone_number = country_code + phone_number

    # Step 2: Get and validate the time input (24-hour format)
    while True:
        try:
            time_input = input("Enter the time to send the message (HH:MM in 24-hour format): ")
            hour, minute = map(int, time_input.split(':'))

            # Validate the time
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                break
            else:
                print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
        except ValueError:
            print("Invalid format. Please enter the time in HH:MM format.")
    
    # Step 3: Open WhatsApp Web and schedule the message
    try:
        print(f"Scheduling message to {full_phone_number} at {hour}:{minute}.")
        kit.sendwhatmsg(full_phone_number, message, hour, minute)
    except Exception as e:
        print(f"An error occurred: {e}")




# Run the scheduling function
schedule_message()
# import pywhatkit as kit
# import datetime
# import time
# import os

# def schedule_message():
#     # Step 1: Get user input for country code, phone number, and message
#     country_code = input("Enter country code (e.g., +1 for USA, +91 for India): ")
#     phone_number = input("Enter mobile number: ")
#     message = input("Enter the message to be sent: ")

#     # Combine country code and phone number
#     full_phone_number = country_code + phone_number

#     # Step 2: Get and validate the time input (24-hour format)
#     while True:
#         try:
#             time_input = input("Enter the time to send the message (HH:MM in 24-hour format): ")
#             hour, minute = map(int, time_input.split(':'))

#             # Validate the time
#             if 0 <= hour <= 23 and 0 <= minute <= 59:
#                 break
#             else:
#                 print("Invalid time. Please enter a valid time between 00:00 and 23:59.")
#         except ValueError:
#             print("Invalid format. Please enter the time in HH:MM format.")
    
#     # Step 3: Calculate the scheduled time
#     now = datetime.datetime.now()
#     scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    
#     # If the scheduled time is in the past, adjust it to the next day
#     if scheduled_time < now:
#         scheduled_time += datetime.timedelta(days=1)

#     print(f"Message to {full_phone_number} is scheduled for {scheduled_time.strftime('%H:%M:%S')}")

#     # Step 4: Active countdown until the scheduled time
#     while datetime.datetime.now() < scheduled_time:
#         remaining_time = scheduled_time - datetime.datetime.now()
#         hours, remainder = divmod(remaining_time.seconds, 3600)
#         minutes, seconds = divmod(remainder, 60)
        
#         # Change color based on remaining time
#         if remaining_time.seconds <= 25:
#             color_code = "\033[91m"  # Red for 25 seconds and below
#         elif remaining_time.seconds <= 30:
#             color_code = "\033[93m"  # Yellow for 30-26 seconds
#         else:
#             color_code = "\033[0m"   # Default color

#         # Clear the line and print countdown
#         print(f"{color_code}\rTime remaining: {hours:02}:{minutes:02}:{seconds:02}\033[0m", end="")
        
#         time.sleep(1)  # Sleep for 1 second and update countdown

#     # Step 5: Open WhatsApp Web and send the message
#     print("\nOpening WhatsApp Web...")
#     kit.sendwhatmsg(full_phone_number, message, hour, minute)

# # Run the scheduling function
# schedule_message()


