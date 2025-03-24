# Functional Login Page with SQLite and Flask  

This project provides a working login system for any website. It handles user authentication, securely stores passwords with bcrypt, and manages sessions using cookies.  

## Requirements  

Click **Code** and **Download ZIP** on GitHub
Extract the ZIP file

To run this project, you'll need Flask, bcrypt, and sqlite3. You can install them with:  

```bash
python -m pip install flask bcrypt
```
or
```bash
python3 -m pip install flask bcrypt
```

Navigate to the following URL to install SQLite3:
`https://www.sqlite.org/`

After downloading, ensure `sqldiff.exe`, `sqlite3.exe`, and `sqlite_analyzer.exe` are in the project directory.

## The Database
The project uses an SQLite3 database where user passwords are stored encrypted using bcrypt.

This database is case-sensitive.

When a password is entered on the login page (starting_page.html), it is encrypted and compared with the stored encrypted password. If they match, the program redirects the user to the homepage and stores a cookie indicating they are logged in.

## Account Creation Page
The create_account_page.html file allows users to create an account.

    - Both usernames and passwords are case-sensitive.
    
    - If the entered username already exists, an error message appears, and the database does not create a duplicate entry.

    - If the username is unique, the password is encrypted and stored in the database, and the user is redirected to the homepage.

## Cookies and Login Page

    - An error will be displayed if the user does not provide their correct credentials.

    - The login system uses cookies to manage user sessions.

    - If a user is not logged in, trying to access the homepage (http://127.0.0.1:5000/login/welcome/) redirects them to starting_page.html.

    - If a user is logged in (i.e., a cookie is stored), they can access the homepage as expected.

## Warning
There is **no password recovery option.** The database only stores usernames and encrypted passwords. Due to the nature of bcrypt hashing, passwords cannot be recovered, so be sure to remember them.

## How to Test:
To run the project, open a terminal and navigate to the project directory. Then, execute
```bash
python website.py
```

Copy and paste the output URL (`http://127.0.0.1:5000`) into your browser to load the project webpage.

Note: If the initial webpage does not load, open the terminal and press `Ctrl + C` to stop the program. Then, restart it with the same command.

## Verifying the Database
Once a user is created, a database titled **LogInformation.db** can be found in the project directory. Here are some steps to ensure it is working as intended:

Open a terminal and enter the following:
```bash
sqlite3 LogInformation.db
```

Then, check the stored users and encrypted passwords:
```bash
SELECT * FROM UserInfo;
```
