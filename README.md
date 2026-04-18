# Canadian Crime Severity Index Dashboard

## Project Overview
This project is a Django-based web application that visualizes Crime Severity Index (CSI) data from Statistics Canada. The application allows users to explore crime trends over time using interactive charts and tables.

The dataset measures crime severity by considering both the volume and seriousness of offences, providing a more accurate representation of crime patterns in Canada.

---

## Features
- Import crime data from CSV into a database
- Store data using SQLite and Django ORM
- Filter crime data by year and metric
- Visualize trends using line and bar charts
- Admin panel for managing records

---

## Technology Stack
- **Backend:** Django
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **Visualization:** Chart.js
- **Language:** Python

---

## Dataset
- Source: Statistics Canada
- Format: CSV
- Fields:
  - Geography (Canada)
  - Year
  - Metric (CSI, Violent CSI, Non-violent CSI)
  - Value

---

## Development Environment Setup

### Prerequisites
Ensure you have the following installed:

- Python **3.10+**
- pip (Python package manager)
- Git

---

## Installation Steps

### 1. Clone the repository
```bash
git clone https://github.com/jerry-oleribe/crime-dashboard.git
cd crime-dashboard