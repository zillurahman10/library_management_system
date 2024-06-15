# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Account

# class RegistrationForm(UserCreationForm):
#     # # profile_image = forms.FileField()
#     username = forms.CharField( widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
#     password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
#     password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input input-bordered'}))
#     shipping_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered'}))

#     class Meta:
#         model = User
#         fields = '__all__'
        
#     def save(self, commit=True):
#         our_user = super().save(commit=False)
#         if commit == True:
#             our_user.save() 
#             first_name = self.cleaned_data.get('first_name')
#             last_name = self.cleaned_data.get('last_name')
#             shipping_address = self.cleaned_data('shipping_address')
            
#             Account.objects.create(
#                 user = our_user,
#                 first_name = first_name,
#                 last_name = last_name,
#                 shipping_address = shipping_address
#             )
#         return our_user



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input input-bordered'}))
    shipping_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
    profile_image = forms.FileField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'profile_image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
            Account.objects.create(
                user=user,
                first_name=self.cleaned_data.get('first_name'),
                profile_image=self.cleaned_data.get('profile_image'),
                last_name=self.cleaned_data.get('last_name'),
                shipping_address=self.cleaned_data.get('shipping_address')
            )
        return user

class DepositForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['balance']
        widgets = {
            'balance': forms.TextInput(attrs={'class': 'input input-bordered'})
        }