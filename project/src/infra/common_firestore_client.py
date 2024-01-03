import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore_async


class CommonFirestoreClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CommonFirestoreClient, cls).__new__(cls)
            cred = credentials.Certificate("/credentials/firebase/serviceAccount.json")
            firebase_admin.initialize_app(cred)
            cls._instance.client = firestore_async.client()
        return cls._instance

    def client(self):
        return self._instance.client
