#!/usr/bin/env python3
"""
RCCG Sunrise Parish Management System - Full Version with 12 Options
Clean & Beautiful Console Display (Termux Safe)
"""

import json
import os
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


class ParishApp:
    def __init__(self):
        self.data_file = "parish_data.json"
        self.images_dir = "parish_images"
        self.members = []
        self.parish_info = {
            "name": "RCCG BENUE 2 SUNRISE PARISH YOUNG AND ADULTS ZONE"
        }
        self.load_data()
        self.setup_images_directory()

    # ---------------- SETUP ----------------
    def setup_images_directory(self):
        Path(self.images_dir).mkdir(exist_ok=True)

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.members = data.get("members", [])
            except Exception:
                self.members = []

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump({"members": self.members}, f, indent=4)

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_header(self, title, color=Fore.CYAN):
        print(color + Style.BRIGHT + "=" * 60)
        print(title.center(60))
        print("=" * 60 + Style.RESET_ALL)

    # ---------------- MEMBERS ----------------
    def add_member(self):
        self.print_header("ADD NEW MEMBER", Fore.YELLOW)

        name = input("Full Name: ").strip()
        if not name:
            print(Fore.RED + "Name is required!")
            return

        phone = input("Phone: ").strip()
        birthday = input("Birthday (DD-MM-YYYY): ").strip()

        member = {
            "id": len(self.members) + 1,
            "name": name,
            "phone": phone,
            "birthday": birthday
        }

        self.members.append(member)
        self.save_data()
        print(Fore.GREEN + f"\nMember added! ID: {member['id']}")

    def view_member(self):
        self.print_header("VIEW MEMBER", Fore.MAGENTA)

        try:
            mid = int(input("Enter Member ID: "))
        except ValueError:
            print(Fore.RED + "Invalid ID!")
            return

        member = next((m for m in self.members if m["id"] == mid), None)
        if not member:
            print(Fore.RED + "Member not found!")
            return

        print("\n" + "-" * 60)
        print("Name      :", member["name"])
        print("Phone     :", member["phone"])
        print("Birthday  :", member["birthday"])
        print("-" * 60)

    def list_all_members(self):
        if not self.members:
            print(Fore.RED + "No members found!")
            return

        self.print_header(f"ALL MEMBERS ({len(self.members)})", Fore.BLUE)

        for m in self.members:
            print(Fore.CYAN + Style.BRIGHT + f"MEMBER ID : {m['id']}")
            print("-" * 60)
            print("Name      :", m["name"])
            print("Phone     :", m["phone"])
            print("Birthday  :", m["birthday"])
            print("-" * 60 + "\n")

    # ---------------- PLACEHOLDERS ----------------
    def coming_soon(self, title):
        self.print_header(title, Fore.RED)
        print("This feature is coming soon 🚧")
    def update_online(self):
        self.print_header("UPDATE ONLINE PORTAL", Fore.GREEN)
        
        # Prepare data for online
        data = {
            "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "members": self.members,
            "messages": []  # You can add messages later
        }
        
        # Save to data.json in current folder
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
        
        print(Fore.YELLOW + "data.json created!")
        print(Fore.CYAN + "Pushing to GitHub...")
        
        # Git commands
        os.system("git add data.json")
        os.system('git commit -m "Update from parish app" || true')
        push_result = os.system("git push")
        
        if push_result == 0:
            print(Fore.GREEN + "✅ Online portal updated successfully!")
            print(Fore.WHITE + "Members can now refresh the portal link to see latest data.")
        else:
            print(Fore.RED + "❌ Push failed — check internet or GitHub token.")
        
        input(Fore.YELLOW + "\nPress Enter to continue...")

    # ---------------- MENU ----------------
    def display_menu(self):
        self.clear_screen()
        print(Fore.CYAN + Style.BRIGHT + "=" * 70)
        print(self.parish_info["name"].center(70))
        print("=" * 70)

        print(Fore.YELLOW + "\nLatest Message:")
        print(Fore.WHITE + "Christmas brings joy and hope. Merry Christmas! 🎄\n")

        print(Fore.MAGENTA + f"Total Members: {len(self.members)}\n")

        print(Fore.CYAN + "MAIN MENU")
        print("1. Add Member")
        print("2. View Member")
        print("3. List All Members")
        print("4. Search")
        print("5. Edit Member")
        print("6. Delete Member")
        print("7. Birthday Reminders")
        print("8. WhatsApp Message")
        print("9. Share on Facebook")
        print("10. Broadcast Message")
        print("11. Manage Images")
        print("12. Update Online Portal")  # New!
        print("13. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nChoose (1-12): ").strip()

            if choice == "1":
                self.add_member()
            elif choice == "2":
                self.view_member()
            elif choice == "3":
                self.list_all_members()
            elif choice == "4":
                self.coming_soon("SEARCH")
            elif choice == "5":
                self.coming_soon("EDIT MEMBER")
            elif choice == "6":
                self.coming_soon("DELETE MEMBER")
            elif choice == "7":
                self.coming_soon("BIRTHDAY REMINDERS")
            elif choice == "8":
                self.coming_soon("WHATSAPP MESSAGE")
            elif choice == "9":
                self.coming_soon("SHARE ON FACEBOOK")
            elif choice == "10":
                self.coming_soon("BROADCAST MESSAGE")
            elif choice == "11":
                self.coming_soon("MANAGE IMAGES")
            elif choice == "12":
                            self.update_online()
            elif choice == "13":
              print(Fore.CYAN + "\nGod bless Sunrise Parish! 🌅\n")
                break
            else:
                print(Fore.RED + "Invalid choice!")

            input(Fore.YELLOW + "\nPress Enter to continue...")


if __name__ == "__main__":
    ParishApp().run()
