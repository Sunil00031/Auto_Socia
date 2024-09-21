# 
import schedule
import time
import pywhatkit
import datetime
import os
import random

def send_message(contact, message, scheduled_time):
    """
    Sends a message to a specific contact at the scheduled time.
    """
    try:
        schedule_time = datetime.datetime.strptime(scheduled_time, '%H:%M')
        current_time = datetime.datetime.now()
        delay = (schedule_time - current_time).seconds

        def scheduled_send():
            pywhatkit.sendwhats_message(contact, message, wait_time=10)
            print(f"Message sent to {contact} at {datetime.datetime.now().strftime('%H:%M')}")

        schedule.every(delay).seconds.do(scheduled_send)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"Error sending message: {e}")

def send_image(contact, image_path, scheduled_time):
    """
    Sends an image to a specific contact at the scheduled time.
    """
    try:
        schedule_time = datetime.datetime.strptime(scheduled_time, '%H:%M')
        current_time = datetime.datetime.now()
        delay = (schedule_time - current_time).seconds

        def scheduled_send():
            pywhatkit.sendwhats_image(contact, image_path, wait_time=10)
            print(f"Image sent to {contact} at {datetime.datetime.now().strftime('%H:%M')}")

        schedule.every(delay).seconds.do(scheduled_send)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"Error sending image: {e}")

def send_document(contact, document_path, scheduled_time):
    """
    Sends a document to a specific contact at the scheduled time.
    """
    try:
        schedule_time = datetime.datetime.strptime(scheduled_time, '%H:%M')
        current_time = datetime.datetime.now()
        delay = (schedule_time - current_time).seconds

        def scheduled_send():
            pywhatkit.sendwhats_document(contact, document_path, wait_time=10)
            print(f"Document sent to {contact} at {datetime.datetime.now().strftime('%H:%M')}")

        schedule.every(delay).seconds.do(scheduled_send)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"Error sending document: {e}")

def chatbot_response(message):
    """
    Simulates a chatbot response based on the input message.
    """
    # Replace this with your own chatbot logic
    responses = [
        "Hello there!",
        "How can I help you today?",
        "I'm still under development, but I'm learning new things every day.",
    ]
    return random.choice(responses)

def main():
    while True:
        choice = input("Choose an action:\n1. Send message\n2. Send image\n3. Send document\n4. Chat with chatbot\n5. Exit\n")

        if choice == '1':
            contact = input("Enter the contact number with country code (e.g., +1234567890): ")
            message = input("Enter the message: ")
            scheduled_time = input("Enter the time to schedule the message in HH:MM format (24-hour clock): ")
            send_message(contact, message, scheduled_time)
        elif choice == '2':
            contact = input("Enter the contact number with country code (e.g., +1234567890): ")
            image_path = input("Enter the path to the image file: ")
            scheduled_time = input("Enter the time to schedule the image in HH:MM format (24-hour clock): ")
            send_image(contact, image_path, scheduled_time)
        elif choice == '3':
            contact = input("Enter the contact number with country code (e.g., +1234567890): ")
            document_path = input("Enter the path to the document file: ")
            scheduled_time = input("Enter the time to schedule the document in HH:MM format (24-hour clock): ")
            send_document(contact, document_path, scheduled_time)
        elif choice == '4':
            while True:
                user_message = input("You: ")
                chatbot_response = chatbot_response(user_message)
                print("Chatbot:", chatbot_response)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()