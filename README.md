# Encrypt-Pro
AI-powered file encryption platform using AES, RSA and ChaCha20.
Encryptor Pro is a cybersecurity desktop application developed using Python and CustomTkinter that provides secure encryption and decryption for text files, images, videos, and other digital assets.

The platform intelligently selects the most suitable encryption algorithm based on file characteristics, risk level, and performance requirements.

🚀 Features
🔒 Hybrid AES + RSA Encryption
AES-256 encrypts file contents efficiently.
RSA encrypts the AES session key for secure key exchange.
Ideal for sensitive and confidential files.
⚡ ChaCha20 Encryption
High-speed encryption for large files and multimedia content.
Optimized for videos and large datasets.
Provides strong security with excellent performance.
🤖 AI Security Assistant
Analyzes uploaded files.
Calculates security score and risk level.
Recommends the most suitable encryption algorithm.
Explains recommendations in simple language.
📝 Supported File Types
Text Files (.txt)
Images (.png, .jpg, .jpeg)
Videos (.mp4, .avi, .mkv, .mov)
Documents (.pdf, .docx)
Spreadsheets (.xlsx, .csv)
Archives (.zip, .rar)
📜 Encryption History
Stores encryption and decryption activities.
Tracks file names, timestamps, and algorithms used.
👤 User Authentication
Secure login and registration system.
Password hashing using bcrypt.
User-specific encryption history.
🏗 System Architecture

User File
↓
AI Security Analysis
↓
Risk Assessment
↓
Algorithm Recommendation
↓
Encryption Process
↓
Secure Storage

🔐 Encryption Strategy
File Type	Recommended Algorithm
Sensitive Documents	AES + RSA
Images	AES + RSA
Small Videos	AES + RSA
Large Videos	ChaCha20
Large Files	ChaCha20
🧠 AI Decision Rules
High-risk or confidential files use AES + RSA Hybrid Encryption.
Large videos and media files use ChaCha20 for improved performance.
Large files are automatically optimized for encryption speed.
The AI assistant provides simple explanations for every recommendation.
🛠 Technologies Used
Python
CustomTkinter
SQLite
AES-256
RSA-2048
ChaCha20
bcrypt
Lemma AI Agents
📷 Screenshots
Login Page

(Add Screenshot)

Dashboard

(Add Screenshot)

Encryption Center

(Add Screenshot)

AI Security Assistant

(Add Screenshot)

History Page

(Add Screenshot)

🎥 Demo Video

Demo Video Link:
(Add Link Here)

📦 Installation

Clone the repository:

git clone https://github.com/VenkatVishal-VK/Encrypt-Pro.git

Navigate to the project folder:

cd Encrypt-Pro

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py
🎯 Hackathon Objective

Encryptor Pro was developed as a hackathon project to demonstrate how artificial intelligence and modern cryptography can work together to provide intelligent and user-friendly cybersecurity solutions.

The project combines strong encryption standards with AI-driven decision making to improve both security and usability.

👨‍💻 Developer

Venkat Vishal V K

📄 License

This project was developed for educational and hackathon purposes.
