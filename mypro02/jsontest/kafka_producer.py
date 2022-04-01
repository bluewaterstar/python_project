# encoding: utf-8
"""
@version: 1.0
@author: Atlantis
@file: kafka_producer
@time: 2022/3/4 10:05
"""
import json
from fileinput import filename

from kafka import KafkaProducer
# producer =KafkaProducer(bootstrap_servers='10.162.201.1:6667,10.162.201.2:6667')

# with open(r"E:\data\trq20220303.json","rb") as f:
#     data = json.load(f)
#     # producer.send(topic, data.encode('utf-8'))


def main():
    producer =KafkaProducer(bootstrap_servers='10.162.201.1:6667,10.162.201.2:6667')
    with open('E:/data/trq20220303.json', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            # print(line.replace('\n',''))
            # 创建主题，发送信息，必须为bytes类型和.encode
            producer.send("dull", bytes(line.replace('\n', '').encode()))  # 主题会自动帮你创建
            # 等待所有有待处理的消息
            producer.flush()


if __name__ == '__main__':
    main()