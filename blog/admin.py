from django.contrib import admin
from .models import Post
from .forms import ContactForm

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','created_on')
    list_filter = ['created_on']
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_on')


admin.site.register(Post, PostAdmin)



admin.site.register(ContactForm, ContactAdmin)