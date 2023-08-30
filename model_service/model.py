import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer

class Item(BaseModel):
    text: str

app = FastAPI()
path_to_model = os.getenv("PATH_TO_MODEL", "/model/output")
tokenizer = AutoTokenizer.from_pretrained(path_to_model)
model = AutoModelForCausalLM.from_pretrained(path_to_model)

@app.post("/predict/")
async def predict(item: Item):
    try:
        input_ids = tokenizer.encode(item.text, return_tensors='pt')
        output = model.generate(input_ids)
        output_text = tokenizer.decode(output[0], skip_special_tokens=True)
        return JSONResponse(content={"response": output_text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
