import datetime

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .schemas.counter_classes import Counter_Indication, Counter
from .schemas.command import  Command, Scene
import typing


FAKE_VALUE = 344.051
app = FastAPI(
    version='0.0.1',
    title='Counters Management Service'
)

counters: typing.Dict[int, Counter] = {}
counters_m: typing.Dict[int, Counter_Indication] = {}

@app.post(
    "/counters", status_code=201, response_model=Counter,
    summary='Добавляет счётчик в базу'
)
async def add_counter(counter: Counter) -> Counter:
    result = Counter(
        **counter.dict(),
        serial_number=len(counters) + 1,
        name='Counter №' + (len(counters) + 1),
        type_c='Газ',
        date_r=datetime.date,
        date_check=datetime.date
    )
    counters[result.serial_number] = result
    return result

@app.post(
    "/counters_m", status_code=201, response_model=Counter_Indication,
    summary='Добавляет показания счётчика в базу'
)
async def add_counter_metrics(counter: Counter, counter_i: Counter_Indication):
    result = Counter_Indication(
        **counter_i.dict(),
        id_i=len(counters_m) + 1,
        id_c=counter.serial_number,
        value=FAKE_VALUE,
        date_check_count=datetime.date
    )
    counters_m[result.id_i] = result
    return result

@app.get("/counters", summary='Возвращает список счётчиков', response_model=list[Counter])
async def get_counters_list() -> typing.Iterable[Counter] :
    return [v for k, v in counters.items()]

@app.get("/counters_m", summary='Возвращает список показаний', response_model=list[Counter_Indication])
async def get_counters_indication_list() -> typing.Iterable[Counter_Indication] :
    return [v for k, v in counters_m.items()]

@app.delete("/counters/{counterId}", summary='Удаляет счетчик из базы')
async def delete_device(counterId: int) -> Counter:
    if counterId in counters:
        del counters[counterId]
        return JSONResponse(status_code=200, content={"message": "Item successfully deleted"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.delete("/counters_m/{counterInd_id}", summary='Удаляет показания из базы')
async def delete_indications(counterInd_id: int) -> Counter:
    if counterInd_id in counters_m:
        del counters_m[counterInd_id]
        return JSONResponse(status_code=200, content={"message": "Item successfully deleted"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.get("/counters/{counterId}", summary='Возвращает информацию о счетчике')
async def get_counter_info(counterId: int) -> Counter:
    if counterId in counters: return counters[counterId]
    return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.get("/counters_m/{counterId}", summary = 'Возвращает информацию о показании')
async def get_counter_indication_info(counterId: int) -> Counter_Indication:
    if counterId in counters_m: return counters_m[counterId]
    return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.put("/counters/{counterId}", summary='Обновляет информацию о счётчике в базе', response_model=Counter)
async def update_counter_info(counterId: int) -> Counter:
    if counterId in counters:
        result = Counter(
            serial_number=counterId,
            name='Counter №' + counterId,
            type_c='Электричество',
            date_r=datetime.today,
            date_check=datetime.today
        )
        counters[counterId] = result
        return JSONResponse(status_code=200, content={"message": "Item successfully updated!"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.put("/counters_m/{counterId}", summary='Обновляет информацию о показаниях счётчиков в базе', response_model=Counter_Indication)
async def update_counter_info(counterId: int, counter: Counter) -> Counter_Indication:
    if counterId in counters_m:
        result = Counter_Indication(
            id_i= counterId,
            id_c=counter.serial_number,
            value=FAKE_VALUE,
            date_check_count=datetime.today
        )
        counters_m[counterId] = result
        return JSONResponse(status_code=200, content={"message": "Item successfully updated!"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})

'''@app.get('/{coldw, hotw}') #метод передачи данных на сервер счётчика за воду(м^3), есть горячая и холодная
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
    return {"Electroenergy Counter:": heat}'''