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
            'district': forms.Select(attrs={"hx-get": "load_branches/", "hx-target": "#id_branch"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            district_id = int(self.data.get('district'))
            self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id)

      