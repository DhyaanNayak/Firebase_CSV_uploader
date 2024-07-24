import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import os

# Initialize Firestore DB
def initialize_firestore(cred_file):
    print(f"Checking credential file at: {cred_file}")
    if not os.path.exists(cred_file):
        raise FileNotFoundError(f"Credential file not found: {cred_file}")
    cred = credentials.Certificate(cred_file)
    firebase_admin.initialize_app(cred)
    return firestore.client()

def upload_csv_to_firestore(db, csv_file, collection_name):
    # Read CSV file into DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert DataFrame to dictionary and upload to Firestore
    for index, row in df.iterrows():
        doc_id = str(index)  # You can use a unique field or index as document ID
        data = row.to_dict()
        db.collection(collection_name).document(doc_id).set(data)
        print(f'Uploaded document {doc_id}')

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
    cred_file = os.path.join(base_dir, 'serviceAccountKey.json')  # Path to service account key
    csv_file = os.path.join(base_dir, 'PubMedtrial.csv')  # Path to CSV file
    collection_name = 'Papers'  # Replace with your Firestore collection name

    # Print paths for debugging
    print(f"Credential file path: {cred_file}")
    print(f"CSV file path: {csv_file}")

    db = initialize_firestore(cred_file)
    upload_csv_to_firestore(db, csv_file, collection_name)

if __name__ == '__main__':
    main()
