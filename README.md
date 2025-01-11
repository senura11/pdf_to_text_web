PythonAnywhere එකේදී GitHub එකෙන් code එක clone කරලා web app එක deploy කිරීම සඳහා පහත පියවර අනුගමනය කරන්න:

---

### 1. **PythonAnywhere Account එකක් Create කිරීම**
1. [PythonAnywhere](https://www.pythonanywhere.com/) website එකට ගොස් account එකක් create කරන්න.
2. Free tier එකක් හෝ paid plan එකක් select කරන්න.

---

### 2. **GitHub Repository Clone කිරීම**
1. PythonAnywhere dashboard එකේ, **Consoles** tab එකට ගොස් **Bash console** එකක් open කරන්න.

2. GitHub repository එක clone කරන්න. උදාහරණයක් වශයෙන්:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

   - `your-username` වෙනුවට ඔබේ GitHub username එක යොදන්න.
   - `your-repo-name` වෙනුවට ඔබේ repository name එක යොදන්න.

   උදාහරණයක් වශයෙන්:

   ```bash
   git clone https://github.com/senura11/pdf_to_text_web.git
   ```

3. Clone කරපු repository එකට ඇතුළු වන්න:

   ```bash
   cd pdf_to_text_web
   ```

---

### 3. **Virtual Environment Setup කිරීම**
1. Virtual environment එක create කරන්න:

   ```bash
   python3 -m venv venv
   ```

2. Virtual environment එක activate කරන්න:

   ```bash
   source venv/bin/activate
   ```

3. Dependencies install කරන්න:

   ```bash
   pip install -r requirements.txt
   ```

---

### 4. **Web App Setup කිරීම**
1. PythonAnywhere dashboard එකේ, **Web** tab එකට ගොස් **Add a new web app** බොත්තම ඔබන්න.
2. **Flask** තෝරාගෙන, Python version එක select කරන්න (උදාහරණයක් වශයෙන් Python 3.8).
3. **Next** ක්ලික් කරන්න.

---

### 5. **Web App Configuration**
1. **Source code** සහ **Working directory** set කරන්න:
   - **Source code**: ඔබේ project folder එකේ path එක set කරන්න (උදාහරණයක් වශයෙන් `/home/your-username/pdf_to_text_web`).
   - **Working directory**: එම path එකම set කරන්න.

2. **WSGI Configuration File** එක edit කරන්න:
   - PythonAnywhere dashboard එකේ, **Web** tab එකේදී **WSGI configuration file** link එක ඔබන්න.
   - WSGI file එකේ පහත code එක add කරන්න:

     ```python
     import os
     import sys

     # Add your project directory to the Python path
     path = '/home/your-username/pdf_to_text_web'
     if path not in sys.path:
         sys.path.append(path)

     # Set the environment variable for Flask
     os.environ['FLASK_APP'] = 'run.py'

     # Import the Flask app
     from app import app as application
     ```

     - `your-username` වෙනුවට ඔබේ PythonAnywhere username එක යොදන්න.
     - `pdf_to_text_web` වෙනුවට ඔබේ project folder එකේ name එක යොදන්න.

3. **Save** ක්ලික් කරන්න.

---

### 6. **Static Files සහ Templates Setup කිරීම**
1. PythonAnywhere dashboard එකේ, **Web** tab එකේදී **Static files** section එකට ගොස්:
   - **URL**: `/static/`
   - **Path**: `/home/your-username/pdf_to_text_web/static/`

2. **Templates** folder එක set කිරීම:
   - ඔබේ `templates` folder එක `app` folder එක තුල තිබේ නම්, එය automatically detect වනු ඇත.

---

### 7. **Uploads Folder Create කිරීම**
PDF files upload කිරීම සඳහා `uploads` folder එක create කරන්න.

1. Bash console එකේදී පහත command භාවිතා කරන්න:

   ```bash
   mkdir /home/your-username/pdf_to_text_web/uploads
   ```

2. `app/__init__.py` file එකේ `UPLOAD_FOLDER` path එක update කරන්න:

   ```python
   app.config['UPLOAD_FOLDER'] = '/home/your-username/pdf_to_text_web/uploads'
   ```

---

### 8. **Web App Reload කිරීම**
PythonAnywhere dashboard එකේ, **Web** tab එකේදී **Reload** බොත්තම ඔබන්න. මෙය web app එක restart කරනු ඇත.

---

### 9. **Web App Access කිරීම**
PythonAnywhere dashboard එකේ, **Web** tab එකේදී ඔබේ web app එකේ URL එක පෙන්වනු ඇත. එම link එක භාවිතා කරලා web app එක access කරන්න.

---

### 10. **Update කිරීම**
ඔබේ web app එක update කිරීම සඳහා:

1. GitHub repository එකේ changes pull කරන්න:

   ```bash
   git pull origin main
   ```

2. Virtual environment එකේ dependencies update කරන්න (අවශ්යයි නම්):

   ```bash
   pip install -r requirements.txt
   ```

3. PythonAnywhere dashboard එකේ, **Web** tab එකේදී **Reload** බොත්තම ඔබන්න.

---

### 11. **Debugging**
Web app එකේ issues තිබේ නම්:

1. **Error Logs Check කරන්න**:
   - PythonAnywhere dashboard එකේ, **Web** tab එකේදී **Error log** link එක ඔබන්න.
   - මෙම log එකේ errors සහ warnings පෙන්වනු ඇත.

2. **Server Logs Check කරන්න**:
   - **Server log** link එක ඔබන්න. මෙය server-side issues identify කිරීමට උපකාරී වේ.

---

### Summary
1. GitHub repository එක clone කරන්න.
2. Virtual environment setup කරන්න.
3. Web app configuration කරන්න.
4. Static files සහ templates setup කරන්න.
5. Web app reload කරන්න.
6. Web app එක access කරන්න.

මෙම steps අනුගමනය කිරීමෙන්, ඔබේ Flask web app එක PythonAnywhere එකේදී deploy කිරීම සිදු කළ හැක.