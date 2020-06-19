from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name



class UserParent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)


    def __str__(self):
        return self.father_name + self.mother_name


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')

    def __str__(self):
        return self.headline


class Category(models.Model):
    name = models.CharField(max_length=100)
    hero_count = models.PositiveSmallIntegerField(default=0)
    villian_count = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"


    def save(self, *args, **kwargs):
        if not self.pk:
            Category.objects.filter(pk=self.category_id).update(hero_count=F('hero_count')+1)
        super(Category, self).save(*args, **kwargs)


    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls.__meta.db_table))


class Hero(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Villian(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Origin(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super(Origin, self).save(*args, **kwargs)
