from django.contrib import admin
from django import forms
from home.models import Blog

class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Blog
        fields = "__all__"

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    list_display = ('title', 'language', 'time')  # Optional: fields to display in the admin list

admin.site.register(Blog, BlogAdmin)
