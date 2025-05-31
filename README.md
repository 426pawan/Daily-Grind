# ☕ Daily-Grind

Daily-Grind is a simple, fun, and efficient To-Do List web application built with **Flask** and **SQLite** that helps you organize and track your everyday tasks effortlessly. Whether for studies, chores, or personal errands, Daily-Grind keeps your daily grind on point!

🔗 **Live Demo**: _[https://daily-grind.onrender.com]_

---

## 📝 Features

✅ Add daily tasks with a title and description  
✅ View all tasks in a neat, responsive list  
✅ Update tasks to keep up with changing plans  
✅ Delete tasks you’ve completed or no longer need  
✅ Minimal and mobile-friendly design for smooth use anywhere

---

## 📁 Project Structure

Daily-Grind  
├── static  
│   ├── css  
│   │   └── style.css  
│   └── js  
│       └── script.js  
├── templates  
│   ├── base.html  
│   ├── index.html  
│   ├── update.html  
│   └── 404.html  
├── app.py  
├── requirements.txt  
├── todo.db  
└── LICENSE

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/426pawan/Daily-Grind.git
cd Daily-Grind

2️⃣ Setup Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt


4️⃣ Initialize Database
python
Copy
Edit
from app import db
db.create_all()
exit()


5️⃣ Run the Application
bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000


⚙️ Tech Stack
Flask – Backend web framework

Flask-SQLAlchemy – ORM for database interaction

SQLite – Lightweight database

HTML, CSS, Bootstrap – Frontend and responsive design


📦 Dependencies (requirements.txt)
blinker==1.9.0

click==8.2.1

colorama==0.4.6

Flask==3.1.1

Flask-SQLAlchemy==3.1.1

greenlet==3.2.2

gunicorn==23.0.0

itsdangerous==2.2.0

Jinja2==3.1.6

MarkupSafe==3.0.2

packaging==25.0

SQLAlchemy==2.0.41

typing_extensions==4.13.2

Werkzeug==3.1.3

gunicorn==23.0.0


📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Contributions are welcome! Fork the repo and submit pull requests.

🙌 Acknowledgements
Thanks to all contributors and the open-source community!

Made with ☕ by Pawan Kumar
© 2025 All rights reserved.

vbnet
Copy
Edit

Let me know if you want me to generate the `requirements.txt` or add anything else!
