from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user','satellite', 'date_time','subsystem_type', 'details','photo','upload']
        widgets={
            'user':forms.HiddenInput(), 
            'satellite':forms.Select(attrs={'class':' form-control w-50'}),
            'date_time':forms.DateTimeInput(attrs={'type':'datetime-local','class':'form-control w-50'}),
            # 'date_time':forms.DateTimeInput(attrs={'type':'datetime','class':'datepicker','class':'form-control w-50'}),
            'subsystem_type':forms.Select(attrs={'class':'form-select w-50'}),
            'details':forms.Textarea(attrs={'class':'form-control'}),
            # 'detail':forms.TextInput(attrs={'class':'form-group1 form-control','id':'exampleFormControlTextarea1' ,'rows':'3'}),
            'photo':forms.FileInput(),
            # 'photo':forms.FileInput(attrs={'class':'form-control w-50'}),
            'upload':forms.FileInput(attrs={'class':'form-control w-50','type':'file'}),
            # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
            }
        # localized_fields = ('date_time',)


# class SatDetailForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['satellite']
