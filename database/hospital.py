from ntpath import realpath
import sqlite3
import random


def add_doc(ID, NAME, PHONE_NUMBER, TYPE):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO DOCTOR VALUES (?,?,?,?)", (ID, NAME, PHONE_NUMBER, TYPE))
    #commit command and exit
    conn.commit()
    conn.close()

def add_patient(ID, NAME, EMAIL_ADDRESS, PHONE_NUMBER, PROBLEM, DOCTOR_ID):
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()

    # Ensure the doctor with the specified DOCTOR_ID exists before adding the patient
    c.execute("SELECT COUNT(*) FROM DOCTOR WHERE ID=?", (DOCTOR_ID,))
    doctor_exists = c.fetchone()[0]

    if doctor_exists:
        # Add the patient to the PATIENT table
        c.execute("INSERT OR IGNORE INTO PATIENT (ID, NAME, EMAIL_ADDRESS, PHONE_NUMBER, PROBLEM, DOCTOR_ID) VALUES (?, ?, ?, ?, ?, ?)",
                  (ID, NAME, EMAIL_ADDRESS, PHONE_NUMBER, PROBLEM, DOCTOR_ID))
        print("Patient added successfully.")
    else:
        print(f"Error: Doctor with ID {DOCTOR_ID} does not exist.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

conn = sqlite3.connect('hospital.db')
query = (''' CREATE TABLE IF NOT EXISTS DOCTOR
            (ID             INTEGER     PRIMARY KEY,
            NAME            TEXT        NOT NULL,
            PHONE_NUMBER    CHAR(20)    NOT NULL,
            TYPE            TEXT);''')

conn.execute(query)

query = (''' CREATE TABLE IF NOT EXISTS PATIENT
            (ID             INTEGER     PRIMARY KEY,
            NAME            TEXT        NOT NULL,
            EMAIL_ADDRESS   TEXT        NOT NULL,
            PHONE_NUMBER    CHAR(20)    NOT NULL,
            PROBLEM         TEXT,
            DOCTOR_ID       INTEGER     NOT NULL,
            FOREIGN KEY(DOCTOR_ID)  REFERENCES  DOCTOR(ID)
            );''')


# for i in range(1, 11):
#     add_doc(i, f"Doctor {i}", f"123-456-{i*1111}", "General Practitioner")

# # Generate 10 patients with random doctor IDs
# for i in range(1, 11):
#     patient_id = i + 100  # to distinguish patient IDs from doctor IDs
#     doctor_id = random.randint(1, 10)  # choose a random doctor ID
#     add_patient(patient_id, f"Patient {i}", f"patient{i}@example.com", f"987-654-{i*1111}", f"Illness {i}", doctor_id)



c = conn.cursor()
c.execute("SELECT * FROM DOCTOR")
items = c.fetchall()
for item in items:
    print(item)

c.execute("SELECT * FROM PATIENT")
items = c.fetchall()
for item in items:
    print(item)


conn.execute(query)
conn.commit()
conn.close()

