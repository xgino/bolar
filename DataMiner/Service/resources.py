from import_export import resources
from .models import Service, ServiceCategory

class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service

class ServiceCategoryResource(resources.ModelResource):
    class Meta:
        model = ServiceCategory