import uvicorn
from adapter.controller import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app)
