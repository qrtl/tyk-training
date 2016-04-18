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

from openerp import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.multi
    @api.depends('origin')
    def _get_sale_order(self):
        for pick in self:
            pick.sale_order_id = 0
            pick.sale_order_id = self.env['sale.order'].search([('name', '=', pick.origin)], limit=1)

    sale_order_id = fields.Many2one('sale.order', compute='_get_sale_order', string="Sale Order", readonly=True)
    project_id = fields.Many2one('account.analytic.account', related='sale_order_id.project_id', string="Contract / Analytic", store=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
