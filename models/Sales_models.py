
from django.db import models
from django.db.models import Sum, Q



class MonthlySales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    month = models.DateField()
    units_sold = models.IntegerField()
    revenue = models.FloatField()
    tax = models.FloatField()
    commission = models.FloatField()
    acos = models.FloatField()
    gross_margin = models.FloatField()
    import_compare = models.FloatField()
    profit = models.FloatField()
    avg_sell_price_unit = models.FloatField()

    class Meta:
        verbose_name = 'Monthly Sales'
        verbose_name_plural = 'Monthly Sales'

    def __str__(self):
        return f"{self.product} - {self.month.strftime('%B %Y')}"

    def save(self, *args, **kwargs):
        if self.pk:  # Check if instance already exists (updating)
            existing_months = MonthlySales.objects.filter(product=self.product).values_list('month', flat=True)
            if self.month in existing_months:
                raise ValidationError("This month's data already exists.")
        # Calculate additional fields
        self.calculate_additional_fields()
        super().save(*args, **kwargs)

    def calculate_additional_fields(self):
        # Calculate Tax
        self.tax = self.revenue * 0.21

        # Calculate Commission
        self.commission = (self.revenue - self.tax) * 0.144

        # Calculate ACOS (Assuming it's already defined)
        # self.acos = ?

        # Calculate Gross Margin
        self.gross_margin = self.revenue - self.tax - self.commission - self.acos

        # Calculate Import Compare
        # Assuming Product has a field import_unit
        self.import_compare = self.product.import_unit * self.units_sold

        # Calculate Profit
        self.profit = self.gross_margin - self.import_compare

        # Calculate Average Sell Price Unit
        if self.units_sold != 0:
            self.avg_sell_price_unit = self.revenue / self.units_sold
        else:
            self.avg_sell_price_unit = 0.0

    @classmethod
    def get_yearly_report(cls, year):
        return get_yearly_report(cls.objects, year)

    @classmethod
    def get_quarterly_report(cls, year, quarter):
        return get_quarterly_report(cls.objects, year, quarter)