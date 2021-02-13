from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    first_name =forms.CharField(min_length=3,max_length = 50,label = "İsim")
    last_name =forms.CharField(min_length=3,max_length = 50,label = "Soyisim")
    username = forms.CharField(min_length=3,max_length = 50,label = "Kullanıcı Adı")
    email = forms.EmailField(label = "Email")
    password = forms.CharField(min_length=3,max_length=20,label = "Parola",widget = forms.PasswordInput)
    confirm = forms.CharField(min_length=3,max_length=20,label ="Parolayı Doğrula",widget = forms.PasswordInput)
    
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values = {
            "username" : username,
            "password" : password,
            "email" : email,
            "first_name":first_name,
            "last_name":last_name
        }
        return values
