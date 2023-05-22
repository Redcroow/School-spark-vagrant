from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='192.168.33.13:9092',
)

for i in range(5):
    message = 'Message {}'.format(i)
    producer.send('kafaktopic', value=message)

producer.flush()

producer.close()
