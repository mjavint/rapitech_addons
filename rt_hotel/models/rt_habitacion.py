# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RTHabitacion(models.Model):
    _name = 'rt.habitacion'
    _description = 'Habitación'

    # tipo, capacidad, estado de limpieza
    name = fields.Char(string='Nombre', compute='_compute_name')
    nro = fields.Integer(string='Nro')
    tipo = fields.Selection(
        selection=[
            ('suite', 'Suite'),
            ('especial', 'Especial'),
            ('normal', 'Normal'),
        ],
        string='Tipo',
    )
    capacidad = fields.Integer(string='Capacidad')
    esta_limpio = fields.Boolean(string='Esta Limpio')

    @api.depends('nro')
    def _compute_name(self):
        for record in self:
            record.name = f'Habitación {str(record.nro)}'
