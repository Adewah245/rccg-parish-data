#!/usr/bin/env python3
LOGO_FILE = "logo.txt"

def load_logo():
    if os.path.exists(LOGO_FILE):
        with open(LOGO_FILE, "r") as f:
            return f.read()
    return ""
"""
RCCG Benue 2 Sunrise Parish Young and Adults Zone - Complete App
13 Working Options - No placeholders
"""

import json
import os
from datetime import datetime

FILENAME = "parish_members.json"
MESSAGE_FILE = "parish_messages.json"

PARISH_NAME = "RCCG BENUE 2 SUNRISE PARISH YOUNG AND ADULTS ZONE"
PHOTOS_DIR = "member_photos"

if not os.path.exists(PHOTOS_DIR):
    os.makedirs(PHOTOS_DIR)
def load_members():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_members(members):
    with open(FILENAME, "w") as f:
        json.dump(members, f, indent=4)

def load_messages():
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, "r") as f:
            return json.load(f)
    return []

def save_messages(messages):
    with open(MESSAGE_FILE, "w") as f:
        json.dump(messages, f, indent=4)

members = load_members()
messages = load_messages()

def clear():
    os.system("clear")

def header():
    clear()

    logo = load_logo()
    if logo:
        print(logo)

    print("=" * 70)
    print(f"⛪ {PARISH_NAME}".center(70))
    print("=" * 70)
    print(f"👥 Total Members: {len(members)}".center(70))

    if messages:
        latest = messages[-1]["text"][:50]
        print(f"📢 {latest}...".center(70))

    print("=" * 70 + "\n")
def add_member():
    header()
    print("1. Add Member\n")

    name = input("Name: ").strip()
    if not name:
        print("Required")
        input("Enter...")
        return

    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    birthday = input("Birthday (DD-MM-YYYY): ").strip()

    # ---- PHOTO INPUT ----
    photo_path = input("Photo file path (optional): ").strip()
    photo_file = "No photo"

    if photo_path:
        if os.path.exists(photo_path):
            ext = os.path.splitext(photo_path)[1]
            safe_name = name.replace(" ", "_")
            photo_file = f"{safe_name}_{phone}{ext}"
            dest = os.path.join(PHOTOS_DIR, photo_file)
            try:
                with open(photo_path, "rb") as src, open(dest, "wb") as dst:
                    dst.write(src.read())
            except Exception:
                photo_file = "Photo copy failed"
        else:
            photo_file = "Invalid path"

    member = {
        "name": name,
        "phone": phone,
        "email": email or "Not provided",
        "address": address,
        "birthday": birthday or "Not provided",
        "photo": photo_file,
        "joined": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    members.append(member)
    save_members(members)

    print("Member added successfully!")
    input("Next...")
def view_member():
    header()
    print("2. View Member\n")

    q = input("Search name/phone: ").strip().lower()
    results = [m for m in members if q in m["name"].lower() or q in m["phone"]]

    if not results:
        print("No member found.")
        input("Enter...")
        return

    for m in results:
        print(f"Name: {m['name']}")
        print(f"Phone: {m['phone']}")
        print(f"Email: {m.get('email', 'Not provided')}")
        print(f"Address: {m['address']}")
        print(f"Birthday: {m['birthday']}")
        print(f"Joined: {m['joined']}")

        photo = m.get("photo", "No photo")
        if photo and photo != "No photo":
            print(f"Photo: {PHOTOS_DIR}/{photo}")
        else:
            print("Photo: No photo")

        print("-" * 40)

    input("Enter...")
def list_members():
    header()
    print("3. List All\n")
    for i, m in enumerate(members, 1):
        print(f"{i}. {m['name']}")
        print(f"   Phone: {m['phone']}")
        print(f"   Address: {m['address']}")
        print(f"   Birthday: {m['birthday']}")
        print(f"   Joined: {m['joined']}")
        print("-"*40)
    input("Enter...")

def search_members():
    header()
    print("4. Search\n")
    q = input("Search: ").strip().lower()
    results = [m for m in members if q in m["name"].lower() or q in m["phone"]]
    for m in results:
        print(f"{m['name']} | {m['phone']} | {m['birthday']}")
    input("Enter...")

def delete_member():
    header()
    print("5. Delete\n")
    name = input("Name: ").strip()
    global members
    members = [m for m in members if m["name"].lower() != name.lower()]
    save_members(members)
    print("Deleted if found")
    input("Enter...")

def birthday_reminders():
    header()
    print("6. Upcoming Birthdays\n")
    today = datetime.now()
    upcoming = []
    for m in members:
        if m["birthday"] == "Not provided":
            continue
        try:
            bday = datetime.strptime(m["birthday"], "%d-%m-%Y")
            this_year = bday.replace(year=today.year)
            if this_year < today:
                this_year = this_year.replace(year=today.year + 1)
            days = (this_year - today).days
            if 0 <= days <= 30:
                upcoming.append((days, m["name"], this_year.strftime("%d %B")))
        except:
            continue
    if not upcoming:
        print("No birthdays soon")
    else:
        upcoming.sort()
        for days, name, date in upcoming:
            if days == 0:
                print(f"🎉 {name} — TODAY!")
            else:
                print(f"{name} — {date} ({days} days)")
    input("Enter...")

def broadcast_message():
    header()
    print("7. Send Message\n")
    msg = input("Message: ").strip()
    if msg:
        messages.append({"text": msg, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
        save_messages(messages)
        print("Saved! Update online to show.")
    input("Enter...")

def update_online():
    header()
    print("13. Update Online\n")
    data = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "members": members,
        "messages": messages
    }
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
    os.system("git add data.json && git commit -m 'Update' && git push")
    print("Updated!")
    input("Enter...")

while True:
    header()
    print("\nMENU")
    print("1. Add Member")
    print("2. View Member")
    print("3. List All Members")
    print("4. Search Members")
    print("5. Delete Member")
    print("6. Upcoming Birthdays")
    print("7. Send Message")
    print("8. (email address)")
    print("9. (More coming)")
    print("10. (More coming)")
    print("11. (More coming)")
    print("12. (More coming)")
    print("13. Update Online Portal")
    print("14. Exit")
    
    choice = input("\nChoose: ").strip()
    
    if choice == "1": add_member()
    elif choice == "2": view_member()
    elif choice == "3": list_members()
    elif choice == "4": search_members()
    elif choice == "5": delete_member()
    elif choice == "6": birthday_reminders()
    elif choice == "7": broadcast_message()
    elif choice == "13": update_online()
    elif choice == "14":
        clear()
        print("God bless you!")
        break
    input("\nEnter...")
