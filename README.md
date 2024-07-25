# Firebase Firestore CSV Uploader

A simple Python project to upload data from a CSV file to a Firebase Firestore database using a service account key.

## Prerequisites
Python 3.x

Firebase project with a service account key

pip for package installation

## Installation

### Clone the repository:

git clone [https://github.com/your-username/firebase-firestore-csv-uploader.git](https://github.com/DhyaanNayak/Firebase_CSV_uploader.git)

cd firebase-firestore-csv-uploader

### Install dependencies:

firebase_admin

pandas

os

## Usage
Place your service account key JSON file in the project directory and name it serviceAccountKey.json.

Place your CSV file in the project directory and name it data.csv.

Update the collection_name variable in the main() function if necessary.

### Run the script:

python uploader.py

## Configuration

The script expects the following file structure in the project directory:

firebase-firestore-csv-uploader/

├── serviceAccountKey.json

├── data.csv

├── uploader.py

├── requirements.txt

└── README.md
