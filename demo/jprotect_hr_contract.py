from odoo import api, fields, models


def jprotect_cm_IrUiMenu_read(self, fields=None, load='_classic_read', IrUiMenu=None, ):
    if fields == ['name', 'sequence', 'parent_id', 'action', 'web_icon', 'web_icon_data']:
        fields.append('x_menu_category_id')
    return super(IrUiMenu, self).read(fields, load)


def jprotect_cm_MenuCategory_get_sorted_category(self, ids, MenuCategory=None, ):
    return self.browse(ids).sorted('sequence').ids




