from kafka import KafkaConsumer

# Créer une instance de KafkaConsumer avec les paramètres appropriés
consumer = KafkaConsumer(
    'kafaktopic',
    bootstrap_servers='192.168.33.13:9092',
)

# Utilisez une boucle pour consommer les messages
for message in consumer:
    # Traitez le message ici
    print(message)
