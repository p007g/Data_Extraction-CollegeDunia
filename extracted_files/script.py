# import json
# import os
# import firebase_admin  # type: ignore
# from firebase_admin import credentials, firestore  # type: ignore
# import uuid  # for generating unique document IDs

# # Initialize Firebase app
# cred = credentials.Certificate("C:\\Users\\91766\\Downloads\\collegecue-filter-firebase-adminsdk-rw683-3ed77cd6bc.json")
# if not firebase_admin._apps:
#     firebase_admin.initialize_app(cred)

# # Initialize Firestore client
# db = firestore.client()

# def upload_json_to_firestore(json_file_path, collection_name):
#     with open(json_file_path) as f:
#         data = json.load(f)
    
#     collection_ref = db.collection(collection_name)

#     for doc_data in data:
#         doc_id = str(uuid.uuid4())  # Generate a unique document ID
#         doc_ref = collection_ref.document(doc_id)
#         doc_ref.set(doc_data)
#         print(f'Document {doc_id} added to {collection_name} collection.')

# def upload_multiple_json_files(directory_path, collection_name):
#     # Iterate over all JSON files in the specified directory
#     i = 1
#     for filename in os.listdir(directory_path):
#         if filename.endswith('.json'):
#             json_file_path = os.path.join(directory_path, filename)
#             print(f'Uploading {json_file_path} to Firestore...')
#             upload_json_to_firestore(json_file_path, collection_name)
#             print(i)
#             i += 1
#     print('All JSON files have been uploaded.')

# directory_path = 'state_wise_college_course_details_3'
# collection_name = 'data-filter'

# print(f'Total JSON files found: {len(os.listdir(directory_path))}')

# upload_multiple_json_files(directory_path, collection_name)


import json
import os

def count_docs_len(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            json_file_path = os.path.join(directory_path, filename)
            with open(json_file_path) as f:
                data = json.load(f)
                yield len(data)

total = []
for directory in ['state_wise_college_course_details', 'state_wise_college_course_details_2']:
    total.extend(count_docs_len(directory))

print(sum(total))
