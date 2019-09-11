# -*- coding: utf-8 -*-

import base64
from odoo import models, fields, api

class descarga_e3l(models.Model):
    _name = 'descarga.e3l'
    _description='Descarga E3L'
        
    x_e3l_id = fields.Many2one(
        'x_dis', 
        string='E3L Descargable'
    )
    x_name = fields.Char(
        string='Nombre Di asociado',
    )
    x_anexo = fields.Binary(
        string='Anexo E3L',
                           ) 
            
    @api.constrains('x_e3l_id')
    def genera_anexo(self):
        self.x_name = self.x_e3l_id.x_codigo_di + '.xml'
        self.x_anexo = base64.encodestring(self.x_e3l_id.x_di_e3l.encode())
        