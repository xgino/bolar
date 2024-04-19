from datetime import date
from .models import Visitor

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get visitor IP address
        ip_address = request.META.get('REMOTE_ADDR')
        
        # Get today's date
        today = date.today()

        # Check if a visitor with the same IP address has visited today
        existing_visitor = Visitor.objects.filter(ip_address=ip_address, timestamp__date=today).exists()

        # If the visitor is not found for today, create a new Visitor object
        if not existing_visitor:
            Visitor.objects.create(ip_address=ip_address)

        # Pass the request to the next middleware or view
        response = self.get_response(request)

        return response