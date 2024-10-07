from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self,email, password, **Kwargs):
        if not email :
           raise ValueError("L'addresse email est obligatoire.")
        
        # convertit la partie du domaine en minuscule / élimine les espaces .
        email = self.normalize_email(email)
        
        # permet la création d'une nouvelle instance
        user = self.model(email = email, **Kwargs)
        
        # fournissant un algorithme de hashage de mot de passe 
        user.set_password(password)
        
        # sauvegarde la nouvelle instance de l'utilisateur crée
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **Kwargs):
        Kwargs['is_staff'] = True
        Kwargs['is_superuser'] = True
        Kwargs['is_active'] = True
        
        return self.create_user(email = email, password = password, **Kwargs)
    
class Customer(AbstractUser):
        username = models.CharField(max_length=90, blank = True, null =True) 
        email = models.EmailField(max_length=240, unique = True, verbose_name=_("User_Email"))

        # Ajout de related_name pour éviter les conflits avec le modèle User par défaut
        groups = models.ManyToManyField(Group, related_name="customer_groups", blank=True)
        user_permissions = models.ManyToManyField(Permission, related_name="customer_user_permissions", blank=True)
    
        USERNAME_FIELD = "email"
        REQUIRED_FIELDS = [] 
        
        objects = CustomUserManager()
        
        def __str__(self):
            return self.email
        
        class Meta:
            verbose_name = _("Customer")
            verbose_name_plural = _("Customers")