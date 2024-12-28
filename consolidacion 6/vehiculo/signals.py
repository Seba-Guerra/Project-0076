from django.db.models.signals import post_save 
from django.contrib.auth.models import User, Permission 
from django.contrib.contenttypes.models import ContentType 
from django.dispatch import receiver 
from .models import Vehiculo

@receiver(post_save, sender=User) 
def assign_visualizar_catalogo_permission(sender, instance, created, **kwargs): 
    if created: 
        content_type = ContentType.objects.get_for_model(Vehiculo) 
        permission = Permission.objects.get(codename='visualizar_catalogo', content_type=content_type) 
        instance.user_permissions.add(permission)


