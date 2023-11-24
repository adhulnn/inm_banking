from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Continue_register,District,Branch


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'style': 'width: 100%;'})

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control', 'style': 'width: 100%;'})

    class Meta:
        model = User
        fields = ['username', 'password']

class ContinueRegisterForm(forms.ModelForm):
    class Meta:
        model = Continue_register
        fields = ['name', 'dob', 'age', 'gender', 'email', 'phone', 'address', 'district', 'branch', 'account_type', 'materials_provide']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={"hx-get": "load_branches/", "hx-target": "#id_branch", 'class': 'form-control'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
            'materials_provide': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
    
    MATERIALS_CHOICES = [
        ('debit_card', 'Debit Card'),
        ('credit_card', 'Credit Card'),
        ('cheque_book', 'Cheque Book'),
        ('pass_book', 'Pass Book'),
    ]

    materials_provide = forms.MultipleChoiceField(
        choices=MATERIALS_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            district_id = int(self.data.get('district'))
            self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id)
      