# TaskUP

### Help the community around you with small, fun tasks

## Features
 - Singpass Login
 - SGqrcode for PayNow
 - OneMap routing and geocoding

## Installation Instructions
Create and activate virtual environment
```
cd server
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
Run initialise_users.py and initialise_errands.py
```
cd server
python initialise_users.py
python initialise_errands.py
```
Run the backend server
```
cd server
python app.py
```
Initialise and Run the React Client
```
cd client
npm install
npm run dev
```
