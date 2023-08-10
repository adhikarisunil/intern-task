
import pika
import json
import sys
import os
import django
# print(sys.path)

# Append the path to the project directory to the system path
project_path = "/home/lenovo/Desktop/Project/Product"
sys.path.append(project_path)

# Set the DJANGO_SETTINGS_MODULE to the correct settings file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Product.settings")
django.setup()

# Import the model
from  products.models import Favorite

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue before consuming
queue_name = 'favorite_products'
channel.queue_declare(queue=queue_name)
# print('this is the callback')

def callback(ch, method, properties, body):
    # print('this is the callback')
    data = json.loads(body)
    user_id = data['user_id']
    product = data['product_id']
    
    Favorite.objects.create(user_id=user_id, product=product)

# Start consuming messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# print('Waiting for messages...')
channel.start_consuming()
