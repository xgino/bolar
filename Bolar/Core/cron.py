import logging
from pages.models import Books
from django.utils import timezone

logger = logging.getLogger(__name__)

def my_scheduled_garbage():
    try:
        title = "Some Book " + str(timezone.now())
        new_book = Books.objects.create(title=title)
        logger.info("Successfully created a new book: %s", new_book)
    except Exception as e:
        logger.error("An error occurred while creating a new book: %s", e)