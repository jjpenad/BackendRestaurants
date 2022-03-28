# BackendRestaurants

This project consist of a simple REST service build with python framework FLASK that includes singup and login endpoint to create an user and then login which will return a JWT token.
With help of this token, you will be able to interact with different endpoint that allow you to create Restaurants into the database.

## Cloud Service

## Models

This application consists of two simple models of data and its attributes:

### User

- **Email:** String. Required for signing up.
  > **Note:** Only email that follow this regular expression are valid:
  > **[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}**
- **Password:** String. Required for signing up.
  > **Note:** Passwords must be at least **10 characters**, contain **one lowercase letter**, **one uppercase letter** and have at least one of: **"!", "@", "#", "?", "]"**.

## Restaurant

- **Name:** String. Is Unique
- **Description:** String.
- **Visibility:** String. Either **private** or **public**
- **Address:** String.
- **City:** String.
- **Score:** Integer.
- **CreatedBy:** UserId. Reference to the user that created it.

## LocalSetup

Once you clone this repo, you need to do the following to make it work:

### 1. Virtual Environment

We recommend creating a virtual environment to manage your dependencies in a better way. In the root folder of the project execute:

If you don't have virtualenv:

```
pip install virtualenv
```

Create venv:

```
virtualenv venv
```

Activate it:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

### 2. Project settings

After setting up your environment, in the root directory(The same you used for env configuration), create a filled called **.ini** with the following content

```
[TEST]
DB_URI = mongodb+srv://<username>:<password>@cluster0.fqi5f.mongodb.net/<database>?retryWrites=true&w=majority
SECRET_KEY=<your_secret_key>
```

Here, replace **\<username\>** and **\<password\>** tags with the information of your mongo connection string. Also change **\<database\>** with the name of you database and finally set a secret key in **\<your_secret_key\>** for encryption of the tokens.

### 3. Execution:

In the root directory, in the terminal execute:

```
python run.py
```

Make sure your localhost and port 5000 are free, otherwise the app will not execute.
Open your browser on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
