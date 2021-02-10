#-*- coding: utf-8 -*-
from odoo import models, fields, api
class CalendarioTask(models.Model):
    _name = 'calendario.task'
    _inherit = ['calendario.task','mail.thread']
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="Breve descripcion de la tarea.")
    horas_estimadas = fields.Integer('Estimacion en horas')
 # def do_marcar(self):
       # if self.user_id != self.env.user:
      #       raise Exception('Solo el responsable ha de marcarla como hecha!')
    #     else:
     #        return super(CalendarioTask, self).do_marcar()
 #    def do_limpiar(self):
  #       domain = [('is_done', '=', True), '|', ('user_id','=', self.env.uid), ('user_id', '=', False)]
 #        done_recs = self.search(domain)
 #        done_recs.write({'active': False})
  #       return True