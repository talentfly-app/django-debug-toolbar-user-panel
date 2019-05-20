from django import forms


class UserForm(forms.Form):
    val = forms.CharField(label='User.{id,username,email}')

    def get_lookup(self):
        from django.contrib.auth import get_user_model
        username_field = get_user_model().USERNAME_FIELD
        val = self.cleaned_data['val']

        if '@' in val:
            return {'email': val}

        try:
            v = int(val)
            if len(val) >= 10:
                return {username_field: val}
            else:
                return {'pk': v}
        except:
            return {username_field: val}
