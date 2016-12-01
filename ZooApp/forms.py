from django import forms
from models import Animal,Donor

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class AnimalsForm(forms.ModelForm):
    """name = forms.CharField(max_length=25,min_length=3)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=(('MALE','MALE'),('FEMALE','FEMALE')))
    species = forms.CharField(max_length=25,min_length=3)
    status = forms.ChoiceField(choices=(('Endangered',"Endangered"),('Critically_Endangered','Critically Endangered'),
                                        ('Extinct','Extinct')))"""
    class Meta:
        model = Animal
        fields = ['name','gender','age']


class AnimalSearchForm(forms.Form):
    name = forms.CharField(max_length=25,min_length=3,
                           widget=forms.TextInput(attrs={'class':'description'}))
    species = forms.CharField(max_length=25,min_length=3,
                              widget=forms.TextInput(attrs={'class': 'description'}))


class BirdSearchForm(forms.Form):
    name = forms.CharField(max_length=25, min_length=3,
                           widget=forms.TextInput(attrs={'class': 'description'}))
    species = forms.CharField(max_length=25, min_length=3,
                              widget=forms.TextInput(attrs={'class': 'description'}))


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name','phone_no','mail_id','finance','addr',]

        widgets = {'name': forms.TextInput(attrs={'class': 'description'}),
                   'phone_no':forms.TextInput(attrs={'class': 'description'}),
                   'mail_id':forms.EmailInput(attrs={'class': 'description'}),
                   'finance': forms.NumberInput(attrs={'class': 'description'}),
                   'addr': forms.Textarea(attrs={'class': 'description'}),
                   }

    def clean(self):
        super(DonorForm,self).clean()
        if (self.cleaned_data['finance'])<0:
            self.add_error(error="Positive needed",field='finance')
            #raise ValidationError(ugtl("Positive needed"),params={"finance":self.cleaned_data['finance']})
        if len(self.cleaned_data['phone_no']) != 10:
            self.add_error(error="invalid phone number",field='phone_no')
            #raise ValidationError(ugtl("Invalid phone number"),params={"phone_no":self.cleaned_data['phone_no']})
        return self.cleaned_data


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'class':'description'}))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class':'description'}),
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields =['username','first_name','last_name','email',]

        widgets = {'username': forms.TextInput(attrs={'class': 'element text medium'}),
                   'first_name': forms.TextInput(attrs={'class': 'element text medium'}),
                   'last_name': forms.EmailInput(attrs={'class': 'element text medium'}),
                   'email': forms.NumberInput(attrs={'class': 'element text medium'}),
                   }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



