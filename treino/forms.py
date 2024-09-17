from django import forms
from .models import Treino

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'descricao', 'data']
        widgets = {
            'data': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Selecione uma data', 'type':'date'}),
            'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do treino'}),
            'descricao': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição do treino'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 3:
            raise forms.ValidationError('Nome deve ter mais de 3 caracteres')
        return nome