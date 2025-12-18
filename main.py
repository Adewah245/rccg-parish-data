import os
import json
import subprocess
from datetime import datetime, timedelta

# ================== CONFIG ==================
PARISH_NAME = "RCCG BENUE 2 SUNRISE PARISH"
ZONE = "Young & Adults Zone"
MEMBERS_FILE = "parish_members.json"
PHOTO_DIR = "photos"

os.makedirs(PHOTO_DIR, exist_ok=True)

def load_members():
    if not os.path.exists(MEMBERS_FILE):
        return []
    with open(MEMBERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_members(members):
    with open(MEMBERS_FILE, "w", encoding="utf-8") as f:
        json.dump(members, f, indent=4, ensure_ascii=False)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    members = load_members()
    total = len(members)
    clear_screen()
    print(f"{PARISH_NAME}")
    print(f"{ZONE}\n")
    print("=" * 70)
    print(f"         ⛪ RCCG BENUE 2 SUNRISE PARISH YOUNG AND ADULTS ZONE")
    print("=" * 70)
    print(f"                          👥 Total Members: {total}     ")
    print("")
    print("       📢 Christmas brings about a bounty of joy and message")
    print("         of hope, love, and salvation through our Lord Jesus Christ.")
    print("=" * 70)

def add_member():
    # Same simple add function as latest version
    print("\n➕ ADD NEW MEMBER")
    name = input("Full Name: ").strip()
    if not name:
        print("❌ Name required!")
        input("Press Enter...")
        return
    phone = input("Phone Number: ").strip()
    email = input("Email (optional): ").strip()
    address = input("Address (optional): ").strip()
    
    print("\nDate of Birth")
    try:
        day = int(input("  Day (1-31): "))
        month = int(input("  Month (1-12): "))
        year = int(input("  Year (e.g. 1995): "))
        dob = datetime(year, month, day)
        birthday = dob.strftime("%d-%m-%Y")
    except:
        print("❌ Invalid date!")
        input("Press Enter...")
        return
    
    print(f"\n📷 Place photo in '{PHOTO_DIR}/' folder first")
    photo_name = input("Enter filename (optional): ").strip()
    photo_path = os.path.join(PHOTO_DIR, photo_name) if photo_name else ""
    if photo_name and not os.path.exists(photo_path):
        print("⚠️ Photo not found — added with note")
        photo_path = "Photo copy failed"
    
    members = load_members()
    new_member = {
        "name": name,
        "phone": phone,
        "address": address,
        "birthday": birthday,
        "joined": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    if email:
        new_member["email"] = email
    if photo_path:
        new_member["photo"] = photo_path if os.path.exists(photo_path) else "Photo copy failed"
    
    members.append(new_member)
    save_members(members)
    print(f"\n✅ {name} added successfully!")
    input("\nPress Enter...")

def search_member():
    # Same as latest
    query = input("\n🔍 Search by name or phone: ").strip().lower()
    members = load_members()
    found = [m for m in members if query in m["name"].lower() or query in m["phone"]]
    if not found:
        print("\n❌ No member found.")
    else:
        print(f"\n📋 Found {len(found)} member(s):\n")
        for m in found:
            print(f"Name     : {m['name']}")
            print(f"Phone    : {m['phone']}")
            print(f"Email    : {m.get('email', 'N/A')}")
            print(f"Address  : {m.get('address', 'N/A')}")
            print(f"Birthday : {m['birthday']}")
            print(f"Joined   : {m.get('joined', 'N/A')}")
            print(f"Photo    : {'Yes' if m.get('photo') and m['photo'] != 'Photo copy failed' else 'No/Missing'}")
            print("-" * 40)
    input("\nPress Enter...")

def list_all_members():
    # Same clean list
    members = load_members()
    if not members:
        print("\nNo members yet.")
    else:
        print(f"\n👥 ALL MEMBERS ({len(members)})")
        print("-" * 70)
        for i, m in enumerate(members, 1):
            photo_status = "📷" if m.get("photo") and m["photo"] != "Photo copy failed" else "⊝"
            print(f"{i:2}. {photo_status} {m['name']:25} | 📞 {m['phone']} | 🎂 {m['birthday']}")
    input("\nPress Enter...")

# Git sync functions (if you want to connect to web later)
def pull_from_web():
    print("\n📥 Pulling latest from web...")
    try:
        subprocess.run(["git", "pull"], check=True)
        print("✅ Updated!")
    except:
        print("❌ Git not set up or error.")
    input("Press Enter...")

def sync_to_web():
    print("\n🔄 Syncing to web...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Local update"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Synced!")
    except:
        print("❌ Git error.")
    input("Press Enter...")

# ================== MAIN LOOP - Now with your full menu in clean style ==================
while True:
    print_header()

    print("\nMENU")
    print("0. 📥 Pull Latest from Web App")
    print("1. ➕ Add Member")
    print("2. 🔍 Search / View Member")
    print("3. 👥 List All Members")
    print("4. 🎂 Upcoming Birthdays")
    print("5. ❌ Delete Member")
    print("6. 📩 Send Message")
    print("7. (Coming soon)")
    print("8. (Coming soon)")
    print("9. (Coming soon)")
    print("10. (Coming soon)")
    print("11. (Coming soon)")
    print("12. (Coming soon)")
    print("13. 🔄 Sync with Web App")
    print("14. 🚪 Exit\n")

    choice = input("Choose: ").strip()

    if choice == "0":
        pull_from_web()
    elif choice == "1":
        add_member()
    elif choice == "2":
        search_member()
    elif choice == "3":
        list_all_members()
    elif choice == "13":
        sync_to_web()
    elif choice == "14":
        clear_screen()
        print("\nGod bless you and the entire Sunrise Parish family!")
        print("Merry Christmas and a prosperous New Year! 🌅⛪🎄✝️\n")
        break
    else:
        print("\nComing soon...")
        input("Press Enter to continue...")
