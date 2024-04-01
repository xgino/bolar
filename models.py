from django.db import models
from django.db.models import Sum, Q


class Dashboard(models.Model):
    revenue = models.FloatField()
    tax = models.FloatField()
    total_costs = models.FloatField()
    import_costs = models.FloatField()
    profit = models.FloatField()
    profit_percentage = models.FloatField()

    def __str__(self):
        return f"Dashboard - {self.pk}"

    @classmethod
    def generate_quarterly_report(cls, year, quarter):
        quarterly_report = cls.objects.filter(created_at__year=year, created_at__quarter=quarter).aggregate(
            total_revenue=Sum('revenue'),
            total_tax=Sum('tax'),
            total_total_costs=Sum('total_costs'),
            total_import_costs=Sum('import_costs'),
            total_profit=Sum('profit'),
            average_profit_percentage=Sum('profit_percentage') / Count('profit_percentage')
        )
        return quarterly_report

    @classmethod
    def generate_yearly_report(cls, year):
        yearly_report = cls.objects.filter(created_at__year=year).aggregate(
            total_revenue=Sum('revenue'),
            total_tax=Sum('tax'),
            total_total_costs=Sum('total_costs'),
            total_import_costs=Sum('import_costs'),
            total_profit=Sum('profit'),
            average_profit_percentage=Sum('profit_percentage') / Count('profit_percentage')
        )
        return yearly_report

@receiver(post_save, sender=Dashboard)
def update_reports(sender, instance, **kwargs):
    year = instance.created_at.year
    month = instance.created_at.month
    if month in [1, 2, 3]:
        quarter = 1
    elif month in [4, 5, 6]:
        quarter = 2
    elif month in [7, 8, 9]:
        quarter = 3
    else:
        quarter = 4
    # Update or save the quarterly and yearly reports accordingly

class FinanceRapport(models.Model):
    revenue_excl_vat = models.FloatField()
    vat = models.FloatField()
    cogs = models.FloatField()
    operational_costs = models.FloatField()
    marketing_advertising_expenses = models.FloatField()
    sales_distribution_costs = models.FloatField()
    training_advisory_costs = models.FloatField()
    depreciation_loans = models.FloatField()
    total_costs = models.FloatField()
    recoverable_vat = models.FloatField()
    pre_tax_result = models.FloatField()
    vat_payable = models.FloatField()
    post_tax_result = models.FloatField()
    profit_by_product = models.FloatField()

    def __str__(self):
        return f"Finance Report - {self.pk}"

    @classmethod
    def generate_quarterly_report(cls, year, quarter):
        quarterly_report = cls.objects.filter(created_at__year=year, created_at__quarter=quarter).aggregate(
            total_revenue_excl_vat=Sum('revenue_excl_vat'),
            total_vat=Sum('vat'),
            total_cogs=Sum('cogs'),
            total_operational_costs=Sum('operational_costs'),
            total_marketing_advertising_expenses=Sum('marketing_advertising_expenses'),
            total_sales_distribution_costs=Sum('sales_distribution_costs'),
            total_training_advisory_costs=Sum('training_advisory_costs'),
            total_depreciation_loans=Sum('depreciation_loans'),
            total_total_costs=Sum('total_costs'),
            total_recoverable_vat=Sum('recoverable_vat'),
            total_pre_tax_result=Sum('pre_tax_result'),
            total_vat_payable=Sum('vat_payable'),
            total_post_tax_result=Sum('post_tax_result'),
            total_profit_by_product=Sum('profit_by_product')
        )
        return quarterly_report

    @classmethod
    def generate_yearly_report(cls, year):
        yearly_report = cls.objects.filter(created_at__year=year).aggregate(
            total_revenue_excl_vat=Sum('revenue_excl_vat'),
            total_vat=Sum('vat'),
            total_cogs=Sum('cogs'),
            total_operational_costs=Sum('operational_costs'),
            total_marketing_advertising_expenses=Sum('marketing_advertising_expenses'),
            total_sales_distribution_costs=Sum('sales_distribution_costs'),
            total_training_advisory_costs=Sum('training_advisory_costs'),
            total_depreciation_loans=Sum('depreciation_loans'),
            total_total_costs=Sum('total_costs'),
            total_recoverable_vat=Sum('recoverable_vat'),
            total_pre_tax_result=Sum('pre_tax_result'),
            total_vat_payable=Sum('vat_payable'),
            total_post_tax_result=Sum('post_tax_result'),
            total_profit_by_product=Sum('profit_by_product')
        )
        return yearly_report

@receiver(post_save, sender=FinanceRapport)
def update_reports(sender, instance, **kwargs):
    year = instance.created_at.year
    month = instance.created_at.month
    if month in [1, 2, 3]:
        quarter = 1
    elif month in [4, 5, 6]:
        quarter = 2
    elif month in [7, 8, 9]:
        quarter = 3
    else:
        quarter = 4
    # Update or save the quarterly and yearly reports accordingly

class SalesRapport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    month = models.DateField()
    year = models.IntegerField()
    quarter = models.IntegerField()
    revenue = models.FloatField()
    tax = models.FloatField()
    commission = models.FloatField()
    shipping = models.FloatField()
    packaging = models.FloatField()
    retour = models.FloatField()
    total_cost = models.FloatField()
    gross_margin = models.FloatField()
    profit = models.FloatField()
    import_compare = models.FloatField()
    profit_percentage = models.FloatField()
    return_percentage = models.FloatField()
    avg_sold_unit = models.FloatField()

    def __str__(self):
        return f"{self.product} - {self.month.strftime('%B %Y')}"

    @classmethod
    def generate_quarterly_report(cls, year, quarter):
        quarterly_report = cls.objects.filter(year=year, quarter=quarter).aggregate(
            total_revenue=Sum('revenue'),
            total_tax=Sum('tax'),
            total_commission=Sum('commission'),
            total_shipping=Sum('shipping'),
            total_packaging=Sum('packaging'),
            total_retour=Sum('retour'),
            total_total_cost=Sum('total_cost'),
            total_gross_margin=Sum('gross_margin'),
            total_profit=Sum('profit'),
            avg_import_compare=Sum('import_compare') / cls.objects.filter(year=year, quarter=quarter).count(),
            total_profit_percentage=(Sum('profit') / Sum('revenue')) * 100,
            total_return_percentage=(Sum('retour') / Sum('avg_sold_unit')) * 100,
            avg_avg_sold_unit=Sum('avg_sold_unit') / cls.objects.filter(year=year, quarter=quarter).count()
        )
        return quarterly_report

    @classmethod
    def generate_yearly_report(cls, year):
        yearly_report = cls.objects.filter(year=year).aggregate(
            total_revenue=Sum('revenue'),
            total_tax=Sum('tax'),
            total_commission=Sum('commission'),
            total_shipping=Sum('shipping'),
            total_packaging=Sum('packaging'),
            total_retour=Sum('retour'),
            total_total_cost=Sum('total_cost'),
            total_gross_margin=Sum('gross_margin'),
            total_profit=Sum('profit'),
            avg_import_compare=Sum('import_compare') / cls.objects.filter(year=year).count(),
            total_profit_percentage=(Sum('profit') / Sum('revenue')) * 100,
            total_return_percentage=(Sum('retour') / Sum('avg_sold_unit')) * 100,
            avg_avg_sold_unit=Sum('avg_sold_unit') / cls.objects.filter(year=year).count()
        )
        return yearly_report

@receiver(post_save, sender=SalesRapport)
def update_reports(sender, instance, **kwargs):
    year = instance.month.year
    month = instance.month.month
    if month in [1, 2, 3]:
        quarter = 1
    elif month in [4, 5, 6]:
        quarter = 2
    elif month in [7, 8, 9]:
        quarter = 3
    else:
        quarter = 4
    # Update or save the quarterly and yearly reports accordingly



class ImportRapport(models.Model):
    SHIPPING_CHOICES = [
        (40, 'Truck (40 days)'),
        (45, 'Sea (45 days)'),
        (30, 'Air (30 days)'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateField()
    arrival_date = models.DateField()
    production_time = models.IntegerField()
    shippingmethode = models.IntegerField(choices=SHIPPING_CHOICES)
    order_price = models.FloatField()
    product_tag = models.CharField(max_length=100, choices=[('Test', 'Test'), ('Restock', 'Restock')])
    completed = models.DateTimeField(auto_now_add=True)
    
    @property
    def est_arrival_date(self):
        shipping_time = {
            40: 40,
            45: 45,
            30: 30
        }
        return self.order_date + timezone.timedelta(days=self.production_time + shipping_time[self.shippingmethode])
    
    def __str__(self):
        return f"{self.product} - {self.product_tag}"


class BrandTable(models.Model):
    brand = models.CharField(max_length=100)
    
    def get_revenue(self):
        # Function to calculate revenue for this brand
        pass
    
    def get_gross_margin(self):
        # Function to calculate gross margin for this brand
        pass
    
    def get_profit(self):
        # Function to calculate profit for this brand
        pass


class ProductDatabase(models.Model):
    brand = models.ForeignKey(BrandTable, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, choices=[('Test', 'Test'), ('Restock', 'Restock')])
    initial_stock = models.IntegerField()  # Initial stock imported
    sell_price = models.FloatField()
    supplier_name = models.CharField(max_length=100)
    supplier_link = models.URLField(max_length=100)
    order_history = models.ForeignKey(ImportHistory, on_delete=models.CASCADE)

    def current_stock(self):
        # Calculate the total units sold up to today
        total_units_sold = SalesRapport.objects.filter(product=self).aggregate(total_sold=Sum('quantity_sold'))['total_sold']
        total_units_sold = total_units_sold if total_units_sold else 0  # Set total_sold to 0 if None

        # Calculate the current stock
        current_stock = self.initial_stock - total_units_sold
        return current_stock



class ProductCalculator(models.Model):
    product_category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    supplier_link = models.URLField(max_length=100)
    quantity = models.IntegerField()
    sell_price = models.FloatField()
    estimated_import_price = models.FloatField()

    def calculate_metrics_and_recommendations(self):
        revenue = self.quantity * self.sell_price
        vat = self.sell_price * 0.21
        commission = (self.sell_price - vat) * 0.144
        shipping = 5.8 * self.quantity
        packaging = 0.8 * self.quantity
        other_costs = revenue * 0.02
        cogs = vat + commission + shipping + other_costs + packaging
        gross_margin = self.sell_price - vat - commission - shipping - packaging - other_costs
        gross_margin_percentage = (gross_margin / revenue) * 100 if revenue != 0 else 0
        profit = gross_margin - self.estimated_import_price
        profit_percentage = (profit / revenue) * 100 if revenue != 0 else 0
        winst = gross_margin - self.estimated_import_price
        winst_percentage = (winst / revenue) * 100 if revenue != 0 else 0
        return_percentage = 15
        return_amount = return_percentage / 100 * revenue
        return_shipping_cost = return_percentage / 100 * shipping
        return {
            'revenue': revenue,
            'vat': vat,
            'commission': commission,
            'shipping': shipping,
            'packaging': packaging,
            'other_costs': other_costs,
            'cogs': cogs,
            'gross_margin': gross_margin,
            'gross_margin_percentage': gross_margin_percentage,
            'profit': profit,
            'profit_percentage': profit_percentage,
            'winst': winst,
            'winst_percentage': winst_percentage,
            'return_percentage': return_percentage,
            'return_amount': return_amount,
            'return_shipping_cost': return_shipping_cost,
        }



## Workllog & Goal achievement Tabel
class Worklog(models.Model):
    CATEGORY_CHOICES = [
        ('Financial', 'Financial'),
        ('Import', 'Import'),
        ('Tax', 'Tax'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    task_name = models.CharField(max_length=100)
    hours_worked = models.FloatField()
    priority = models.IntegerField()
    notes = models.TextField()
    completed = models.BooleanField(default=False)
    date_completed = models.DateField(null=True, blank=True)

    def mark_completed(self):
        self.completed = True
        self.date_completed = timezone.now()
        self.save()

class Goal(models.Model):
    goal_name = models.CharField(max_length=100)
    achieve_date = models.DateField()

    def __str__(self):
        return self.goal_name





## Product Price Tracker / Recommended
class ProductPriceTracker(models.Model):
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    competitor_urls = models.TextField()  # Comma-separated URLs for competitors
    scrape_date = models.DateField()  # Date when the scraping is performed, runs monthly
    product_price = models.IntegerField()  # Field to store the scraped product price

    def get_product_price(self):
        # Implement scraping logic here to retrieve the product price from the competitor URLs
        # Update the 'product_price' field with the scraped product price
        # Save the instance
        # Return the scraped product price

class SellPriceCalculator(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)
    recommended_sell_price = models.FloatField()

    def calculate_recommended_sell_price(self):
        # Get all ProductPriceTracker instances for the current product
        product_trackers = ProductPriceTracker.objects.filter(product=self.product)
        
        if product_trackers.exists():
            # Calculate the mean of the product prices from all trackers
            mean_price = product_trackers.aggregate(models.Avg('product_price'))['product_price__avg']
            # Set the recommended sell price as the mean price
            self.recommended_sell_price = mean_price
        else:
            self.recommended_sell_price = None  # If no ProductPriceTracker instances found for the product