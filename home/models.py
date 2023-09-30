from django.db import models

# Create your models here.
class Uplaod(models.Model):
    """Model definition for Uplaod."""

    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

    class Meta:
        """Meta definition for Uplaod."""

        verbose_name = 'Uplaod'
        verbose_name_plural = 'Uplaods'

    def __str__(self):
        """Unicode representation of Uplaod."""
        return self.caption
    
class DemoTable(models.Model):
    #string, number, date, time, email, url, file, image, boolen, choice,multiple choice,large text
    gender_choices = (("M","Male"),
                      ("F","Female"),
                      ("NS","Not Specified"))
    name = models.CharField(max_length=30)
    age = models.IntegerField(null = True, blank = True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    daterime =  models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    url = models.URLField(max_length=200)
    file = models.FileField(upload_to='files/')
    avatar = models.ImageField(upload_to='avatars/')
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=2, choices=gender_choices)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=100)
    given_to = models.CharField(max_length=50)
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Photographer(models.Model):
        name = models.CharField(max_length=100)
        image = models.ImageField(upload_to='image/')

        def _str_(self):
            return self.name
        
class PhotographerProfile(models.Model):
            gender_choices = ((0, "Female"), (1, "MALE"), (3,"OTHER"))
            photographer = models.OneToOneField(Photographer, on_delete=models.CASCADE, related_name='profile')
            city = models.CharField(max_length=50)
            gender = models.IntegerField(choices=gender_choices)

            def __str__(self):
                return f"{self.photographer.name}"  
            
class Team(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Player(models.Model):
     name = models.CharField(max_length=100)
     team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='Players')
     def __str__(self):
        return self.name