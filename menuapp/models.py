from django.db import models

class Category(models.Model):
  category = models.CharField(max_length=100, null=True, blank=True)

  class Meta:
    db_table = 'category'

  def __str__(self):
    return self.category

# Create your models here.
class Menu(models.Model):
  menuName = models.CharField(max_length=100, null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.PROTECT)
  image = models.ImageField(upload_to='media')
  items = models.TextField()
  author = models.CharField(max_length=200, null=True, blank=True)

  class Meta:
    db_table = 'menuapp_menu'

  def __str__(self):
    return self.menuName