from fastapi import APIRouter
from usecase.hello_usecase import HelloUsecase
from utilities.logger.logging import logger
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


router = APIRouter()


@router.get('/')
def main_api_controller():
    try:
        helloUsecase = HelloUsecase()
        res = helloUsecase.hello()
        json_compatible_item_data = jsonable_encoder(res)
        print(json_compatible_item_data)
    except Exception as e:
        print(e)
        return e
    return JSONResponse(content=json_compatible_item_data)


def main_batch_controller():
    try:
        helloUsecase = HelloUsecase()
        res = helloUsecase.hello()
        print(res)
    except Exception as e:
        logger.error(e)
        return e
    return res
