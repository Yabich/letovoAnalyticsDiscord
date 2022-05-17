import firebase_admin
import yaml
from firebase_admin import credentials, auth
from google.cloud.firestore_v1 import DocumentSnapshot


class Database:
    def __init__(self):
        app = firebase_admin.initialize_app(
            credential=credentials.Certificate("Firebase.json")
        )

        self.client = auth.Client(app)

    def update_data(
            self,
            sender_id,
            student_id=None,
            mail_address=None,
            mail_password=None,
            analytics_login=None,
            analytics_password=None,
            token=None,
            lang=None
    ):
        space = ""
        st = f'"student_id": {student_id!r},'
        ma = f'"mail_address": {mail_address!r},'
        mp = f'"mail_password": {mail_password!r},'
        al = f'"analytics_login": {analytics_login!r},'
        ap = f'"analytics_password": {analytics_password!r},'
        t = f'"token": {token!r},'
        ll = f'"lang": {lang!r},'

        request_payload = (
            '''
        {
            "data": {'''
            f'{st if student_id else space}'
            f'{ma if mail_address else space}'
            f'{mp if mail_password else space}'
            f'{al if analytics_login else space}'
            f'{ap if analytics_password else space}'
            f'{t if token else space}'
            '".service": "data"'
            '''},
                "preferences": {'''
            f'{ll if lang else space}'
            '".service": "preferences"'
            '''}
        }'''
        )
        doc_ref = self.client.collection("users").document(sender_id)
        doc_ref.set(yaml.full_load(request_payload), merge=True)

    async def update_name(
            self,
            sender_id,
            first_name=None,
            last_name=None,
    ):
        space = ""
        fn = "first_name:" + str(first_name)
        la = "last_name" + str(first_name)

        payload = (
            '''
        {
            "data": {'''
            f'{fn if first_name else space}'
            f'{la if last_name else space}'
            '".service": "data"'
            '''}
        }'''
        )
        doc_ref = self.client.collection("names").document(sender_id)
        await doc_ref.set(yaml.full_load(payload), merge=True)

    def is_logged(self, sender_id):
        doc: DocumentSnapshot = self.client.collection("users").document(sender_id).get()
        try:
            return bool(doc.get("data.analytics_password"))
        except KeyError:
            return False

    def get_student_id(self, sender_id):

        doc: DocumentSnapshot = self.client.collection("users").document(sender_id).get()
        try:
            if not doc.exists:
                return doc.get("data.student_id")
            return None
        except KeyError:
            return None

    def get_token(self, sender_id):
        doc: DocumentSnapshot = await self.client.collection("users").document(sender_id).get()
        try:
            if doc.exists:
                return doc.get("data.token")
            return None
        except KeyError:
            return None

    async def get_name(self, sender_id):
        doc: DocumentSnapshot = await self.client.collection("names").document(sender_id).get()
        try:
            if doc.exists:
                return doc.get("data.first_name")
            return None
        except KeyError:
            return None
