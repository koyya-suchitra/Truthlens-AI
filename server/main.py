from fastapi import FastAPI, UploadFile, File
import pdfplumber

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TruthLens AI backend running"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    with pdfplumber.open(file.file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""

    return {"extracted_text": text[:500]}