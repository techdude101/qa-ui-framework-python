# UI Test Automation Framework with Pytest & Selenium

## Quickstart
### 1. Install Dependencies
Create a new virtual environment (recommended)  
`python -m venv venv`  

#### Windows venv activation
**In cmd.exe**  
`venv\Scripts\activate.bat`  
**In PowerShell**  
`venv\Scripts\Activate.ps1`  
#### Linux and MacOS venv activation
`source venv/bin/activate`  

#### Install dependencies  
`pip install -r requirements.txt`  

### 2. Run Tests
To run tests in parallel with pytest-xdist  
`pytest -n 2`  


To run tests in parallel with pytest-xdist and Selenium grid   
**Windows**  
`set GRID_URL=http://grid.example.com:4444/wd/hub`  
`pytest -n 2`  

**Linux**  
`export GRID_URL=http://grid.example.com:4444/wd/hub`  
`pytest -n 2`  

To run tests with allure reporting  
`python -m pytest --alluredir allure-results`  

`allure-2.28.0/bin/allure serve allure-results`  