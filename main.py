# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import JSONResponse
# import uvicorn

# app = FastAPI()

# def is_real_or_fake(file_name: str) -> str:
#     # Extract the last number in the filename (before extension)
#     name = file_name.rsplit('.', 1)[0]
#     numbers = ''.join(filter(str.isdigit, name))
#     if numbers == '':
#         return 0  # no number found
#     last_digit = int(numbers[-1])
#     return "real" if last_digit % 2 == 0 else "fake"

# @app.post("/predict/")
# async def predict(file: UploadFile = File(...)):
#     prediction = is_real_or_fake(file.filename)
#     return JSONResponse(content={
#         "filename": file.filename,
#         "prediction": prediction
#     })

# # Run this using: uvicorn filename:app --reload

from fastapi import FastAPI

app = FastAPI()

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the root route!"}

# Route to display info for items
@app.get("/items/")
def items():
    return {"message": "Welcome to the items route!"}

# Route to display info for updating items
@app.get("/items/update/")
def update_item():
    return {"message": "Welcome to the update item route!"}
