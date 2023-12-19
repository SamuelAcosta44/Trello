from django.contrib.auth.forms import AuthenticationForm

class SimpleAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(SimpleAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
