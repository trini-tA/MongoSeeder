import pymongo
from faker import Faker

fake = Faker()
sensorsNumber = 100000
batchInfo = 500
counter = 0

db = pymongo.MongoClient("mongodb://localhost").bulk_example

sensors = []
print('Start bulk insert')
for i in range(sensorsNumber):

    if counter >= batchInfo :
        ids = db.sensors.insert_many(sensors)
        ids_sensors = ids.inserted_ids
        measures = []
        for id in ids_sensors:
            for y in range(batchInfo):
                measures.append({
                    'name': fake.name(),
                    'sensor': id,
                    'type': 1,
                    'timestamp': fake.unix_time(),
                    'data': [
                        {
                            'temperature': fake.pyfloat()
                        },
                        {
                            'temperature': fake.pyfloat()
                        },
                        {
                            'temperature': fake.pyfloat()
                        }
                    ],
                })
        db.measures.insert_many(measures)

        sensors = []
        print( 'sensors inserted', batchInfo )
        print( 'measures inserted', len(measures))
        counter = 0

    counter = counter + 1

    sensors.append({
        'name': fake.name(),
        'enable': fake.pybool(),
        'locate': fake.city(),
        'creator': fake.name(),
        'type': fake.name(),
        'unit': fake.name(),
        'store': fake.name(),
        'measures': []
    })

db.sensors.insert_many(sensors)
print('End bulk insert')

