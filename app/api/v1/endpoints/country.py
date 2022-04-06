from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import app.services.country as service
from app.api.deps import get_db_pg
from app.models.country import Country
from app.schemas.country import CountryIn, CountryOut

router = APIRouter()


@router.post(
    "/",
    response_model=CountryOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создает страну",
)
def create_country(
    country: CountryIn,
    db: Session = Depends(get_db_pg),
) -> CountryOut:
    """
    # Ответ:
    | Параметр | Тип | Описание |
    |----------|-----|----------|
    | id | int | id страны. |
    | name | str | Название страны. |
    ```
    {
        "id": 1,
        "name": "Russia"
    }
    ```
    """
    return service.create_country(
        db=db,
        country=country,
    )


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[CountryOut],
    summary="Возвращает все страны",
)
async def get_all_countries(
    db: Session = Depends(get_db_pg),
) -> List[Country]:
    """
    # Ответ:
    | Параметр | Тип | Описание |
    |----------|-----|----------|
    | id | int | id страны. |
    | name | str | Название страны. |
    ```
    [
      {
        "id": 1,
        "name": "USA"
      },
      {
        "id": 2,
        "name": "Russia"
      }
    ]
    ```
    """

    return service.get_all_countries(db=db)
