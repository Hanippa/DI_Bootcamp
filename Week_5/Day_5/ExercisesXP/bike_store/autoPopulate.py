import os
import django
from faker import Faker
import random
import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

from rent.models import *
fake = Faker()


if __name__ == '__main__':
    # for i in range(100):
    #     new_customer = Customer(
    #                 first_name = fake.first_name(),
    #                 last_name = fake.last_name(),
    #                 email = fake.email(),
    #                 phone_number = fake.phone_number(),
    #                 address = fake.address(),
    #                 city = fake.city(),
    #                 country = fake.country())
        
    #     new_customer.save()




    # for i in range(100):
    #     new_vehicle= Vehicle(
    #         vehicle_type = random.choice(VehicleType.objects.all()),
    #         date_created = f'{random.randint(2010 , 2023)}-{random.randint(1 , 12)}-{random.randint(1 , 28)}',
    #         real_cost = random.randint(1000 , 4000),
    #         vehicle_size = random.choice(VehicleSize.objects.all())
    #     )
    #     new_vehicle.save()


    for i in range(100):

        start_date = datetime.datetime.now()
        end_date = start_date + datetime.timedelta(days=10)

        random_date = start_date + (end_date - start_date) * random.random()

        random_return_date = random_date + (end_date - random_date) * random.random()

        random_vehicle = random.choice(Vehicle.objects.all())
        random_customer = random.choice(Customer.objects.all())


        try:
            while Rental.objects.get(vehicle = random_vehicle).return_date == None:
                random_vehicle = random.choice(Vehicle.objects.all())
        except:
            pass

        new_rental = Rental(
            rental_date = random_date,
            return_date = random.choice([None , random_return_date]),
            customer = random_customer,
            vehicle = random_vehicle
        )
        new_rental.save()