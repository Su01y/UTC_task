from fastapi import FastAPI

from app.service import schedule_messages

app = FastAPI()


@app.post("/schedule")
async def schedule():
    schedule_messages()
    return {"message": "Mailing is planned!"}
