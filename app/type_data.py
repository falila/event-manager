import re
from dataclasses import dataclass, field
from enum import Enum, unique
from typing import Dict, List, Optional
import json


@unique
class EventKind(str, Enum):
    PAINT = "paint"
    MARK = "mark"
    MEASURE = "measure"
    FIRST_INPUT = "first-input"
    UNKNOWN = "unknown"


@dataclass
class EventComponentTiming:
    kind: str
    start: float
    end: float

    @property
    def duration(self):
        return self.end - self.start


@dataclass(frozen=True)
class PerformanceEvent:
    uuid: str
    sample_id: str
    kind: EventKind
    name: str
    timings: Dict[str, EventComponentTiming]
    size: int
    start_time: str
    end_time: str
    raw: dict = field(repr=False)
    
    def to_json(self):
        return json.dumps(self.__dict__, default=lambda x: x.__dict__, indent=4)
