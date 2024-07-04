import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Garden(BaseModel, Base):
    
    if models.storage_t == "db":
        __tablename__ = "Garden"
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        garden_name = Column(String(60))
        location = Column(String(60), nullable=False)
        sensorsNo = Column(Integer, default=0)
        plant_minitored = Column(Integer, default=0)
        description = Column(String(500))
    else:
        user_id = ""
        location = ""
        garden_name = ""
        sensorsNo = 0
        description = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)