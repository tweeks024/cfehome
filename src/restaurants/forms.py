from django import forms


class RestaurantCreateForm:
    name            = forms.CharField()
    location        = forms.CharField(required=False)
    category        = forms.CharField(required=False)
