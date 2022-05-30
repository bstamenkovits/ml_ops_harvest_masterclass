import abc
from typing import Any

from pydantic import BaseModel


class PredictorBase(BaseModel):

    @abc.abstractmethod
    def load_model(self, path: str) -> Any:
        pass

    @abc.abstractmethod
    def predict(self, input_features: Any) -> Any:
        pass
