### Step 1: Set Up Your Environment

1. **Install Flask**: If you haven't already, you can install Flask using pip. Open your terminal and run:
   ```bash
   pip install Flask
   ```

2. **Create a Project Directory**: Create a directory for your Flask project and navigate into it:
   ```bash
   mkdir flask_app
   cd flask_app
   ```

3. **Create a Directory for Templates**: Create a folder named `templates` where you will store your HTML files:
   ```bash
   mkdir templates
   ```

4. **Create a Directory for Static Files**: Create a folder named `static` for your CSS, JavaScript, and image files:
   ```bash
   mkdir static
   ```

### Step 2: Organize Your Files

Copy your HTML files into the `templates` directory and your CSS, JavaScript, and image files into the `static` directory. Your directory structure should look like this:

```
flask_app/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── who-are-we.html
│   ├── services.html
│   ├── Environmental.html
│   ├── contact-us.html
│   ├── Registration.html
│   ├── get-our-services.html
│
└── static/
    ├── css/
    ├── js/
    └── Images/
```

### Step 3: Create the Flask Application

Create a file named `app.py` in the `flask_app` directory and add the following code:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/who-are-we')
def who_are_we():
    return render_template('who-are-we.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/environmental')
def environmental():
    return render_template('Environmental.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')

@app.route('/registration')
def registration():
    return render_template('Registration.html')

@app.route('/get-our-services')
def get_our_services():
    return render_template('get-our-services.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 4: Run the Application

1. Open your terminal and navigate to the `flask_app` directory.
2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000/` to see your application in action.

### Step 5: Accessing Different Pages

You can access different pages by navigating to the following URLs:

- Home: `http://127.0.0.1:5000/`
- Who Are We: `http://127.0.0.1:5000/who-are-we`
- Services: `http://127.0.0.1:5000/services`
- Environmental: `http://127.0.0.1:5000/environmental`
- Contact Us: `http://127.0.0.1:5000/contact-us`
- Registration: `http://127.0.0.1:5000/registration`
- Get Our Services: `http://127.0.0.1:5000/get-our-services`

### Conclusion

You now have a basic Flask application that serves your HTML files and handles requests for different pages. You can expand this application by adding more functionality, such as handling form submissions, connecting to a database, or adding user authentication as needed.