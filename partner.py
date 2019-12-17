from odoo import api, fields, models, _

class Partner(models.Model):
	_name = 'res.partner'
	_inherit = 'res.partner'

	is_instructur = fields.Boolean(string="Is Instructur")