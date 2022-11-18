
from fastapi import FastAPI

from main import Board


app = FastAPI()

@app.get("/blink")
def start_blink():
    board = Board(17)
    board.blink()
