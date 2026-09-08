from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='İstifadəçi adı',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "İstifadəçi adı buraya"
        })
    )
    email = forms.EmailField(
        label='Elektron poçt',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "Email buraya Məsələn: someone@some.com"
        })
    )
    password = forms.CharField(
        label='Şifrə',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': "Şifrə"
            }
        ))
    confirm_password = forms.CharField(
        label='Şifrənin təstiqi',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': "Şifrənin təkrarı"
            }
        ))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password and password and confirm_password:
            raise forms.ValidationError("Şifrələr uyğun deyil")
        return cleaned_data


class LoginForm(forms.Form):
    username_or_email = forms.CharField(
        label='İstifadəçi adı və ya email',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': "İstifadəçi adı və ya email buraya"
        })
    )
    password = forms.CharField(
        label='Şifrə',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',
        }))
