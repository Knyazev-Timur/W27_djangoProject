from django.db import models


class Vacancy(models.Model):
    STATUS = [
        ("draft", "Черновик"),
        ("open", "открыто"),
        ("close", "закрыт")
    ]

    slug = models.SlugField(max_length=50)
    text = models.CharField(max_length=2000)
    status = models.CharField(max_length=8, choices=STATUS, default="draft")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.slug
