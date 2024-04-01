from crispy_form.layout import Submit
from crispy_form.helper import FormHelper
from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]

  
  def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))