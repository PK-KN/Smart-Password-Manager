***Smart Password Manager (GUI Version)***

A secure desktop application built with Python that helps users store and manage their passwords using industry-standard encryption.

**🌟 Key Features**
**AES-256 Encryption:** All passwords are encrypted using the cryptography library before being saved.

**Modular Design:** Separates the security logic (security_utils.py) from the user interface (main_gui.py).

**Password Strength Checker:** Real-time feedback on how secure your password is (Weak, Medium, or Strong).

**Automatic Generator:** Create high-entropy, random passwords with one click.

**Zero-Knowledge Storage:** Your master password is never stored; it is only used to derive the decryption key.

🛠️ Tech Stack
Language: **Python 3.x**

*GUI Library:* **Tkinter (Built-in)**

*Security:* **Cryptography**

*🚀 How to Run*
**Clone the project:**

*Bash*
git clone <your-repository-link>

**Install the required library:**

*Bash*
pip install -r requirements.txt

**Run the application:**

*Bash*
python main_gui.py

**📂 Project Structure**
**main_gui.py:** The visual interface and user interactions.

**security_utils.py:** The "brain" of the app (Encryption, Strength checking, and Generation).

**requirements.txt:** List of Python libraries needed.

**passwords.txt:** (Generated automatically) Stores your encrypted data.

🔒 **Security Note**
*This project uses Symmetric Encryption. This means the same "Master Password" used to lock the vault is required to unlock it. If the Master Password is lost, the data cannot be recovered.*
