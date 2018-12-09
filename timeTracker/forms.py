from django import forms

class AddHoursForm(forms.Form):
	fecha = forms.CharField(required=True)
	proyecto = forms.CharField(required=True)
	tarea = forms.IntegerField(required=True)