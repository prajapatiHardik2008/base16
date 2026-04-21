# base16
# 🔐 Base16 Encoder / Decoder (Custom)

A simple Python CLI tool to encode and decode text using a **custom Base16 encoding**.

🔗 Repo: https://github.com/prajapatiHardik2008/base16

---

## 🚀 Features

- Encode text into custom Base16 format
- Decode Base16 back to original text
- Simple and beginner-friendly code
- No external libraries required

---

## 🧠 How It Works

- Each character → converted into **8-bit binary**
- Split into **two 4-bit parts**
- Each 4-bit value maps to a character from:


abcdefghijklmnop


### Example:


'f' → 01100110 → 0110 0110 → g g → "gg"


---

## 📦 Installation

```bash
git clone https://github.com/prajapatiHardik2008/base16.git
cd base16
python main.py
🖥️ Usage
------------------------
[+] 1 :- Encoding      |
[+] 2 :- Decoding      |
[+] 3 :- Exit          |
------------------------
Encode
Enter your Choice :- 1
Enter your text :- hello
Decode
Enter your Choice :- 2
Enter encoded text :- ...
🧪 Example
Input  : hi
Encoded: hg...
Decoded: hi
⚠️ Limitations
No validation for invalid input
Only works with correct encoded text
Not encryption (only encoding)
🔧 Future Improvements
File encode/decode support
GUI version
Custom alphabet support
👨‍💻 Author

Hardik Prajapati
GitHub: https://github.com/prajapatiHardik2008

⭐ Support

If you like this project, give it a ⭐ on GitHub!


---

If you want next level upgrade, I can add:
- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- :contentReference[oaicite:2]{index=2}

Just tell 👍
