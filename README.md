
# 🛡️ Smart Password Manager (GUI Version)
A secure, modular desktop application for encrypted credential management.

## 📋 Overview
This project is a secure desktop application built with Python. It allows users to store and manage their sensitive passwords using industry-standard encryption, featuring a clean User Interface and real-time security analysis.

## 🌟 Key Features
* **AES-256 Encryption**: All passwords are encrypted using the `cryptography` library before being saved to local storage.
  
* **Modular Architecture**: Separates the **Security Logic** (`security_utils.py`) from the **User Interface** (`main_gui.py`).
  
* **Password Strength Checker**: Provides real-time visual feedback (Weak, Medium, or Strong) as the user types.
  
* **Automatic Password Generator**: Create high-entropy, random 16-character passwords with a single click.
  
* **Zero-Knowledge Storage**: The Master Password is never stored on disk; it's only used to derive keys during the active session.

## 🛠️ Tech Stack
* **Language:** Python 3.x
  
* **GUI Framework:** Tkinter (Built-in)
  
* **Security Library:** cryptography (Fernet & PBKDF2)

## 🚀 Installation & Usage

### 1. Clone the Repository
```bash
git clone <(https://github.com/PK-KN/Smart-Password-Manager)>
cd Smart-Password-Manager
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
```bash
python main_gui.py
```

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `main_gui.py` | Handles the window creation, button events, and user input. |
| `security_utils.py` | The backend engine for encryption and strength logic. |
| `requirements.txt` | Contains the external library dependencies. |
| `passwords.txt` | The local encrypted database (Generated on first save). |

## 🔒 Security Note
> [!WARNING]
> This project uses **Symmetric Encryption**. The "Master Password" is the only way to decrypt your data. If the Master Password is lost, the stored data **cannot be recovered** by any means.

