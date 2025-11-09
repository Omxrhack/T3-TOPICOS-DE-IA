from __future__ import annotations
from typing import Protocol
import numpy as np

class FitnessFunction(Protocol):
    def __call__(self, x: np.ndarray) -> float: ...

def maximize_f_x_sin_x(x: np.ndarray) -> float:
    return float(np.sum(x * np.sin(x)))
