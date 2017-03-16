from django import forms


class UserForm(forms.Form):
    val = forms.CharField(label='User.{id,username,email}')

    def get_lookup(self):
        val = self.cleaned_data['val']

        if '@' in val:
            return {'email': val}

        try:
            v = int(val)
            if len(val) >= 10:
                return {'username': val}
            else:
                return {'pk': v}
        except:
            return {'username': val}
