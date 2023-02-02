# Flask-simple-mqtt
 
##  use correct version of Python when creating VENV
python3 -m venv venv

##  activate on Unix or MacOS
source venv/bin/activate

##  activate on Windows (cmd.exe)
venv\Scripts\activate.bat

##  activate on Windows (PowerShell)
venv\Scripts\Activate.ps1

##  Activated environment will appear
(venv) D:\Flask-Simple-app>

<br/>

# Folder structure 

📦tests ( <sub>Folder which holds testcases</sub>) <br />
 ┣ 📂functional (<sub> Folder which holds functional test cases</sub>)<br />
 ┃ ┣ 📜__init__.py <br />
 ┃ ┗ 📜test_api.py <sub> Holds all test cases</sub><br/> 
 ┗ 📜conftest.py<sub> Fixtures are defined to help push testing context</sub><br />


 # conftest.py
 ### This file helps to define fixtures which helps to add context for testing. Hence increases reusability 

 ## Scopes can be defined in 
 <pre>
@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

 </pre>

# Run test command 
> run -m pytest

# Run coverage
> coverage run -m pytest

# Coverage report
> coverage report

# Setting up requirements

## requirement.txt
### -  Create requirements.txt file
### - Add flask as primary requirement
### - celery==5.2.7 , redis

##  install the modules in your requirements.txt file

### pip install -r requirements.txt