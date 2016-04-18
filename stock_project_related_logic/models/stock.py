# -*- coding: utf-8 -*-
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016 Rooms For (Hong Kong) Limited T/A OSCG
#    <https://www.odoo-asia.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp.osv import fields, osv

class stock_picking(osv.osv):
    _inherit = "stock.picking"

    def _get_sale_order(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for picking in self.browse(cr, uid, ids, context=context):
            res[picking.id] = self.pool.get('sale.order').search(cr, uid, [('name', '=', picking.origin)], limit=1)
        return res

    _columns = {
        'sale_order_id': fields.function(_get_sale_order, string="Sale Order", type='many2one', relation='sale.order', method=True, readonly=True),
#        'project_id': fields.related('sale_order_id', 'project_id', string="Contract / Analytic", type='many2one', relation='account.analytic.account'),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
