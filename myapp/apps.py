from django.apps import AppConfig
import logging


class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"

    def ready(self):
        logging.debug("Request parameters: <name>:<value>")
        logging.info("User <username> logged in")
        logging.warning("Low disk space: 25 MB remaining")
        logging.error("Error connecting to database: <dbname>")
        logging.critical("Application crashed. <more_info>")
