# MongoDB Atlas Form Submission

## Objective

Create a frontend form that inserts user data into MongoDB Atlas using Flask.

## Features

* Frontend form for user input
* Flask backend
* MongoDB Atlas integration
* Redirects to a success page after successful submission
* Displays errors on the same page if submission fails

## Project Structure

```text
mongodb-atlas-form/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
    ├── form.html
    └── success.html
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd mongodb-atlas-form
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## MongoDB Atlas Configuration

Before running the project, replace the following line in `app.py`:

```python
MONGO_URI = "YOUR_MONGODB_CONNECTION_STRING"
```

with your own MongoDB Atlas connection string:

```python
MONGO_URI = "mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority"
```

## Running the Application

```bash
python3 app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Usage

1. Enter Name and Email.
2. Click Submit.
3. Data is stored in MongoDB Atlas.
4. User is redirected to the success page displaying:

```text
Data submitted successfully
```

## Technologies Used

* Python
* Flask
* MongoDB Atlas
* PyMongo
* HTML

## Author

Pawan Kalyan

