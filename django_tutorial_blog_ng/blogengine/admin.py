import models
from django.contrib import admin
from django.contrib.auth.models import User

# from django.forms import ModelForm
# from suit.widgets import HTML5Input


# # customize post input field
# class PostForm(ModelForm):
#     class Meta:
#         widgets = {
#             'color': HTML5Input(input_type='color'),
#         }


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    # form = PostForm

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
