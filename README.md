# Canvas-CrossLister
A web application that allows SDSU ITS staff to cross-list, combine and transfer the enrollments of a multiple sections of a course. 

Built using

- HTML5
- CSS
- Bootstrap
- JavaScript
- Python
- Django
- CanvasAPI

<h2>Prerequisites</h2>

To run this application, you must have Python installed on your computer. You will need Python 3 to use the tool. You can download it from here:

https://www.python.org/downloads/

You will also need the </strong>Canvas API key</strong>. The current Canvas URL in this version is set for beta testing only. Thus, you will need the API key from your beta environment, not production. If you don't know how to get the API key, then install the application first as it will tell you how to generate the key from your Canvas environment. 

Also refer to the project directory structure at the bottom, to refer how folders are set up within application. 

<h2>Setup & Installation</h2>

Download the repo into your local machine and unzip it. Makes sure to store it somewhere safe if you want to use the application on a regular basis.

Next, go inside the main <strong>Canvas-CrossLister</strong> directory. Open you terminal inside this directory and run the following command on your terminal to install all the packages and it's dependencies:

`python3 setup.py develop`

<h2>Running the Application</h2>

It is important to know that this application runs locally on your browser by starting a local server. So you have to start or run the server first. 

If you are inside <strong>Canvas-CrossLister</strong> directory, then go to the <strong>appliction</strong> folder. Now, run the following command from your terminal:

`python3 manage.py runserver`

If the command is successful, the terminal should give you an output stating the URL of the local server. This command started a localhost where your application is now currently running. The URL of your localhost is usually <strong>127.0.0.1:8000</strong>. 

IMPORTANT: Not all the time the URL of the localhost is set to <strong>127.0.0.1:8000</strong>. Make sure to verify using the terminal. 

<h2>Data</h2>

There is a data.json file that holds all our data and class information. This is one of the core components of the application.

Depending which CANVAS environmnent you are trying to connect the application, you will have to pull data from the respective instance. The current version has data.json loaded from the beta instance. 

Just in case you need to update the data.json for running the application on production,you will have to run the <strong>data.py</strong> first to update the data.json with production data. 

Go to the <strong>crosslist</strong> folder under the <strong>appliction</strong> directory. Run the following command on your terminal:

`python3 data.py`

You will have to run this command once, every semester or only when you need to update the data reflecting on your Canvas instance. 

<h2>Limitations</h2>

As of current, these are the following limitations you should be aware of when using the application:

- After crosslisting, the sub-accounts is not transferred. 
- SIS ID for the new shell is also not generated automatically. 
- You cannot de-crosslist through the application. 

<h2>Project Directory Structure</h2>

<pre>

├── Canvas-CrossLister
│   ├── Canvas_Crosslister.egg-info
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   ├── dependency_links.txt
│   │   ├── requires.txt
│   │   └── top_level.txt
│   ├── README.md
│   ├── __pycache__
│   │   └── main.cpython-37.pyc
│   ├── application
│   │   ├── __init__.py
│   │   ├── application
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-37.pyc
│   │   │   │   ├── settings.cpython-37.pyc
│   │   │   │   ├── urls.cpython-37.pyc
│   │   │   │   └── wsgi.cpython-37.pyc
│   │   │   ├── asgi.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── crosslist
│   │   │   ├── Front-End\ Backups
│   │   │   │   ├── static
│   │   │   │   │   ├── logo.png
│   │   │   │   │   └── main.css
│   │   │   │   └── templates
│   │   │   │       ├── app.html
│   │   │   │       ├── base.html
│   │   │   │       ├── confirm.html
│   │   │   │       ├── home.html
│   │   │   │       ├── mainBackup.py
│   │   │   │       ├── result.html
│   │   │   │       ├── run.html
│   │   │   │       └── sdsuLogo.jpeg
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-37.pyc
│   │   │   │   ├── admin.cpython-37.pyc
│   │   │   │   ├── apps.cpython-37.pyc
│   │   │   │   ├── mainBackup.cpython-37.pyc
│   │   │   │   ├── models.cpython-37.pyc
│   │   │   │   ├── urls.cpython-37.pyc
│   │   │   │   └── views.cpython-37.pyc
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── data.json
│   │   │   ├── data.py
│   │   │   ├── forms.py
│   │   │   ├── mainBackup.py
│   │   │   ├── migrations
│   │   │   │   ├── __init__.py
│   │   │   │   └── __pycache__
│   │   │   │       └── __init__.cpython-37.pyc
│   │   │   ├── models.py
│   │   │   ├── static
│   │   │   │   ├── logo.png
│   │   │   │   └── main.css
│   │   │   ├── templates
│   │   │   │   ├── app.html
│   │   │   │   ├── base.html
│   │   │   │   ├── confirm.html
│   │   │   │   ├── home.html
│   │   │   │   ├── mainBackup.py
│   │   │   │   ├── result.html
│   │   │   │   ├── run.html
│   │   │   │   └── sdsuLogo.jpeg
│   │   │   ├── test.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── db.sqlite3
│   │   └── manage.py
│   ├── build
│   │   ├── bdist.macosx-10.9-x86_64
│   │   └── lib
│   │       └── application
│   │           ├── __init__.py
│   │           └── manage.py
│   ├── canvasCrosslister.egg-info
│   │   ├── PKG-INFO
│   │   ├── SOURCES.txt
│   │   ├── dependency_links.txt
│   │   ├── requires.txt
│   │   └── top_level.txt
│   ├── dist
│   │   ├── Canvas\ Crosslister-0.1.tar.gz
│   │   ├── Canvas_Crosslister-0.1-py3-none-any.whl
│   │   ├── canvasCrosslister-0.1-py3-none-any.whl
│   │   └── canvasCrosslister-0.1.tar.gz
│   ├── setup.py
│   └── venv

</pre>

For bugs, feedbacks or suggestions you can contact the following email:

<strong>myeahia@sdsu.edu</strong>



