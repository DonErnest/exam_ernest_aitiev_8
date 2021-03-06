from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts.models import Review, Profile


class UserSignUpForm(forms.ModelForm):
    email = forms.EmailField(label='Электронный адрес', required=True, widget=forms.EmailInput)
    password=forms.CharField(max_length=100, required=True, label='Password', widget=forms.PasswordInput, strip=False)
    password_confirm = forms.CharField(max_length=100, required=True, label='Password input', widget=forms.PasswordInput, strip=False)

    def password_check(self):
        password = self.cleaned_data.get('password')
        password_check = self.cleaned_data.get('password_confirm')
        if password != password_check:
            raise ValidationError('Password does not match!', code='passwords_do_not_match')

    def first_last_empty_check(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise ValidationError('Both first name and last name are empty!',
                                  code='first_last_empty_values')

    def clean(self):
        super().clean()
        self.password_check()
        self.first_last_empty_check()
        return self.cleaned_data

    def save(self, commit=True):
        user=super(UserSignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields=['username','password','password_confirm','first_name','last_name','email']


class UserChangeForm(forms.ModelForm):
    avatar = forms.ImageField(label='Аватар', required=False)

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit)
        self.save_profile(commit)
        return user

    def save_profile(self, commit=True):
        profile = self.instance.profile

        for field in self.Meta.profile_fields:
            setattr(profile, field, self.cleaned_data[field])

        if not profile.avatar:
            profile.avatar = None

        if commit:
            profile.save()

    def get_initial_for_field(self, field, field_name):
        if field_name in self.Meta.profile_fields:
            return getattr(self.instance.profile, field_name)
        return super(UserChangeForm, self).get_initial_for_field(field, field_name)


    class Meta:
        model =User
        fields = ['first_name', 'last_name', 'email', 'avatar']
        profile_fields = ['avatar']

class UserPasswordChangeForm(forms.ModelForm):
    old_password = forms.CharField(max_length=100, required=True, label='Старый пароль',
                                       widget=forms.PasswordInput, strip=False)
    password = forms.CharField(max_length=100, required=True, label='Новый пароль', widget=forms.PasswordInput, strip=False)
    password_confirm = forms.CharField(max_length=100, required=True, label='Подтвердите новый пароль',
                                       widget=forms.PasswordInput, strip=False)


    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Это не старый пароль!')
        return old_password

    def clean(self):
        super().clean()
        password_1 = self.cleaned_data.get('password')
        password_2 = self.cleaned_data.get('password_confirm')
        if password_1 != password_2:
            raise ValidationError('Пароли не совпадают!', code='passwords_do_not_match')
        return self.cleaned_data

    def save(self, **kwargs):
        kwargs['commit'] = False
        self.instance = super().save(**kwargs)
        self.instance.set_password(self.cleaned_data['password'])
        self.instance.save()
        return self.instance

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']


class ReviewForm(forms.ModelForm):

    class Meta:
        model=Review
        fields = ['rating', 'review']