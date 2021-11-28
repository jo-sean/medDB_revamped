Making Required Changes
First you should go to the medDB_revamped repository folder and setup a new Python virtual environment for Flask, 
then install related dependencies. Run the commands within previous directory:

cd medDB_revamped
bash
virtualenv venv -p $(which python3) 
source ./venv/bin/activate
pip3 install --upgrade pip
pip install -r requirements.txt

Next run the sql queries in your database to add the necessary tables and sample data.

Create a .env in the root directory. Inside include the following. Make sure you are using your own information to 
connect your database.

340DBHOST='classmysql.engr.oregonstate.edu'
340DBUSER='cs340_{ONID_USERNAME}'
340DBPW='{DB_PASS}'
340DB='cs340_{ONID_USERNAME}'

You can then edit the PORT inside the app.py to whatever you wish and run app.py.

Notes:
- use command 'pip install mysqlclient' for MacOS (https://stackoverflow.com/questions/454854/no-module-named-mysqldb)

Backlog:
1. Add update functionality to all pages (completed: medications, techs)
    - Not all fields should be allowed to be edited (e.g. medication name) - does the project requirements 
    want us to enable updating for everything
2. Add search functionality for medications page
3. Dropdown menus for FKs to allow for updating and inserting into tables
4. Clean up schema diagram
5. Use bootstrap or other CSS framework to clean up UI
6. Deploy on heroku and clearDB for portfolio
