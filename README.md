# Running a Flask Application

## Prerequisites
Ensure Flask is installed before running the application:

```bash
pip install flask
```

## Running Flask from Command Prompt (cmd)
1. Navigate to your project directory:
   ```cmd
   cd path\to\your\project
   ```
2. Set the Flask application:
   ```cmd
   set FLASK_APP=market.py
   ```
3. Run the Flask app:
   ```cmd
   flask run
   ```

## Running Flask from PowerShell
1. Navigate to your project directory:
   ```powershell
   cd path\to\your\project
   ```
2. Set the Flask application:
   ```powershell
   $env:FLASK_APP="app.py"
   ```
3. Run the Flask app:
   ```powershell
   flask run
   ```

## Running Flask with Debug Mode
To enable debug mode for automatic reloading:

### **Command Prompt:**
```cmd
set FLASK_DEBUG=1
```

### **PowerShell:**
```powershell
$env:FLASK_DEBUG = "1"
```
---
Your Flask app should now be running at **http://127.0.0.1:5000/** 🚀

## Running database from Command Prompt (cmd)
1. Navigate to your project directory:
   ```cmd
   cd path\to\your\project
   ```
2. Set the Flask application:
   ```cmd
   set FLASK_APP=market.py
   ```
3. Run the Flask app:
   ```cmd
   flask shell
   ```  
4. Write anything then:
   ```cmd
   from market import db
   db.create_all()
   ````