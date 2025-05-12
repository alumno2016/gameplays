from django.db import models

# Create your models here.
palabras = [        
        "MANATI", 
        "PERRO", 
        "GATO", 
        "CONEJO", 
        "TIBURON",
        "ELEFANTE",
        "ALCON",
        "SERPIENTE",
        "JAGUAR",
        "CANGURO",
        "LOBO",
        "MONO",
        "NUTRIA",
        "LEON",
        "LORO",
        "TORO",
        "ORUGA"
        ]

class Search(models.Model):
    dash = models.TextField()
    words = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Soup {self.date}"
