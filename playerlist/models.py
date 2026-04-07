from django.db import models

class Player(models.Model):
    name =models.CharField(max_length = 50)
    dateJoined = models.DateField()
    Positions = [
        ("S", "Setter"),
        ("L", "Libero"),
        ("MH", "Middle Hitter"),
        ("OP", "Opposite Hitter"),
        ("OH", "Outside Hitter"),
        ("DS", "Defensive Specialist"),
    ]
    position = models.CharField(max_length = 3, choices=Positions)
    salary = models.DecimalField(max_digits=10, decimal_places=4)
    contactPerson=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_position_display()})"

# Create your models here.
