from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import create_engine



class DataBase():
    Base = declarative_base()
    def __init__(self):
        super().__init__()

        self.engine = create_engine('sqlite:///rtsp_data.db')
        self.Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

class Device(DataBase.Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    rtsp_url = Column(String(200), nullable=False)
    save_path = Column(String(200), nullable=False)
    interval = Column(Integer, nullable=False, default=60)
    active = Column(Boolean, nullable=False, default=False)