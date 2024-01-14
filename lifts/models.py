from django.db import models

# Create your models here.
class bench(models.Model):
    weight = models.IntegerField(null=True)
    sets = models.IntegerField(null=True)
    reps = models.IntegerField(null=True)
    date = models.DateField(null=True)
    
    
    @property
    def estimate(self):
        return self.weight/( 1.0278 -(0.0278 * self.reps) )
    
    class Meta:
        ordering = ('date',)
    
class squat(models.Model):
    weight = models.IntegerField(null=True)
    sets = models.IntegerField(null=True)
    reps = models.IntegerField(null=True)
    date = models.DateField(null=True)
    
    @property
    def estimate(self):
        return self.weight/( 1.0278 -(0.0278 * self.reps) )
    
    class Meta:
        ordering = ('date',)

class dead(models.Model):
    weight = models.IntegerField(null=True)
    sets = models.IntegerField(null=True)
    reps = models.IntegerField(null=True)
    date = models.DateField(null=True)
    
    
    @property
    def estimate(self):
        return self.weight/( 1.0278 -(0.0278 * self.reps) )
    
    class Meta:
        ordering = ('date',)   