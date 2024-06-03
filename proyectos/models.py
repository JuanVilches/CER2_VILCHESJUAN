from django.db import models
# Importa el módulo 'models' de Django, que proporciona clases base para definir modelos de datos.

from django.contrib.auth.models import User
# Importa el modelo 'User' del módulo de autenticación de Django, que representa a los usuarios en el sistema.

class Proyecto(models.Model):

    titulo = models.CharField(max_length=100)# Define un campo de texto llamado 'titulo' con un máximo de 100 caracteres.
    tema = models.CharField(max_length=100)# Define un campo de texto largo llamado 'descripcion' sin límite de caracteres.
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)# Define una relación de clave foránea con el modelo 'User', representando al estudiante.
                                                                  # 'on_delete=models.CASCADE' significa que si el usuario asociado se elimina, también se eliminará el proyecto.
    patrocinado = models.BooleanField(default=False)# Define un campo booleano llamado 'patrocinado' que indica si el proyecto está patrocinado. Por defecto, es False.
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='proyectos_patrocinados')
    # Define otra relación de clave foránea con el modelo 'User', representando al profesor que patrocina el proyecto.
    # 'null=True' permite que este campo sea opcional.
    # 'blank=True' permite que el campo sea opcional en los formularios.
    # 'related_name' proporciona un nombre inverso para acceder a los proyectos patrocinados desde un objeto 'User'.
    def __str__(self):
        return self.titulo
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#apunta a el campo id de la tabla usuario
    # Define una relación de uno a uno con el modelo 'User', vinculando cada perfil de usuario a un usuario específico.
    #Esto significa que cada instancia de UserProfile está asociada con exactamente un usuario.
    # 'on_delete=models.CASCADE' significa que si el usuario asociado se elimina, también se eliminará el perfil de usuario.
    es_profesor = models.BooleanField(default=False)# Define un campo booleano llamado 'es_profesor' que indica si el usuario es un profesor. Por defecto, es False.
    #Este método es utilizado para proporcionar una representación en cadena legible para humanos de la instancia de UserProfile. Cuando imprimes una instancia de UserProfile, este método controla qué se muestra.
    def __str__(self):
        return self.user.username