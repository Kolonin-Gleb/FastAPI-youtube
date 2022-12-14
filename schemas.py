# Файл с pydantic моделями для валидации данных, отправляемых на сервер
from typing import List # Для аннотирования типов данных. Как строгая типизация

from pydantic import BaseModel, validator, Field
from datetime import date

class Genre(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description="Возраст должен быть > 15 и < 90") # Валидация через Field

    # Валидатор для поля pydantic модели
    # Позволяет гарантировать создание авторов определённого возраста
    '''
    @validator('age')
    def check_age(cls, v):
        if v <= 18:
            raise ValueError("Автор должен быть старше 18")
        return v
    '''
class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = [] # Список из жанров, что разрешены моделью Genre.
    pages: int

# Модель, используемая для ответа от сервера
class BookOut(Book):
    id: int


