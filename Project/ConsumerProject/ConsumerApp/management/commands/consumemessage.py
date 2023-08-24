from typing import Any, Optional
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import pika
from django.core.management.base import BaseCommand
from pika.exceptions import AMQPConnectionError
import time
from ...views import consume_queue
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from ninja import NinjaAPI

class Command(BaseCommand):
    help = 'Continuously consume messages from RabbitMQ'

    def handle(self, *args, **options):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
                credentials=pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
            ))
            channel = connection.channel()
            channel.queue_declare(queue="Messages")

            def callback(ch, method, properties, body):
                message = body.decode('utf-8')
                self.stdout.write(self.style.SUCCESS(f"[✓] Received message: {message}"))

            channel.basic_consume(queue="Messages", on_message_callback=callback, auto_ack=True)

            self.stdout.write(self.style.SUCCESS("[+] Waiting for messages. To exit press CTRL+C"))
            channel.start_consuming()

        except (Exception, AMQPConnectionError) as e:
            self.stdout.write(self.style.ERROR("[X] Error while consuming messages."))
            self.stderr.write(str(e))
            