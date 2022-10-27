import datetime

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from services.counterdata-service.app.schemas.counter_classes import Counter_Indication, Counter
from .schemas.command import Command, Scene
import typing

app = FastAPI()

counters: typing.Dict[int, Counter] = {}
counters_m: typing.Dict[int, Counter_Indication] = {}
FAKE_VALUE = 344.051

@app.post(
    "/counters", status_code=201, response_model=Counter,
    summary='Добавляет счётчик в базу'
)
async def add_counter(counter: Counter):
    result = Counter(
        **counter.dict(),
        serial_number=len(counters) + 1,
        name='Counter №' + Counter.serial_number,
        type_c='Газ',
        date_r=datetime.date,
        date_check=datetime.date
    )
    counters[result.serial_number] = result
    return result

@app.get("/counters", summary='Возвращает список счётчиков', response_model=list[Counter])
async def get_counters_list() -> typing.Iterable[Counter] :
    return [v for k, v in counters.items() ]

@app.delete("/counters/{counterId}", summary='Удаляет счетчик из базы')
async def delete_device(counterId: int) -> Counter:
    if counterId in counters:
        del counters[counterId]
        return JSONResponse(status_code=200, content={"message": "Item successfully deleted"})
    return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.get("/counters/{counterId}", summary='Возвращает информацию о счетчике')
async  def get_counter_info(counterId: int) -> Counter:
    if counterId in counters: return counters[counterId]
    return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.post(
    "/counters_m", status_code=201, response_model=Counter_Indication,
    summary='Добавляет показания счётчика в базу'
)
async def add_counter_metrics(counter: Counter_Indication):
    result = Counter_Indication(
        **counter.dict(),
        id_i=counter.id_i,
        id_c=counter.id_c,
        value=FAKE_VALUE,
        date_check_count=datetime
    )
    counters_m[result.id_i] = result
    return result

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