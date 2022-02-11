from pydantic import BaseModel
from typing import Optional

#Post CloudEvent
class CloudEventModel(BaseModel):
    msg: Optional[str] = None