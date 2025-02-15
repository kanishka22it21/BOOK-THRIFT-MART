# BOOK-THRIFT-MART
---
# Bookstore Application

A simple Flask application for managing user registrations and providing access to various book genres. Users can register, log in, and explore different categories of books.

## Features

- **User Registration:** Users can register with personal details.
- **User Login:** Users can log in using their registered email and password.
- **Book Genres:** Provides access to various book genres including Horror, Thriller, Romance, Fantasy, and more.
- **Responsive Pages:** Dynamic pages for each book genre.

## Technologies Used

- **Flask:** Web framework for the application.
- **Flask-MySQLdb:** For MySQL database connection.
- **HTML/CSS:** For front-end templates.
- **Docker**: Containerizes the application for easy deployment.
- **AWS S3**: For storing files.
- **Boto3**: AWS SDK to interact with AWS services like S3.

## Installation

To set up and run the application, follow these steps:

### Set Up the Environment

Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

Install the required Python libraries:

```bash
pip install Flask Flask-MySQLdb
```

### Configure MySQL Database

Ensure you have a MySQL database named `form` and a table named `info` with the following schema:

```sql
CREATE TABLE info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sname VARCHAR(100),
    age INT,
    dob DATE,
    phone VARCHAR(15),
    mail VARCHAR(100) UNIQUE,
    Gender VARCHAR(10),
    fpass VARCHAR(100),
    lpass VARCHAR(100),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50)
);
```

### Update Database Credentials
Create a .env file to securely store your sensitive data (e.g., database credentials, AWS credentials). 
Ensure to replace placeholders with actual values::

```python
MYSQL_HOST=your-rds-endpoint
MYSQL_USER=your-db-username
MYSQL_PASSWORD=your-db-password
MYSQL_DB=your-db-name

AWS_ACCESS_KEY_ID=your-aws-access-key-id
AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key
S3_BUCKET=your-s3-bucket-name
S3_REGION=your-s3-region

FLASK_SECRET_KEY=your-flask-secret-key

```
Make sure to update your main.py to load these credentials using the dotenv library:
```python
from dotenv import load_dotenv
import os
load_dotenv()

app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")



```
### Dockerize the Application
If you wish to containerize the application, Docker configuration files are available.

### AWS CI/CD Integration
For continuous deployment using AWS CodePipeline, a buildspec.yml file is available for automating the build and deployment process.

### Run the Flask Application

Start the Flask application:

```bash
python main.py
```

The application will be available at `http://127.0.0.1:5000/`. Open this URL in your web browser to access the application.

## File Structure

- `main.py`: The main Flask application file.
- `Dockerfile` : Docker configuration to containerize the app 
- `docker-compose.yml`: Docker Compose file for local testing 
- `buildspec.yml`: AWS CodePipeline build specifications 
- `.env` : Environment variables for MySQL and AWS credentials
- `templates/`: Contains HTML templates for the web pages.
  - `first.html`: The homepage template.
  - `signup.html`: The registration page template.
  - `login.html`: The login page template.
  - `recommendation.html`: The page shown after successful login.
  - Various genre templates (e.g., `horror.html`, `thriller.html`, etc.).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
