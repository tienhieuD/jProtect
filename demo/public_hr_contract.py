from .jprotect_hr_contract import *
from odoo import api, fields, models


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    x_menu_category_id = fields.Many2one('x.menu.category', 'Menu Category')

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        return jprotect_cm_IrUiMenu_read(self, fields= fields, load= load, IrUiMenu= IrUiMenu, )

class MenuCategory(models.Model):
    _name = 'x.menu.category'

    sequence = fields.Integer()
    name = fields.Char(required=1)

    @api.model
    def get_sorted_category(self, ids):
        return jprotect_cm_MenuCategory_get_sorted_category(self, ids, MenuCategory= MenuCategory, )
