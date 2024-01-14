from django import forms
from .models import bench, squat, dead



class BenchForm(forms.ModelForm):
   class Meta:
      model = bench
      fields = ('id', 'weight', 'sets', 'reps', 'date')

class SquatForm(forms.ModelForm):
   class Meta:
      model = squat
      fields = ('id', 'weight', 'sets', 'reps', 'date')

class DeadForm(forms.ModelForm):
   class Meta:
      model = dead
      fields = ('id', 'weight', 'sets', 'reps', 'date')