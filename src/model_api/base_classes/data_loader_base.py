import abc
from typing import Any

from pydantic import BaseModel


class DataLoaderBase(BaseModel):
    data_path: str

    @abc.abstractmethod
    def get_data(self) -> Any:
        """
        Returns the raw data
        :return: Any
        """
        pass
