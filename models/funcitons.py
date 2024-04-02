from django.db.models import Sum

def get_yearly_report(queryset, year):
    yearly_data = queryset.filter(month__year=year).values('month').annotate(total_price=Sum('price')).order_by('month')
    yearly_report = {}
    total_year_price = 0

    for data in yearly_data:
        month_name = data['month'].strftime('%B')
        yearly_report[month_name] = data['total_price']
        total_year_price += data['total_price']

    yearly_report['Total Year'] = total_year_price

    return yearly_report

def get_quarterly_report(queryset, year, quarter):
    quarters = {
        'Q1': ['January', 'February', 'March'],
        'Q2': ['April', 'May', 'June'],
        'Q3': ['July', 'August', 'September'],
        'Q4': ['October', 'November', 'December']
    }

    quarter_months = quarters.get(quarter)
    if not quarter_months:
        return {}

    quarter_data = queryset.filter(month__year=year, month__month__in=range(1, 13)).values('month').annotate(total_price=Sum('price')).order_by('month')
    quarterly_report = {}
    total_quarter_price = 0

    for data in quarter_data:
        month_name = data['month'].strftime('%B')
        if month_name in quarter_months:
            quarterly_report[month_name] = data['total_price']
            total_quarter_price += data['total_price']

    quarterly_report[f'Total {quarter}'] = total_quarter_price

    return quarterly_report