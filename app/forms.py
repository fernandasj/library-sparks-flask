from flask_wtf import Form
from wtforms import StringField, IntegerField, DateField
import datetime


class ReservaForm(Form):
    Id_reserva = IntegerField('Id_reserva')
    Id_usuario = IntegerField('Id_usuario')
    Id_livro = IntegerField('Id_livro')


class EmprestarForm(Form):
    Id_emprestimo = IntegerField('Id_emprestimo')
    Id_usuario = IntegerField('Id_usuario')
    Id_livro = IntegerField('Id_livro')
    Data_emprestimo = DateField('Data_emprestimo')
