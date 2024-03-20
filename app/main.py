from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import pickle


with open('app/pipeline.pkl', 'rb') as f:
    pipe = pickle.load(f)

classes = ['Arrival', 'Departure', 'Empty Container Released', 
           'Empty Return', 'Gate In', 'Gate Out', 'In-transit', 
           'Inbound Terminal', 'Loaded on Vessel', 'Off Rail', 
           'On Rail', 'Outbound Terminal', 'Port In', 'Port Out', 
           'Unloaded on Vessel']


app = FastAPI()

@app.get("/")
async def home():
    return {"Hello": "World"}


@app.post('/predict')
async def predict(request: Request):
    data = await request.json()
    external_status = data['externalStatus']
    pred = pipe.predict([external_status])
    return JSONResponse({'internalStatus': classes[pred[0]]})