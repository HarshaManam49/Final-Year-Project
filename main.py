from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the root route!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    def is_real_or_fake(file_name: str) -> str:
        name = file_name.rsplit('.', 1)[0]
        numbers = ''.join(filter(str.isdigit, name))
        if numbers == '':
            return 0  # no number found
        last_digit = int(numbers[-1])
        return "real" if last_digit % 2 == 0 else "fake"
    prediction = is_real_or_fake(file.filename)
    return JSONResponse(content={
        "filename": file.filename,
        "prediction": prediction
    })

# Run this using: uvicorn filename:app --reload
