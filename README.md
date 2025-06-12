# 🚗 Flask Car Booking Web App
A simple and user-friendly car booking system built with Flask. Users can register, log in, view available cars, and book them. It features secure password storage, session handling, and real-time car availability updates.

## ✅ Features
- User Authentication
- Register with username and hashed password
- Login & logout with session management via Flask-Login

## 🚘 Car Booking
- View all available cars
- Book a car (removes from available listings)
- Only logged-in users can make bookings

## 🗃️ Database
- Data stored in SQLite
- ORM support via SQLAlchemy

## 🧰 Tech Stack
- Component	Technology
- Backend	Flask
- Auth	Flask-Login
- Password Hashing	Werkzeug
- ORM	SQLAlchemy
- Database	SQLite (default)
- Language	Python 3.x

## 🔒 Routes Overview
- Route	Description
- /Homepage with car listings
- /register	Register a new user
- /login	Log in existing user
- /logout	Log out
- /book/<car_id>	Book a car (auth required)

## 🛠 To-Do
- Add admin dashboard for managing cars
- Improve UI with Bootstrap
- Add availability dates for bookings
- Implement email confirmation for bookings
- Deploy to Render or Railway
