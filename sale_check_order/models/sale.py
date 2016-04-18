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

class sale_order(osv.osv):
    _inherit = "sale.order"

    _columns = {
        'check_order': fields.boolean('Order Received', help="Flagged when receive order from Customer")
    }

#        'check_order': fields.boolean('Order Received', readonly=True, help="Flagged when receive order from Customer")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
