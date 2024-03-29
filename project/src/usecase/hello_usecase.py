import sys
import os
from adapter.gateway.hello_gateway import HelloGateway

from domain.hello import Hello


class HelloUsecase:
    def __init__(self):
        self.hello_repository = HelloGateway()
        pass

    def hello(self, event="test") -> Hello:
        hello = Hello(
            environment=os.environ["MACHINE_ENV"], py_version=sys.version, event=event
        )
        return hello

    def find_all(self):
        data = self.hello_repository.find()
        return data
