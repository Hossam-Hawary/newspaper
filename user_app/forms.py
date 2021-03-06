
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')
# check the both passwords ..they have to be the same
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch', #the error that intialized above
            )
        return password2


#uniqe userName 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("The username already exists. Please try another one.")
 

# overrided method !!
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
#uniqe mail
def clean_email(self):
    	email = self.cleaned_data.get('email')
        print User.objects.filter(email=email).count()
    	if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError("This email address is already registered.")
        return email