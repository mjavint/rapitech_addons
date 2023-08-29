# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class addons/base_template(models.Model):
#     _name = 'addons/base_template.addons/base_template'
#     _description = 'addons/base_template.addons/base_template'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
