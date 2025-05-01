# RFID_Based_Stud_Attendance

1. (Optional) Create a virtual environment. It helps a lot
2. Packages to install 
    (Recommended way)
    pip install Django
    pip install django-import-export
    pip install openpyxl
    pip install schedule

(or install using requirements.txt file pip install -r requirements.txt)
If additional packages are needed then install them (numpy , pandas) only if asked

(Make sure the terminal is on the "RFID_Attendance_System" folder)
3. Run the server
    python manage.py runserver

4. Run the automated_mail_system in different terminal
    python module_automated_attendance.py

5. Use the "username_passwords.txt" to login to different accounts

6. To simulate NODE_MCU marking attendance use the following links in browser

Teacher:
http://127.0.0.1:8000/mark/?rfid=d966514
http://127.0.0.1:8000/mark/?rfid=rf_10

Students:
http://127.0.0.1:8000/mark/?rfid=c12f51d
http://127.0.0.1:8000/mark/?rfid=rf_2
http://127.0.0.1:8000/mark/?rfid=rf_3
http://127.0.0.1:8000/mark/?rfid=rf_4
http://127.0.0.1:8000/mark/?rfid=rf_5


Note:- I have removed my email and password from the settings.py file at the last line
Also, I have commented the send_mass_mail() function so that it wont actually send the mail to the student
If you want to try it then add your email and password in settings.py file and uncomment the send_mass_mail() function from the code in the files ,'teacher_dashboard/views.py' and 'module_automated_attendance.py'
