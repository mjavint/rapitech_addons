# -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'school'
    _description = 'school'

    # Campos basicos
    name = fields.Char(string='Nombre')
    value = fields.Integer()
    value2 = fields.Float(digits='Payment Terms')
    activado = fields.Boolean(string='Activado')

    # Campos avanzados
    hoy = fields.Date(string='Hoy')
    hoy_hora = fields.Datetime(string='Hoy con Hora')
    archivo = fields.Binary('Archivo')
    image = fields.Image('image', max_width=200, max_height=200)
    value3 = fields.Float(compute='_value_pc')
    name_related = fields.Char(
        related='partner_id.name', string='Name Relacionado'
    )
    description = fields.Text()
    seleccioname = fields.Selection(
        [
            ('prueba1', 'Prueba 1'),
            ('prueba2', 'Prueba 2'),
            ('prueba3', 'Prueba 3'),
            ('prueba4', 'Prueba 4'),
        ],
        string='Seleccioname',
    )

    # Campos relacionales
    partner_id = fields.Many2one(comodel_name='res.partner', string='Cliente')
    usuario_ids = fields.Many2many(comodel_name='res.users', string='Usuarios')
    company_ids = fields.One2many(
        comodel_name='res.company', inverse_name='school_id', string='Company'
    )

    @api.depends('value')
    def _value_pc(self):
        # self.env['account.move'].search([('state', '=', 'posted')]).filtered(
        #     lambda x: str(x.name).startswith('F001'))
        for record in self:
            record.value3 = float(record.value) / 100


class ResCompany(models.Model):
    _inherit = 'res.company'

    school_id = fields.Many2one(comodel_name='school', string='School')
