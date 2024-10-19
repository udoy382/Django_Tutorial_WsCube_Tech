from django import forms


class UsersForm(forms.Form):
    First_Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    Middle_Name = forms.CharField()
    Last_Name = forms.CharField()
    Email = forms.EmailField()