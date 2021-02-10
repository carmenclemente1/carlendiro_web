# -*- coding: utf-8 -*- 
from odoo import models, fields 
class CalendarioTask(models.Model): 
    _name = 'calendario.task' 
    _description = 'Calendario Task'
    name = fields.Char('Description', required=True) 
    is_done = fields.Boolean('Done?') 
    active = fields.Boolean('Active?', default=True)
    def do_marcar(self):
        self.is_done = not self.is_done
        return True
    def do_limpiar(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
     
