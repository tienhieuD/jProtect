from odoo import api, fields, models


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    x_menu_category_id = fields.Many2one('x.menu.category', 'Menu Category')

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        if fields == ['name', 'sequence', 'parent_id', 'action', 'web_icon', 'web_icon_data']:
            fields.append('x_menu_category_id')
        return super(IrUiMenu, self).read(fields, load)


class MenuCategory(models.Model):
    _name = 'x.menu.category'

    sequence = fields.Integer()
    name = fields.Char(required=1)

    @api.model
    def get_sorted_category(self, ids):
        return self.browse(ids).sorted('sequence').ids


