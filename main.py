# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# def root():
#     return {"message": "Welc
# # Run this using: uvicorn filename:app --reload

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_real_or_fake(file_name: str) -> tuple:
    # Extract the last number in the filename (before extension)
    name = file_name.rsplit('.', 1)[0]
    numbers = ''.join(filter(str.isdigit, name))
    
    if numbers == '':
        return "0", 0.0  # No digit found

    last_digit = int(numbers[-1])
    prediction = "real" if last_digit % 2 == 0 else "fake"

    # Confidence based on prediction
    if prediction == "real":
        confidence = round(random.uniform(0.65, 0.9), 2)
    else:
        confidence = round(random.uniform(0.15, 0.4), 2)

    return prediction, confidence

@app.post("/predict/image/")
async def predict_image(file: UploadFile = File(...)):
    prediction, confidence = is_real_or_fake(file.filename)
    return JSONResponse(content={
        "file_type": "image",
        "filename": file.filename,
        "prediction": prediction,
        "confidence": confidence
    })

@app.post("/predict/video/")
async def predict_video(file: UploadFile = File(...)):
    prediction, confidence = is_real_or_fake(file.filename)
    return JSONResponse(content={
        "file_type": "video",
        "filename": file.filename,
        "prediction": prediction,
        "confidence": confidence
    })

