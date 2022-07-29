# keyUA test task
Django project

### Installing and setup

- Python3 v3.9+ must be already installed
- SQLite3 have to be installed and setup 

```shell
git clone https://github.com/Flashmobber/keyUA.git
cd keyUA
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
python manage.py migrate
python mange.py createsuperuser
SECRET_KEY="put you django secret key here" DEBUG=1(if you live it out you must set ALLOWED_HOSTS='127.0.0.1' or other) python manage.py runserver
```

### Features

- Anonymous User can only access HOME page and login or registration forms
- User can create, delete or see list of his own entries only
- To create an entry user provide this data:
  - date
  - distance
  - duration
- When user see list of entries, application also shows average speed
- Able to filter list of entries by date range
- Page with per-week statistics for last year - week number, total amount of entries, total distance, total duration and weekly average speed.
- Minimal front-end design with bootstrap. With sticky header, table and list.
- Configuration ready to be used in different environments. Secret key not be committed to git.
- User - Can only manage own entries
- Admin - Can manage users, can see all users data and create and update entries on behalf of other user.
