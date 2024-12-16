from django import forms 
 
from .models import Comment 
 
 
class CommentCreationForm(forms.ModelForm): 
 
    class Meta: 
        model = Comment 
        fields = ['email', 'text', 'rating', 'product'] 
 
     
    def clean_rating(self): 
        rating = self.cleaned_data['rating'] 
        if 1 > rating > 5: 
            self.add_error('rating', 'Rating must be a number in range of 1 to 5') 
            return 
        return rating 
 
 
    def clean_text(self): 
        text = self.cleaned_data['text'] 
        if 'Bob' in text: 
            self.add_error('text', 'There must be no Bobs') 
            return 
        return text
