# -*- coding: utf-8 -*-
import json

clients = []

def add_client():
    name = input("Client name: ")
    phone = input("Phone number: ")
    time = input("Appointment date and time (e.g. 2025-05-14 15:30): ")

    client = {"name": name, "phone": phone, "time": time}
    clients.append(client)
    print("✅ Client added!\n")

def show_clients():
    if not clients:
        print("📭 No records yet.\n")
    else:
        print("📋 Client list:")
        for i, c in enumerate(clients, 1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['time']}")
        print()

def save_to_file():
    with open("clients.json", "w", encoding="utf-8") as f:
        json.dump(clients, f, ensure_ascii=False, indent=4)
    print("💾 Data saved to 'clients.json'\n")

def main():
    while True:
        print("Menu:")
        print("1. Add client")
        print("2. Show client list")
        print("3. Save to file")
        print("4. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            add_client()
        elif choice == "2":
            show_clients()
        elif choice == "3":
            save_to_file()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()

