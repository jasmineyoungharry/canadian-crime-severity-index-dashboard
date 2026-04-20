# Canadian Crime Severity Index Dashboard

## Course Information
Course: CPRO 2201 – Python Programming II  
Institution: Red Deer Polytechnic  
Term: Winter 2026  

## Group Members
- Jerry Oleribe  
- Jasmine Youngharry  
- Marvin Ehiaguina  

---

## Project Overview
This project is a Django-based web application that visualizes Crime Severity Index (CSI) data from Statistics Canada. The application imports crime data from a CSV file into a SQLite database and presents it using tables and charts to analyze **crime trends over time in Canada**.

The Crime Severity Index (CSI) is a weighted measure of crime that reflects both the number of crimes and the seriousness of offences.

---

## Features
- Import crime data from CSV into a database
- Store data using SQLite and Django ORM
- Filter crime data by year and metric
- Visualize trends using:
  - Line chart (trend over time)
  - Bar chart (latest year comparison)
- Admin panel for managing records
- Database verification using DB Browser for SQLite

---

## Technology Stack
- Backend: Django
- Database: SQLite
- Frontend: HTML, CSS
- Visualization: Chart.js
- Language: Python

---

## Dataset
Source: Statistics Canada  
Type: Crime Severity Index (CSI)  
Format: CSV  

Fields used:
- REF_DATE → Year  
- GEO → Geography (Canada)  
- Statistics → Crime metric  
- VALUE → Numeric value  

Crime metrics included:
- Crime Severity Index (CSI)  
- Violent Crime Severity Index  
- Non-violent Crime Severity Index  

 Important:
- Dataset is **Canada-level only**
- No province comparison
- Focus is **trend analysis over time**

---

# EXACT DEVELOPMENT ENVIRONMENT (Instructor Requirement)

To recreate this project successfully, use the following versions:

| Tool | Version |
|------|--------|
| Python | 3.11.0 |
| Django | 6.0.4 |
| SQLite | Built-in with Python |
| pip | Latest |
| OS Used | Windows 10/11 |
| IDE (optional) | PyCharm / VS Code |
| Browser | Chrome / Edge |

---

## Required Libraries

Install dependencies using:

pip install -r requirements.txt

Minimum required:
Django==6.0.4

(Optional depending on environment):
pandas

---

# HOW TO RECREATE THE DEVELOPMENT ENVIRONMENT (Step-by-Step)

Follow these steps exactly to run the project.

---

## Step 1 – Clone the repository

git clone https://github.com/jasmineyoungharry/canadian-crime-severity-index-dashboard 
cd crime-dashboard  

---

## Step 2 – Create virtual environment

python -m venv venv  

---

## Step 3 – Activate virtual environment

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

---

## Step 4 – Install dependencies

pip install -r requirements.txt  

---

## Step 5 – Apply database migrations

python manage.py migrate  

This creates the SQLite database structure.

---

## Step 6 – Import dataset into database

python manage.py import_crime_data data/crime_data.csv  

This step:
- Reads CSV file  
- Processes records  
- Stores them in SQLite database (`dashboard_crimerecord`)  

---

## Step 7 – Create admin user

python manage.py createsuperuser  

---

## Step 8 – Run the application

python manage.py runserver  

---

## Step 9 – Open in browser

Main app:
http://127.0.0.1:8000/  

Admin panel:
http://127.0.0.1:8000/admin/  

---

# HOW THE PROJECT WORKS

## Data Flow

CSV file → Django import command → SQLite database → Django models → Views → Web interface  

---

## Core Components

### Model
CrimeRecord:
- province_or_territory (represents Canada)
- year
- metric
- value

---

### Views
- Home → dataset summary  
- Data Table → filterable records  
- Charts → visualization  

---

### Charts
- Line chart → shows trend over time  
- Bar chart → compares metrics in latest year  

---

## Database

- Type: SQLite  
- File: db.sqlite3  
- Table: dashboard_crimerecord  

---

## Database Verification (Important)

To verify data:

1. Open DB Browser for SQLite  
2. Open db.sqlite3  
3. Select table:
   dashboard_crimerecord  

This confirms CSV → database conversion.

---

## Testing the Project

To confirm functionality:

- Run server  
- Open homepage  
- Verify data table loads  
- Apply filters  
- Open charts page  
- Confirm graphs display  
- Access admin panel  

---

## Expected Output

- Crime data table  
- Filtering functionality  
- Line chart (trend over time)  
- Bar chart (latest year comparison)  
- Admin panel  

---

## Limitations

- Dataset is Canada-level only  
- No province comparison  
- Basic UI design  
- Local development only  

---

## Future Improvements

- Add province-level data  
- Improve UI/UX  
- Add REST API  
- Deploy online  

---

## Contributors

Jerry Oleribe  
- Backend development  
- Database design  
- Data import implementation  

Jasmine Youngharry  
- Frontend templates  
- UI styling  
- Chart integration  

Marvin Ehiaguina  
- Dataset sourcing  
- Data cleaning  
- Testing and validation  

---

## References (APA)

Statistics Canada. (n.d.). Crime severity index (CSI).  
https://www150.statcan.gc.ca/  

Django Software Foundation. (n.d.). Django documentation.  
https://docs.djangoproject.com/  

Chart.js Contributors. (n.d.). Chart.js documentation.  
https://www.chartjs.org/docs/  

Python Software Foundation. (n.d.). Python documentation.  
https://docs.python.org/  

---

## License
This project is for academic purposes only.
