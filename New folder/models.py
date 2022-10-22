from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
from django.utils.timezone import now


class Investmentplan(models.Model):
    currencychoice = [
        ('NGN', 'NGN'),
        ('USD', 'USD'),
    ]
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    inestment_name = models.CharField(blank=True, max_length=500)
    investment_description = models.TextField(blank=True, max_length=5000)
    investment_active = models.BooleanField(default=True)
    investment_posteddate = models.DateTimeField(auto_now_add=True)
    investent_rate = models.PositiveIntegerField(blank=True, default=12)
    inveestment_currency = models.CharField(blank=True, max_length=500, default="NGN", choices=currencychoice)


    def __str__(self):
        return self.inestment_name


class Loanplan(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Loan_name = models.CharField(blank=True, max_length=500)
    Loan_description = models.TextField(blank=True, max_length=5000)
    Loan_active = models.BooleanField(default=True)
    Loan_posteddate = models.DateTimeField(auto_now_add=True)
    Loan_rate = models.PositiveIntegerField(blank=True, default=12)

    def __str__(self):
        return self.Loan_name


class Startinvestment(models.Model):
    Workstatus = [
        ('pending confirmation', 'pending confirmation'),
        ('submitted for review', 'submitted for review'),
        ('Awaiting Payment', 'Awaiting Payment'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
    ]
    reference = models.CharField(blank=True, max_length=500)
    requestuser = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Investmentplan, on_delete=models.CASCADE)
    status = models.CharField(blank=True, max_length=500, choices=Workstatus, default='pending confirmation')
    tenor = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    interest_rate = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    interest_amount = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    maturity_date = models.DateField(default=now)
    effective_date = models.DateField(default=now)
    principal = models.FloatField(blank=True)
    total_amount_payable = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    updated_at = models.DateTimeField(auto_now=True)
    payment_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.status


class Loanoverview(models.Model):
    Workstatus = [
        ('pending confirmation', 'pending confirmation'),
        ('submitted for review', 'submitted for review'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
        ('Processing Payment', 'Processing Payment'),
    ]

    LoanPurpose = [
        ('Business Loans', 'Business Loans'),
        ('Individual Loans', 'Individual Loans'),
    ]

    Repaymentsource = [
        ('Working Capital', 'Working Capital'),
        ('Asset Financing', 'Asset Financing'),
        ('Cashflow/Bridging Financial', 'Cashflow/Bridging Financial'),
        ('Local Purchase Orderfinacing', 'Local Purchase Orderfinacing'),
        ('Project Handling', 'Project Handling'),
        ('Invoive Discounting', 'Invoive Discounting'),
    ]

    reference = models.CharField(blank=True, max_length=500)
    requestuser = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Loanplan, on_delete=models.CASCADE)
    status = models.CharField(blank=True, max_length=500, choices=Workstatus, default='pending confirmation')
    tenor = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    interest_rate = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    monthly_repayment = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    principal = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    total_repayment = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    total_interest = models.DecimalField(blank=True, decimal_places=2, max_digits=30, default=1)
    maturity_date = models.DateField(default=now)
    effective_date = models.DateField(default=now)
    updated_at = models.DateTimeField(auto_now=True)
    payment_data = models.JSONField(blank=True, null=True)
    loanpurpose = models.CharField(blank=True, max_length=500, choices=LoanPurpose, default='Individual Loans')
    Repayment_Source = models.CharField(blank=True, max_length=500, choices=Repaymentsource, default='Working Capital')

    def __str__(self):
        return self.status


class Loanpaymenthistory(models.Model):
    Payment_status = [
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
    ]
    reference = models.CharField(blank=True, max_length=500)
    payment_for = models.ForeignKey(Loanoverview,on_delete=models.CASCADE)
    payment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_paid = models.PositiveIntegerField(default=1000)
    updated_at = models.DateTimeField(auto_now=True)
    payment_data = models.JSONField(blank=True, null=True)
    status = models.CharField(blank=True, max_length=500, choices=Payment_status)



class Person(models.Model):
    name = models.CharField(max_length=128,  null=True, blank=True)
    last_name = models.CharField(max_length=50,  null=True, blank=True)
    birth_date = models.DateTimeField(default=timezone.now)
    sent_to = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class Subscribers(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Scheduleinvestmentplan(models.Model):
    Workstatus = [
        ('pending confirmation', 'pending confirmation'),
        ('submitted for review', 'submitted for review'),
        ('Awaiting Payment', 'Awaiting Payment'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
    ]
    reference = models.CharField(blank=True, max_length=500)
    requestuser = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Investmentplan, on_delete=models.CASCADE)
    status = models.CharField(blank=True, max_length=500, choices=Workstatus, default='pending confirmation')
    tenor = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    interest_rate = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    interest_amount = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    maturity_date = models.DateField(default=now)
    effective_date = models.DateField(default=now)
    principal = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    total_amount_payable = models.DecimalField(blank=True, decimal_places=2, max_digits=30)
    updated_at = models.DateTimeField(auto_now=True)
    payment_data = models.JSONField(blank=True, null=True)
    schedule_status = models.BooleanField(default=False)
    issue =  models.CharField(blank=True, max_length=500)



    def __str__(self):
        return self.requestuser.username



class scheduleloanrepayment(models.Model):
    Payment_status = [
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled'),
    ]
    effective_date = models.DateField(default=now)
    schedule_status = models.BooleanField(default=False)
    reference = models.CharField(blank=True, max_length=500)
    payment_for = models.ForeignKey(Loanoverview,on_delete=models.CASCADE)
    payment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_paid = models.PositiveIntegerField(default=1000)
    updated_at = models.DateTimeField(auto_now=True)
    payment_data = models.JSONField(blank=True, null=True)
    status = models.CharField(blank=True, max_length=500, choices=Payment_status)

    def __str__(self):
        return self.payment_user.username