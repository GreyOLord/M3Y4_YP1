from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(choices=[('admin' , 'Admin'),( 'user', 'User')])
    group = models.ManyToManyField('Groups',related_name="groups")
    

    def __str__(self):
        return self.name

    def change_role(self,role_name):
        self.role = role_name
        self.save()

# ну і незнаю там сказано про можливість додати до групи то давай я створю модель групу дам її : назву , тему , адміна ,
        
class Groups(models.Model):
    name  = models.CharField(max_length=100)
    topic  = models.CharField(max_length=100)
    admin = models.ManyToManyField('User',related_name="administ")


    def __str__(self):
        return self.name





# Create your models here.
