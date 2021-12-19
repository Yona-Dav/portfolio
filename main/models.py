from django.db import models

# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    image1 = models.ImageField(upload_to='picture', blank=True)
    image2 = models.ImageField(upload_to='picture', blank=True)
    image3 = models.ImageField(upload_to='picture', blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.ManyToManyField(Skills)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='picture', blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
