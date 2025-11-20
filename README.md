# GeoShop Locator (Django + GeoDjango + PostGIS)

A geospatial web application built using **Django**, **GeoDjango**, **Leaflet**, and **PostGIS** that allows users to:

- Create an account and log in  
- Add shops using an interactive map  
- Save shop coordinates as a **PostGIS Point geometry**  
- View, update, and delete their own shops  
- Display all shops on a Leaflet map  
- Filter shops by name, address, and category  

---

## 🚀 Features

### 🗺️ GeoDjango + PostGIS
- Each shop's location is stored as a **PointField** in PostGIS.
- Coordinates are captured by Leaflet and automatically converted into `Point(lon, lat, srid=4326)`.

### 👤 User Authentication
- Custom login, signup, and logout system.
- Logged-in users can only manage (update/delete) their own shops.

### 🏪 Shop Management
- Add shop with name, address, category, and map location.
- CRUD operations: Create, Read, Update, Delete.
- “View Shops” table with coordinates (longitude, latitude).

### 🗂️ Dashboard with Search
- Filter by:
  - Shop name  
  - Address  
  - Category  
- Option to “Show All Shops”.

---

## 🏗️ Tech Stack

**Backend**
- Django 5.2.x  
- GeoDjango  
- PostgreSQL + PostGIS  
- GDAL / GEOS / PROJ (OSGeo4W on Windows)  

**Frontend**
- Leaflet.js  
- Bootstrap 5  
- JavaScript for map interaction  

---

## 📁 Project Structure

geomap_stores/
│── geomap_stores/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│── shops/
│ ├── migrations/
│ ├── templates/
│ │ ├── base.html
│ │ ├── dashboard.html
│ │ ├── shop_form.html
│ │ ├── view_shop.html
│ │ ├── login.html
│ │ ├── sign_up.html
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│── static/
│── manage.py
│── requirements.txt
│── README.md

yaml
Copy code

---

# 🛠️ Installation Instructions (Windows)

### 1️⃣ Clone Repo & Create Virtual Environment
git clone <your-repo-url>
cd geomap_stores
python -m venv venv
venv\Scripts\activate

shell
Copy code

### 2️⃣ Install Dependencies
pip install -r requirements.txt

shell
Copy code

### 3️⃣ Install & Configure OSGeo4W  
Download OSGeo4W (64-bit):

https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup-x86_64.exe

markdown
Copy code

Install packages:
- **gdal**
- **geos**
- **proj**

### 4️⃣ Configure GeoDjango (in settings.py)
Make sure these paths are added at the top of settings:

OSGEO4W = r"C:\OSGeo4W"
os.environ["OSGEO4W_ROOT"] = OSGEO4W
os.environ["GDAL_DATA"] = fr"{OSGEO4W}\share\gdal"
os.environ["PROJ_LIB"] = fr"{OSGEO4W}\share\proj"
os.environ["PATH"] = fr"{OSGEO4W}\bin;" + os.environ["PATH"]

GEOS_LIBRARY_PATH = r"C:\OSGeo4W\bin\geos_c.dll"
GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal311.dll"

r
Copy code

### 5️⃣ Configure PostGIS Database
In PostgreSQL:

```sql
CREATE DATABASE geomap_stores_db;
\c geomap_stores_db
CREATE EXTENSION postgis;
Make sure settings.py matches your credentials.

🔧 Run Migrations
nginx
Copy code
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
▶️ Run Development Server
nginx
Copy code
python manage.py runserver
Open browser:

cpp
Copy code
http://127.0.0.1:8000/
