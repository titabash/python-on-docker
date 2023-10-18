import dataset
import os

# from utilities.logger.logging import logger


class CommonSQLClient:
    def __init__(
        self, dbName, tblName, user=None, pwd=None, dbType="postgresql", port=5432
    ):
        user = user if user is not None else os.environ["SQL_USER"]
        pwd = pwd if pwd is not None else os.environ["SQL_PASS"]
        self.db = dataset.connect(
            f"{dbType}://{user}:{pwd}@{os.environ['SQL_ENDPOINT']}:{port}/{dbName}"
        )
        self.table = self.db[tblName]  # DB名を設定
