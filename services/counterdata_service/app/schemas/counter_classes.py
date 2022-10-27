import datetime
from pydantic import BaseModel, Field
##from typing import Optional

'''class BaseCounter(BaseModel):
    serial_number: int = Field(title='Серийный номер счётчика')'''

class Counter(BaseModel):
    serial_number: int = Field(title='Серийный номер счётчика')
    name: str = Field(title='Название устройства')
    type_c: str = Field(title='Тип счётчика')
    date_r: datetime.date = Field(title='Дата регистрации счётчика')
    date_check: datetime.date = Field(title='Дата снятия показаний счётчика')

class Counter_Indication(BaseModel):
    id_i: int = Field(title='id показания счётчика')
    id_c: int = Field(title='id счётчика')
    value: float = Field(title='Зафиксированное значение')
    date_check_count: datetime.date = Field(title='Дата передачи показаний')


