# lost-and-found
An API built with FastAPI for creating, updating, retrieving, and deleting lost and found items.

# Installation
create a virtual environm*ent:

python -m venv env

# Activate Virtual Environment
# Windows
env\Scripts\activate.bat

# Install dependencies:
pip install fastapi uvicorn sqlalchemy pymysql

# MySQL should be running and the database must exists:
-Database name: `lostandfoundapplication`
- Username: `root`

# Run the app :
uvicorn myapi:app --reload

# Open your browser and go to:
http://127.0.0.1:8000/docs
