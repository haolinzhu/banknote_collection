from django.db import models

# Create your models here.
COMPOSITION_CHOICES = (
    ("paper", "Paper"),
    ("polymer", "Polymer"),
    ("hybrid substrate", "Hybrid substrate"),
)

GRADE_CHOICES = (
    ("unc", "UNC"),
    ("au", "AU"),
    ("xf", "XF"),
    ("vf", "VF"),
    ("f", "F"),
    ("vg", "VG"),
    ("g", "G"),
)

class Banknote(models.Model):
    country = models.CharField(max_length=50)
    denomination = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=20)
    issuing_authority = models.CharField(max_length=50)
    composition = models.CharField(max_length=20, choices=COMPOSITION_CHOICES, default="paper")
    grade = models.CharField(max_length=5, choices=GRADE_CHOICES, default="unc")
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    intro_year = models.IntegerField(blank=True, null=True)
    intro_month = models.IntegerField(blank=True, null=True)
    intro_day = models.IntegerField(blank=True, null=True)
    acquire_year = models.IntegerField(blank=True, null=True)
    acquire_month = models.IntegerField(blank=True, null=True)
    acquire_day = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    pick = models.CharField(max_length=10)
    printer = models.CharField(max_length=50, blank=True, default="")
    # image = models.ImageField(upload_to='banknotes/')
    
    # def __str__(self):
    #     return self.country + " " + str(self.denomination) + " " + str(self.currency) + " " + str(self.year)
