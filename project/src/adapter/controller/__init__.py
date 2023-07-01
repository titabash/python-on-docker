from fastapi import FastAPI
from adapter.controller import hello_controller


def create_app():
    app = FastAPI()
    app.include_router(hello_controller.router)
    return app


def excute_batch():
    result = hello_controller.main_api_controller()
    return result
