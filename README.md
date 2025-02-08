# QRListGen – QR Code List Generator

**Description**

This project uses Flask and the qrcode package in Python to generate QR codes for:

A list of items sold at a hotel (e.g., menu items, room services).

A list of items bought by a customer in a grocery store (e.g., receipts, purchase summary).

The generated QR codes can be scanned to quickly access the details of items, improving customer convenience and efficiency in transactions.

**Features**

✅ Generate QR codes for item lists dynamically.

✅ Display QR codes using an HTML frontend.

✅ Simple and lightweight Flask backend.

✅ Easy integration with hotel and grocery store systems.

**Technologies Used**

Python (Flask, qrcode)

HTML

MongoDB (storing item lists)

**Installation**

*->Clone the repository:*

git clone https://github.com/your-username/qr-code-hotel-grocery.git

cd qr-code-hotel-grocery

*->Install dependencies:*

pip install flask qrcode

*->Run the Flask server:*

python app.py

Open your browser and go to:
http://127.0.0.1:5000

**Usage**

Enter a list of items in the provided input form.
Click Generate QR Code to create a QR code for the list.
Download or scan the QR code to view the item details.

**Screenshots**

![hi1](https://github.com/user-attachments/assets/5568b3c9-8b18-40d8-bdae-111655acfc0c)
![land](https://github.com/user-attachments/assets/988c5271-2a4f-4b88-bdc1-2e6d3716e645)
![qr_code](https://github.com/user-attachments/assets/12bfe1e9-4dfe-4d2a-9bc7-c7ab1b418680)


**Future Improvements**

🔹 Add database support to save QR codes and item lists.

🔹 Integrate with hotel POS and grocery billing systems.

🔹 Improve UI/UX with better design and animations.

**License**

📜 MIT License

