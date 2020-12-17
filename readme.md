# Bubu Pharmacy
Bubu Pharmacy is a website that displays various kinds of drugs, drug supplies, and performs drug transactions. This website is made with the Django v.1.11 LTS Web Framework with a SQL Server database.

---

## Tools Required
 - Framework Djando v.1.11 LTS
 - Module Pyodbc

### How to install tools
```
    pip install Django==1.11.*
    pip install pyodbc
```

---

## How To Run Project
```
    python manage.py runserver --insecure
```

> Using `--insecure` because DEBUG is set to False, so testing without debugging requires it to run

### Note
Before running this project, make sure you have the necessary databases and tables.