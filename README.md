# GeoShop Locator (Django + GeoDjango + PostGIS)

A geospatial web application built using **Django**, **GeoDjango**, **Leaflet**, and **PostGIS** that allows users to:

- Create an account and log in  
- Add shops using an interactive Leaflet map  
- Save shop coordinates as a **PostGIS Point geometry**  
- View, update, and delete their own shops  
- Display all shops on a map  
- Filter shops by name, address, and category  

---

## 🚀 Features

### 🗺️ GeoDjango + PostGIS
- Each shop's location is stored as a **PointField**
- Coordinates are captured via **Leaflet map click**
- Automatically converted to:

```
Point(lon, lat, srid=4326)
```

---

### 👤 User Authentication
- Custom login, signup, logout  
- Each user can manage only **their own shops**

---

### 🏪 Shop Management
- Add shop: name, address, category, and map location  
- Full **CRUD operations**  
- “View Shops” table with latitude & longitude  

---

### 🗂️ Dashboard with Search Filters
Search by:

- Shop name  
- Address  
- Category  

Additional:

- **Show All Shops** (view shops added by all users)

---

## 🏗️ Tech Stack

### 🔧 Backend
- Django 5.2.x  
- GeoDjango  
- PostgreSQL + PostGIS  
- GDAL / GEOS / PROJ (via OSGeo4W on Windows)

### 🎨 Frontend
- Leaflet.js  
- Bootstrap 5  
- Custom JavaScript for map events  

---

## 📁 Project Structure

```
geomap_stores/
│── geomap_stores/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
│── shops/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── shop_form.html
│   │   ├── view_shop.html
│   │   ├── login.html
│   │   ├── sign_up.html
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│
│── static/
│── manage.py
│── requirements.txt
│── README.md
```

---

## 🛠️ Installation Instructions (Windows)

### 1️⃣ Clone Repo & Create Virtual Environment

```bash
git clone https://github.com/Prashant6603/GeoDjango-shop-app.git
cd GeoDjango-shop-app

python -m venv venv
venv\Scripts\activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install & Configure OSGeo4W  
(Required for **GeoDjango, GDAL, GEOS, PROJ**)

Download OSGeo4W (64-bit):

https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup-x86_64.exe

Install packages:

- gdal  
- geos  
- proj  

---

### 4️⃣ Configure GeoDjango in `settings.py`

Add this at the **TOP**:

```python
OSGEO4W = r"C:\OSGeo4W"
os.environ["OSGEO4W_ROOT"] = OSGEO4W
os.environ["GDAL_DATA"] = fr"{OSGEO4W}\share\gdal"
os.environ["PROJ_LIB"] = fr"{OSGEO4W}\share\proj"
os.environ["PATH"] = fr"{OSGEO4W}\bin;" + os.environ["PATH"]

GEOS_LIBRARY_PATH = r"C:\OSGeo4W\bin\geos_c.dll"
GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal311.dll"   # Use correct version
```

---

### 5️⃣ Configure PostGIS Database

Open PostgreSQL:

```sql
CREATE DATABASE geomap_stores_db;
\c geomap_stores_db
CREATE EXTENSION postgis;
```

Make sure your credentials match `settings.py`.

---

### 🔧 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### ▶️ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

http://127.0.0.1:8000/

---

