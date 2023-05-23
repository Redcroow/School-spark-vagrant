import csv
from kafka import KafkaProducer

bootstrap_servers = '192.168.33.13:9092'
topic_name = 'kafaktopic'

csv_file = 'data/data_covid.csv'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    
    for row in csv_reader:
        message = ','.join(row).encode('utf-8')

        producer.send(topic_name, value=message)
        producer.flush()

producer.close()
