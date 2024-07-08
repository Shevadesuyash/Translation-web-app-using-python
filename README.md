# Translation Web Application

Welcome to the Translation Web Application project! This web application allows you to translate text between different languages using the Google Translate API. It's built with Flask and can be deployed either locally or in a Docker container.

## Features

- Translate text from one language to another.
- Automatic language detection.
- Pronunciation support for translated text (English only).

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **API:** Google Translate (via `googletrans` library)
- **Deployment:** Docker

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python:** Make sure Python 3.x is installed. [Install Python](https://www.python.org/downloads/)
- **Docker:** Install Docker to run the application in a container. [Install Docker](https://docs.docker.com/get-docker/)

## Setup and Deployment

### Option 1: Deploy Locally

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Shevadesuyash/Translation-web-app-using-python.git
   cd Translation-web-app-using-python

2. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt


3. **Run the application:**
   Start the Flask server:

   ```bash
   python app.py

The application will be accessible at http://localhost:5000.

### Option 2: Deploy with Docker

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Shevadesuyash/Translation-web-app-using-python.git
   cd Translation-web-app-using-python
2. **Build the Docker image:**
Build the Docker image from the Dockerfile:
   ```bash
   docker build -t translation-app .

3. **Run the Docker container:**
Start a Docker container from the built image:
   ```bash
   docker run -p 5000:5000 translation-app

4.**Access the application:**

Open your web browser and navigate to http://localhost:5000 to use the application.

### Usage
1. Enter the text you want to translate, select the languages, and click "Translate".
2. View the translated text and pronunciation .


### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

### Contact
Suyash Shevade - shevadesuyash30@gmail.com

Project Link: https://github.com/Shevadesuyash/Translation-web-app-using-python

