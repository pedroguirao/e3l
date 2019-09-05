# -*- coding: utf-8 -*-

import base64
from odoo import models, fields, api

class d_e3l(models.Model):
	_name = 'd_e3l'
    
    e3l_filename = fields.Char()
    e3l_binary = fields.Binary()
    x_di_e3l_id = fields.Many2one('x_dis',string='E3L Descargable')
    
	@api.onchange('x_di_e3l_id')
    def generate_file(self):
        return self.write({
            'e3l_filename': self.x_di_e3l_id.x_name +'.xml',
            'e3l_binary': base64.encodestring(self.x_di_e3l_id.x_di_e3l.encode())
        })