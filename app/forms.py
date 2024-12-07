from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["email", "text", "rating", "product_id"]
    
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            self.add_error('rating', 'rating must be number from 1 to 5')
            return
        return rating

    
    def clean_text(self):
        text = self.cleaned_data['text']
        if 'Bob' in text:
            self.add_error('text', 'There must be no Bob')
            return
        return text
