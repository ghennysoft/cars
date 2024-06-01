from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from shortuuid.django_fields import ShortUUIDField
from  django.contrib.auth import get_user_model


User = get_user_model()


#-------------------- Voyage --------------------------#
class SocieteAviation(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='societeAviation/')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'SocietesAviation'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class TrajetVoyage(models.Model):
    societe = models.ForeignKey(SocieteAviation, on_delete=models.CASCADE)
    trajet_id=ShortUUIDField(unique=True, length=20, max_length=30, alphabet='abcdefghijk1234567890')
    depart = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    prix = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Trajets voyage'

    def __str__(self):
        return f'{self.depart} »» {self.destination}  --by--  {self.societe.name}'
