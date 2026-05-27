# 🍕 Ultimate Creative Restaurant Chatbot 🍕

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyttsx3
import datetime
import random

# ---------------- VOICE ENGINE ---------------- #

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------------- MENU ---------------- #

menu = {
    "pizza": 200,
    "burger": 120,
    "pasta": 180,
    "sandwich": 100
}

# ---------------- VARIABLES ---------------- #

total = 0
order_history = []

# ---------------- CUSTOMER NAME ---------------- #

customer_name = input("Enter Your Name: ")

# ---------------- MAIN WINDOW ---------------- #

root = tk.Tk()
root.title("🍕 Foodie Restaurant Chatbot")
root.geometry("600x750")
root.configure(bg="#fff8dc")

# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="🍕 FOODIE RESTAURANT CHATBOT 🍔",
    font=("Arial", 20, "bold"),
    bg="#fff8dc",
    fg="darkred"
)

title.pack(pady=10)

# ---------------- CHAT AREA ---------------- #

chat_area = tk.Text(
    root,
    height=20,
    width=60,
    font=("Arial", 12),
    bg="white"
)

chat_area.pack(pady=10)

# ---------------- INPUT BOX ---------------- #

user_input = tk.Entry(
    root,
    width=35,
    font=("Arial", 14)
)

user_input.pack(pady=10)

# ---------------- IMAGE LABEL ---------------- #

image_label = tk.Label(root, bg="#fff8dc")
image_label.pack()

# ---------------- SHOW FOOD IMAGE ---------------- #

def show_image(food):

    try:

        if food == "pizza":
            img = Image.open("pizza.png")

        elif food == "burger":
            img = Image.open("burger.png")

        else:
            return

        img = img.resize((200, 200))

        photo = ImageTk.PhotoImage(img)

        image_label.config(image=photo)
        image_label.image = photo

    except:
        pass

# ---------------- RECEIPT ---------------- #

def generate_receipt():

    receipt = "\n======= RECEIPT =======\n"

    if len(order_history) == 0:
        receipt += "No items ordered.\n"

    else:

        for order in order_history:
            receipt += order + "\n"

    receipt += f"\nTotal Bill = ₹{total}"
    receipt += "\n======================="

    return receipt

# ---------------- MAIN CHATBOT FUNCTION ---------------- #

def send_message():

    global total

    user = user_input.get().lower()

    chat_area.insert(tk.END, f"\nYou: {user}\n")

    # ---------------- GREETING ---------------- #

    if "hi" in user or "hello" in user:

        bot_reply = f"Hello {customer_name}! Welcome to Foodie Restaurant 😄"

    # ---------------- MENU ---------------- #

    elif "menu" in user:

        bot_reply = "🍔 MENU 🍔\n\n"

        for item, price in menu.items():
            bot_reply += f"{item.capitalize()} - ₹{price}\n"

    # ---------------- PIZZA ---------------- #

    elif "pizza" in user:

        quantity = 1

        for word in user.split():

            if word.isdigit():
                quantity = int(word)

        cost = menu["pizza"] * quantity

        total += cost

        order_history.append(f"{quantity} x Pizza = ₹{cost}")

        bot_reply = f"🍕 {quantity} Pizza added successfully!\n"
        bot_reply += f"Cost = ₹{cost}\n"
        bot_reply += f"Current Total = ₹{total}"

        show_image("pizza")

    # ---------------- BURGER ---------------- #

    elif "burger" in user:

        quantity = 1

        for word in user.split():

            if word.isdigit():
                quantity = int(word)

        cost = menu["burger"] * quantity

        total += cost

        order_history.append(f"{quantity} x Burger = ₹{cost}")

        bot_reply = f"🍔 {quantity} Burger added successfully!\n"
        bot_reply += f"Cost = ₹{cost}\n"
        bot_reply += f"Current Total = ₹{total}"

        show_image("burger")

    # ---------------- PASTA ---------------- #

    elif "pasta" in user:

        quantity = 1

        for word in user.split():

            if word.isdigit():
                quantity = int(word)

        cost = menu["pasta"] * quantity

        total += cost

        order_history.append(f"{quantity} x Pasta = ₹{cost}")

        bot_reply = f"🍝 {quantity} Pasta added successfully!\n"
        bot_reply += f"Cost = ₹{cost}\n"
        bot_reply += f"Current Total = ₹{total}"

    # ---------------- SANDWICH ---------------- #

    elif "sandwich" in user:

        quantity = 1

        for word in user.split():

            if word.isdigit():
                quantity = int(word)

        cost = menu["sandwich"] * quantity

        total += cost

        order_history.append(f"{quantity} x Sandwich = ₹{cost}")

        bot_reply = f"🥪 {quantity} Sandwich added successfully!\n"
        bot_reply += f"Cost = ₹{cost}\n"
        bot_reply += f"Current Total = ₹{total}"

    # ---------------- BILL ---------------- #

    elif "bill" in user or "total" in user:

        bot_reply = generate_receipt()

    # ---------------- ORDER HISTORY ---------------- #

    elif "history" in user:

        if len(order_history) == 0:

            bot_reply = "🛒 No orders yet."

        else:

            bot_reply = "🛒 ORDER HISTORY\n\n"

            for order in order_history:
                bot_reply += order + "\n"

    # ---------------- OFFERS ---------------- #

    elif "offer" in user or "discount" in user:

        offers = [
            "🎉 You won 10% Discount!",
            "🍕 Buy 1 Get 1 Free!",
            "🥤 Free Cold Drink!",
            "🍔 Free Burger Coupon!"
        ]

        bot_reply = random.choice(offers)

    # ---------------- DELIVERY ---------------- #

    elif "delivery" in user:

        bot_reply = "🚚 Your order will arrive in 20 minutes."

    # ---------------- TIME ---------------- #

    elif "time" in user:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        bot_reply = f"⏰ Current Time: {current_time}"

    # ---------------- THANK YOU ---------------- #

    elif "thank" in user:

        bot_reply = "😊 You're Welcome!"

    # ---------------- ABOUT CHATBOT ---------------- #

    elif "who are you" in user:

        bot_reply = "🤖 I am Foodie Restaurant Chatbot."

    # ---------------- HELP ---------------- #

    elif "help" in user:

        bot_reply = """
🤖 Try These Commands:

• hi
• menu
• pizza
• burger
• pasta
• sandwich
• bill
• history
• offer
• delivery
• time
• exit
"""

    # ---------------- EXIT ---------------- #

    elif "exit" in user:

        bot_reply = "🍕 Thank You! Visit Again."

        speak(bot_reply)

        messagebox.showinfo("Exit", bot_reply)

        root.destroy()

        return

    # ---------------- UNKNOWN QUESTION ---------------- #

    else:

        bot_reply = """
❌ Sorry, I didn't understand.

Try:
• menu
• pizza
• burger
• pasta
• sandwich
• bill
• history
• offer
• help
"""

    # ---------------- DISPLAY ---------------- #

    chat_area.insert(tk.END, f"Bot: {bot_reply}\n")

    # ---------------- VOICE ---------------- #

    speak(bot_reply)

    # ---------------- CLEAR INPUT ---------------- #

    user_input.delete(0, tk.END)

# ---------------- SEND BUTTON ---------------- #

send_button = tk.Button(
    root,
    text="SEND",
    command=send_message,
    bg="orange",
    fg="white",
    font=("Arial", 14, "bold"),
    width=15
)

send_button.pack(pady=15)

# ---------------- START PROGRAM ---------------- #

root.mainloop()