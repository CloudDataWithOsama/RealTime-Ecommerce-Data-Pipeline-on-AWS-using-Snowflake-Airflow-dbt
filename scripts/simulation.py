import csv
import time
from faker import Faker
import random

fake = Faker()

def generate_data():
    while True:

        # Orders Data
        order_data = [
            random.randint(1000, 9999),
            fake.name(),
            random.choice(['Laptop', 'Phone', 'Watch']),
            random.randint(50, 500)
        ]

        with open('/tmp/orders.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(order_data)

        # Customers Data
        customer_data = [
            fake.name(),
            fake.email(),
            fake.country()
        ]

        with open('/tmp/customers.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(customer_data)

        print(f"Generated: Order for {order_data[1]} and Customer {customer_data[0]}")

        time.sleep(2)

if __name__ == "__main__":
    generate_data()