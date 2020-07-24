from django import forms


class InputForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "Enter Patient Name"
            }
        ), required=True)
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control"
            }
        ), required=True)
