from fastapi import FastAPI

app = FastAPI()

@app.get('/{coldw, hotw}') #метод передачи данных на сервер счётчика за воду(м^3), есть горячая и холодная
def get_water_count(coldw: float, hotw: float):
    return {"Cold Water Counter:": coldw, "Hot Water Counter:": hotw}

@app.get('/{gas}') #метод передачи данных на сервер счётчика за газ(м^3)
def get_gas_count(gas: float):
    return {"Gas Counter:": gas}

@app.get('/{electro}') #метод передачи данных на сервер счётчика за электроэнергию
def get_electro_count(electro: float):
    return {"Electroenergy Counter:": electro}

@app.get('/{heat}') #метод передачи данных на сервер счётчика за отопление
def get_heating_count(heat: float):
    return {"Electroenergy Counter:": heat}

'''@app.get('/{flat}') #метод передачи данных на сервер ежемесячной квартплаты
def get_flatpayment_count(flat: float):
    return {"FlatPay Counter:": flat}'''