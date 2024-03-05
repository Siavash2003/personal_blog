from django.db import models

class Info(models.Model):
    profile_pic = models.ImageField(null=True, upload_to='img/profile')
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    about_me = models.TextField()
    instagram = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    telegram = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)
    experience = models.TextField(blank=True)

class Resume(models.Model):
    title = models.CharField(max_length=100)
    progress_bar = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
