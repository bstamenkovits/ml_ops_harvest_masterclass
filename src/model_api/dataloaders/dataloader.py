from typing import Any, Optional

from pydantic import PrivateAttr
import pandas as pd

from model_api.base_classes import DataLoaderBase
from model_api.api_classes import UserResponseModel


class DataLoader(DataLoaderBase):
    data_path: Optional[str] = ""
    _data_frame: pd.DataFrame = PrivateAttr()

    def __init__(self, **data):
        super().__init__(**data)
        self._data_frame = pd.DataFrame({"user_id": [1, 2, 3],
                                         "name": ["Bas", "Niels", "Sjors"]})

    def get_data(self) -> pd.DataFrame:
        return self._data_frame

    def post_data(self, new_data: UserResponseModel):
        self._data_frame = self._data_frame.append(pd.DataFrame(new_data.dict(), index=[0]))

    def set_data(self, key: int, col: str, value: Any):
        self._data_frame.loc[self._data_frame["user_id"] == key, col] = value

    def query_data(self, **kwargs) -> pd.DataFrame:
        return self._data_frame.query(
            " and ".join(k + "==" + ("'" + v + "'" if type(v) == str else str(v)) for k, v in kwargs.items()))

    def delete_data(self, key):
        self._data_frame = self._data_frame.loc[self._data_frame["user_id"] != key]
        print(self._data_frame)

    class Config:
        arbitrary_types_allowed = True
