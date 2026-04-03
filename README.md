🛡️ Smart Password Manager (GUI Version)
A secure, modular desktop application for encrypted credential management.

📋 Overview
This project is a secure desktop application built with Python. it allows users to store and manage their sensitive passwords using industry-standard encryption, featuring a clean User Interface and real-time security analysis.

🌟 Key Features
1. AES-256 Encryption
All passwords are encrypted using the cryptography library before being saved to local storage.

2. Modular Architecture
The project separates the Security Logic (security_utils.py) from the User Interface (main_gui.py) for better maintainability and reusability.

3. Password Strength Checker
Provides real-time visual feedback (Weak, Medium, or Strong) as the user types, based on character complexity.

4. Automatic Password Generator
Create high-entropy, random 16-character passwords with a single click to ensure maximum security.

5. Zero-Knowledge Storage
The Master Password is never stored on disk. It is used only as a seed to derive the decryption key during the active session.

🛠️ Tech Stack
Language: Python 3.x

GUI Framework: Tkinter (Built-in)

Security Library: cryptography (Fernet & PBKDF2)

🚀 Installation & Usage
Step 1: Clone the Repository
Bash
git clone <your-repository-link>
Step 2: Install Dependencies
Bash
pip install -r requirements.txt
Step 3: Launch the Application
Bash
python main_gui.py
📂 Project Structure
main_gui.py: Handles the window creation, button events, and user input.

security_utils.py: The backend engine for encryption, strength logic, and generation.

requirements.txt: Contains the external library dependencies.

passwords.txt: The local encrypted database (Generated on first save).

🔒 Security Note
WARNING: This project uses Symmetric Encryption. The "Master Password" is the only way to decrypt your data. If the Master Password is lost, the stored data cannot be recovered by any means.
