from django.db import models

# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    others = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField()

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class newsLetter(models.Model):
    email_letter = models.EmailField()

    def __str__(self):
        return self.email_letter

    class Meta:
        verbose_name = "NewsLetter"
        verbose_name_plural = "NewsLetters"
