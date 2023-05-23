from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def process_rdd(rdd):
    if not rdd.isEmpty():
        rdd = rdd.map(lambda x: x[1].split(','))
        rdd_filter = rdd.map(lambda x: (x[0], int(x[4]), int(x[5]), x[6]))
        df = spark.createDataFrame(rdd_filter, ["Date", "NbrAffected", "NbrDeaths", "Country"])
        df.show(10)

spark = SparkSession.builder \
    .master("local[2]") \
    .appName("CovidKafka") \
    .getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 10)

dks = KafkaUtils.createDirectStream(ssc, ["kafaktopic"], {"metadata.broker.list": "192.168.33.13:9092"})
dks.foreachRDD(process_rdd)

ssc.start()
ssc.awaitTermination()