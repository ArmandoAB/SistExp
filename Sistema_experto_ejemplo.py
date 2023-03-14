# Base de datos del sistema experto ejemplo en la que se usan tuplas

knowledge_base = {
    'gripe': ['fiebre', 'dolor de cabeza', 'dolor de cuerpo'],
    'resfriado': ['congestión nasal', 'tos', 'estornudos'],
    'alergia': ['picazón en los ojos', 'estornudos', 'secreción nasal']
}

# Motor de inferencia

from pyknow import *

class Enfermedad(Fact):
    pass

class SistemaExpert(KnowledgeEngine):
    @Rule(OR(Enfermedad(sintoma='fiebre'),
             Enfermedad(sintoma='dolor de cabeza'),
             Enfermedad(sintoma='dolor de cuerpo')))
    def gripe_rule(self):
        self.declare(Enfermedad(nombre='gripe'))

    @Rule(OR(Enfermedad(sintoma='congestión nasal'),
             Enfermedad(sintoma='tos'),
             Enfermedad(sintoma='estornudos')))
    def resfriado_rule(self):
        self.declare(Enfermedad(nombre='resfriado'))

    @Rule(OR(Enfermedad(sintoma='picazón en los ojos'),
             Enfermedad(sintoma='estornudos'),
             Enfermedad(sintoma='secreción nasal')))
    def alergia_rule(self):
        self.declare(Enfermedad(nombre='alergia'))

# Interfaz de usuario

        import tkinter as tk

def get_diagnosis():
    # Lógica para obtener la enfermedad a partir de los síntomas
    diagnosis = "Gripe"
    diagnosis_label.config(text=f"La enfermedad es: {diagnosis}")

root = tk.Tk()
root.geometry("400x300")

symptoms_label = tk.Label(root, text="Ingrese los síntomas:")
symptoms_label.pack()

symptoms_entry = tk.Entry(root)
symptoms_entry.pack()

diagnose_button = tk.Button(root, text="Diagnosticar", command=get_diagnosis)
diagnose_button.pack()

diagnosis_label = tk.Label(root, text="")
diagnosis_label.pack()

root.mainloop()

# Módulo de explicación

explanation = f"El paciente presenta los siguientes síntomas: {', '.join(patient_symptoms)}. A partir de estos síntomas, se infiere que el paciente tiene {diagnosis}, ya que estos síntomas coinciden con los síntomas típicos de la gripe según nuestra base de conocimientos."

# Módulo de adquisición de conocimientos

def add_disease(name, symptoms):
    knowledge_base[name] = symptoms
    print(f"Se ha agregado la enfermedad {name} con los síntomas {symptoms} a la base de conocimientos.")

# Agregar la enfermedad 'neumonía' a la base de conocimientos
add_disease('neumonía', ['fiebre alta', 'tos', 'dificultad para respirar'])