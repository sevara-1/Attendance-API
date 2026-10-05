from fastapi import FastAPI
app = FastAPI(title = "Attendance API")

@app.get("/")
def root():
    return {"message": "Attendance API"}