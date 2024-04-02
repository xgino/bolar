
from django.db import models
from django.db.models import Sum, Q




CATEGORY_CHOICES = [
    ('Inkoop', 'Inkoop'),
    ('Operationele Kosten', 'Operationele Kosten'),
    ('Marketing en Reclame', 'Marketing en Reclame'),
    ('Verkoop en Distributie', 'Verkoop en Distributie'),
    ('Training / advies', 'Training / advies'),
    ('Afschrijvingen/ Leningen', 'Afschrijvingen/ Leningen'),
    ('Algemene kosten', 'Algemene kosten'),
]

class Cost(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    month = models.DateField()
    price = models.FloatField()
    recurring = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cost'
        verbose_name_plural = 'Costs'

    def __str__(self):
        return f"{self.name} - {self.month.strftime('%B %Y')}"

    @classmethod
    def get_yearly_report(cls, year):
        return get_yearly_report(cls.objects, year)

    @classmethod
    def get_quarterly_report(cls, year, quarter):
        return get_quarterly_report(cls.objects, year, quarter)
    

    @classmethod
    def get_category_report(cls, category):
        category_data = cls.objects.filter(category=category).values('month').annotate(total_price=Sum('price')).order_by('month')
        category_report = {}

        for data in category_data:
            month_name = data['month'].strftime('%B %Y')
            category_report[month_name] = data['total_price']

        return category_report



















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
        yearly_data = cls.objects.filter(month__year=year).values('month').annotate(total_revenue=Sum('revenue')).order_by('month')
        yearly_report = {}
        total_year_revenue = 0

        for data in yearly_data:
            month_name = data['month'].strftime('%B')
            yearly_report[month_name] = data['total_revenue']
            total_year_revenue += data['total_revenue']

        yearly_report['Total Year'] = total_year_revenue

        return yearly_report

    @classmethod
    def get_quarterly_report(cls, year, quarter):
        quarters = {
            'Q1': ['January', 'February', 'March'],
            'Q2': ['April', 'May', 'June'],
            'Q3': ['July', 'August', 'September'],
            'Q4': ['October', 'November', 'December']
        }

        quarter_months = quarters.get(quarter)
        if not quarter_months:
            return {}

        quarter_data = cls.objects.filter(month__year=year, month__month__in=range(1, 13)).values('month').annotate(total_revenue=Sum('revenue')).order_by('month')
        quarterly_report = {}
        total_quarter_revenue = 0

        for data in quarter_data:
            month_name = data['month'].strftime('%B')
            if month_name in quarter_months:
                quarterly_report[month_name] = data['total_revenue']
                total_quarter_revenue += data['total_revenue']

        quarterly_report[f'Total {quarter}'] = total_quarter_revenue

        return quarterly_report