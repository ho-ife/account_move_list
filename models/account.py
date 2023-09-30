from odoo import models, fields

class AccountAccount(models.Model):
    _inherit = 'account.account'

    move_lines = fields.One2many('account.move.line', 'account_id', string='Related Move Lines')