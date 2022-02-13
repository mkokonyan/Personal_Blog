from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-contact',
            }
        )
    )
    email = forms.EmailField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-contact',
            }
        )
    )
    company = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-contact',
            }
        )
    )
    message = forms.CharField(max_length=2000,
                              widget=forms.Textarea(
                                  attrs={
                                      'class': 'form-control form-contact',
                                      'rows': 7,
                                  }
                              )
                              )
