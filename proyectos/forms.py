from django.forms import ModelForm
from .models import Proyecto, UserProfile
class CreateForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = [
            'titulo','tema', 'estudiante', 'profesor', 'patrocinado'
        ]
    
    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        # Filtrar los usuarios para el campo estudiante
        self.fields['estudiante'].queryset = UserProfile.objects.filter(es_profesor=False).select_related('user')
        # Filtrar los usuarios para el campo profesor
        self.fields['profesor'].queryset = UserProfile.objects.filter(es_profesor=True).select_related('user')