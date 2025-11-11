import requests
import tkinter as tk
from tkinter import messagebox

URL = "https://shahad.top/spoofer.php"

headers = {
    'authority': 'shahad.top',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://shahad.top',
    'referer': 'https://shahad.top/spoofer.php',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

# Function to send email
def send_email():
    data = {
        'license': 'atelegramuser',
        'sender_name': sender_name_entry.get(),
        'from_email': from_email_entry.get(),
        'to_email': to_email_entry.get(),
        'subject': subject_entry.get(),
        'message': message_text.get("1.0", tk.END),
        'submit': '1',
    }

    try:
        response = requests.post(URL, headers=headers, data=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Email sent successfully!")
        else:
            messagebox.showerror("Error", f"Failed with status code {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.title("Email Spoofer Tool")
root.geometry("400x500")

title_label = tk.Label(root, text="Made by @NGYT777GG", font=("Arial", 14, "bold"), fg="blue")
title_label.pack(pady=10)
sender_name_label = tk.Label(root, text="Sender Name:")
sender_name_label.pack()
sender_name_entry = tk.Entry(root, width=40)
sender_name_entry.pack()

from_email_label = tk.Label(root, text="From Email:")
from_email_label.pack()
from_email_entry = tk.Entry(root, width=40)
from_email_entry.pack()

to_email_label = tk.Label(root, text="To Email:")
to_email_label.pack()
to_email_entry = tk.Entry(root, width=40)
to_email_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(root, width=40)
subject_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()
message_text = tk.Text(root, width=40, height=10)
message_text.pack()

send_button = tk.Button(root, text="Send Email", command=send_email, bg="green", fg="white", font=("Arial", 12, "bold"))
send_button.pack(pady=20)

root.mainloop()