# Login_System_YT
"I’m creating this login system project specially for my YouTube family. This is a complete playlist where we’ll build a secure, real-world login system using Python. This project is going to be very helpful for all of you, and I hope it adds great value to your learning journey."





# RedMark-LoginSystem

A real-world, secure and offline-capable command-line login system built in Python. This project is ideal for educational use, admin dashboards, restricted tools, and internal system access environments. It implements real-world authentication features such as multi-user roles, session timeouts, secure password storage, and more — all without requiring internet access.

---

## 🔐 Features

* **Multi-user roles:** Supports both `admin` and `user` accounts with role-based access control
* **Forgot password:** Reset passwords securely without OTP verification
* **Simulated reCAPTCHA:** Simple human check using math-based challenge
* **Login attempt limits:** Lockout after 3 failed login attempts
* **Auto-logout:** Session times out after 30 seconds of inactivity
* **Password hashing:** Uses SHA-256 for storing passwords securely
* **JSON-based storage:** User records are stored in `users.json` file
* **Offline executable:** Can be packaged into a `.exe` using `PyInstaller`
* **Author credit:** Login interface includes "by RedMark" for attribution

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/RedMark-LoginSystem.git
cd RedMark-LoginSystem
```

### 2. Install Python (if not already installed)

[Download Python](https://www.python.org/downloads/)

### 3. Run the Program

```bash
python login_system.py
```

---

## 💡 Example Users

Sample `users.json` structure:

```json
{
  "adminuser": {
    "password": "<hashed_password>",
    "role": "admin"
  },
  "normaluser": {
    "password": "<hashed_password>",
    "role": "user"
  }
}
```

Users can register via the CLI menu, and passwords are automatically hashed.

---

## 🛠 Packaging as .EXE (For Offline Distribution)

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Build Executable

```bash
pyinstaller --onefile login_system.py
```

This generates an `.exe` file inside the `dist/` directory.

---

## 📁 Project Structure

```
RedMark-LoginSystem/
├── login_system.py      # Core Python application
├── users.json           # User database (auto-generated)
├── README.md            # Project overview and usage
```

---

## 👤 Author

**RedMark** – Python developer focused on building practical, secure, and efficient CLI tools for real-world use.

> GitHub Profile: [github.com/RedMark](https://github.com/RedMark) *(update with actual profile)*

---


---

## ❤️ Support & Contributions

If you find this useful:

* ⭐ Star the repository
* 🍴 Fork it for your own improvements
* 🛠 Contribute by submitting PRs or reporting issues

---

## 🧠 Planned Features

* OTP-based password reset (optional email integration)
* Activity logging and admin audit trail
* GUI-based version using Tkinter or PyQt

---

**Built with 💻 Python & secured with logic — by RedMark**

