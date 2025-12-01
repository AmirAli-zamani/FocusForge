#!/bin/sh

# صبر کردن برای دیتابیس
echo "Waiting for database..."
python manage.py wait_for_db

# اجرای مایگریشن‌ها
echo "Running migrations..."
python manage.py migrate

# اجرای سرور
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
