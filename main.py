from fastapi.responses import FileResponse
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get('/7B2_CabangPurnama/data_csv')
def data_csv():
    df = pd.read_csv('Cars.csv')
    df.to_html('Cars.html')
    return FileResponse('cars.html')

@app.get('/7B2_CabangPurnama/data_json')
def data_json():
    df = pd.read_csv('Cars.csv')
    df.to_json('Cars.json')
    return FileResponse('cars.json')

@app.get('/7B2_CabangPurnama/data_xml')
def data_xml():
    # df = pd.read_csv('Cars.csv')
    # df.to_xml('Cars.xml')
    return FileResponse('Cars.xml')
