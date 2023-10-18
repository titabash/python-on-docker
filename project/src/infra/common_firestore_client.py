import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore_async


class CommonFirestoreClient:
    def __init__(
        self,
        project_id=None,
        collectionName=None,
    ):
        cred = credentials.Certificate("path/to/serviceAccount.json")
        firebase_admin.initialize_app(cred)
        self.client = firestore_async.client()
