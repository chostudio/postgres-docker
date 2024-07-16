from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL
DATABASE_URL = "postgresql+psycopg2://postgres:mysecretpassword@localhost/postgres"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a base class for the models. Took it from online, not really sure what it does
Base = declarative_base()

# Define the models
class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    naics_code = Column(String(255), nullable=True)
    product_category = Column(String(255), nullable=True)

    def __init__(self, id, name, address, naics_code, product_category):
        self.id = id
        self.name = name
        self.address = address
        self.naics_code = naics_code
        self.product_category = product_category

class Process(Base):
    __tablename__ = 'process'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'), nullable=False)
    raw_material_used = Column(String(255), nullable=False)

    def __init__(self, id, name, manufacturer_id, raw_material_used):
        self.id = id
        self.name = name
        self.manufacturer_id = manufacturer_id
        self.raw_material_used = raw_material_used

class Machine(Base):
    __tablename__ = 'machine'
    id = Column(Integer, primary_key=True)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'), nullable=True)
    process_id = Column(Integer, ForeignKey('process.id'), nullable=True)
    make_and_model = Column(String(255), nullable=False)
    max_width = Column(Integer, nullable=True)
    max_length = Column(Integer, nullable=True)
    max_height = Column(Integer, nullable=True)
    utilization_rate = Column(Float, nullable=False)
    operating_cost_per_hour = Column(Float, nullable=False)
    days_operational = Column(Integer, nullable=False)
    shifts_per_day = Column(Integer, nullable=False)
    hours_per_shift = Column(Integer, nullable=False)
    hours_available_per_week = Column(Integer, nullable=True)

    def __init__(self, id, manufacturer_id, process_id, make_and_model, max_width, max_length, max_height, utilization_rate, operating_cost_per_hour, days_operational, shifts_per_day, hours_per_shift, hours_available_per_week):
        self.id = id
        self.manufacturer_id = manufacturer_id
        self.process_id = process_id
        self.make_and_model = make_and_model
        self.max_width = max_width
        self.max_length = max_length
        self.max_height = max_height
        self.utilization_rate = utilization_rate
        self.operating_cost_per_hour = operating_cost_per_hour
        self.days_operational = days_operational
        self.shifts_per_day = shifts_per_day
        self.hours_per_shift = hours_per_shift
        self.hours_available_per_week = hours_available_per_week

class RawMaterials(Base):
    __tablename__ = 'raw_materials'
    id = Column(Integer, primary_key=True)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'), nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    density = Column(Float, nullable=False)

    def __init__(self, id, manufacturer_id, name, price, density):
        self.id = id
        self.manufacturer_id = manufacturer_id
        self.name = name
        self.price = price
        self.density = density

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a new session
session = Session()

# Insert data
manufacturer = Manufacturer(id=1, name="Manufacturer 1", address="1234 Elm St", naics_code="123456", product_category="Electronics")
process = Process(id=1, name="Process 1", manufacturer_id=1, raw_material_used="Steel")
machine = Machine(id=1, manufacturer_id=1, process_id=1, make_and_model="Model 1", max_width=100, max_length=200, max_height=300, utilization_rate=0.85, operating_cost_per_hour=50.0, days_operational=5, shifts_per_day=2, hours_per_shift=8, hours_available_per_week=40)
raw_material = RawMaterials(id=1, manufacturer_id=1, name="Steel", price=100.0, density=7.85)

session.add(manufacturer)
session.add(process)
session.add(machine)
session.add(raw_material)

session.commit()

# Retrieve data
manufacturers = session.query(Manufacturer).all()
for manufacturer in manufacturers:
    print(manufacturer.id, manufacturer.name, manufacturer.address, manufacturer.naics_code, manufacturer.product_category)

processes = session.query(Process).all()
for process in processes:
    print(process.id, process.name, process.manufacturer_id, process.raw_material_used)

machines = session.query(Machine).all()
for machine in machines:
    print(machine.id, machine.manufacturer_id, machine.process_id, machine.make_and_model, machine.max_width, machine.max_length, machine.max_height, machine.utilization_rate, machine.operating_cost_per_hour, machine.days_operational, machine.shifts_per_day, machine.hours_per_shift, machine.hours_available_per_week)

raw_materials = session.query(RawMaterials).all()
for raw_material in raw_materials:
    print(raw_material.id, raw_material.manufacturer_id, raw_material.name, raw_material.price, raw_material.density)
