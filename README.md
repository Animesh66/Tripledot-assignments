
 **There are few prerequisites to run the tests locally** 
1. install python3 on your machine from https://www.python.org/downloads/
2. install node on your machine from https://nodejs.org/en/download
3. Check that npm is getting install once node is install by the command `npm --version`
4. Clone the repo using `git clone <git url>`

**Instructions to run the test locally on Mac or Windows**

1. Create a python virtual environment using `python3 -m venv env` (this needs to be executed from content root folder)
2. Active the virtual environment using shell `shell ./venv/bin/activate.bat` for Windows and `/venv/bin/activate` (this needs to be executed from content root folder)
3. Install all the dependencies using `pip3 install -r requirements.txt` (this needs to be executed from content root folder)
4. Install adb on your local system from https://www.xda-developers.com/install-adb-windows-macos-linux/
5. To verify if adb is successfully installed on your machine once connect the mobile device with your 
6. To run the test on your command line use pytest -v -s -m <marker name(eg regression, happy_path, invalid_cred)>
7. To generate allure report use below two commands one after another
8. `python -m pytest sample.py --alluredir ./Reports`
9. `allure serve ./Reports`