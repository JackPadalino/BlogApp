from django.apps import AppConfig # this import standard with Django

 # the class standard with Django
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
