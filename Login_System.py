import json
import os
import hashlib
import time
import random
import sys

# ===== Header =====
def show_header():
    print("=" * 50)
    print("       Secure Multi-Role Login System")
    print("             by RedMark")
    print("=" * 50)
    time.sleep(1)

# ===== Constants =====
USER_FILE = "users.json"
MAX_ATTEMPTS = 3
IDLE_TIMEOUT = 30  # seconds

# ===== Utils =====
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as f:
            json.dump({}, f)
    with open(USER_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# ===== CAPTCHA =====
def simulate_recaptcha():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = a + b
    try:
        user_input = int(input(f"CAPTCHA: What is {a} + {b}? "))
        return user_input == answer
    except:
        return False

# ===== Registration =====
def register():
    print("\n--- Register New User ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    role = input("Enter role (admin/user): ").strip().lower()

    if role not in ['admin', 'user']:
        print("Invalid role. Choose 'admin' or 'user'.")
        return

    users = load_users()
    if username in users:
        print("User already exists.")
        return

    users[username] = {
        "password": hash_password(password),
        "role": role
    }
    save_users(users)
    print(f"User '{username}' registered successfully as {role}!")

# ===== Forgot Password =====
def forgot_password():
    print("\n--- Forgot Password ---")
    username = input("Enter your username: ").strip()
    users = load_users()

    if username not in users:
        print("User not found.")
        return

    new_password = input("Enter new password: ").strip()
    users[username]['password'] = hash_password(new_password)
    save_users(users)
    print("Password updated successfully.")

# ===== Login =====
def login():
    print("\n--- Login ---")
    attempts = 0
    last_attempt_time = time.time()

    while attempts < MAX_ATTEMPTS:
        if time.time() - last_attempt_time > IDLE_TIMEOUT:
            print("Session timed out due to inactivity.")
            return None, None

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if not simulate_recaptcha():
            print("Failed CAPTCHA. Try again.")
            attempts += 1
            continue

        users = load_users()
        if username in users and users[username]['password'] == hash_password(password):
            print(f"Welcome, {username}! Role: {users[username]['role']}")
            return username, users[username]['role']

        else:
            print("Invalid credentials. Try again.")
            attempts += 1
            last_attempt_time = time.time()

    print("Too many failed attempts. Access locked.")
    return None, None

# ===== Main =====
def main():
    show_header()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            username, role = login()
            if username:
                print(f"\nAccess granted. You are logged in as '{role}'.")
                # Role-based actions here (customize as needed)
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()