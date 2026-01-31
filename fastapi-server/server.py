import logging
from fastapi import FastAPI, File, UploadFile, HTTPException
from model_helper import predict

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.post("/predict")
async def get_prediction(file: UploadFile = File(...)):
    try:
        logging.info(f"Received file: {file.filename}")

        image_bytes = await file.read()
        image_path = "temp_file.jpg"
        with open(image_path, "wb") as f:
            f.write(image_bytes)

        logging.info(f"Saved image to {image_path}")

        prediction = predict(image_path)
        logging.info(f"Prediction: {prediction}")

        return {"prediction": prediction}

    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
