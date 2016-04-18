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

from openerp import models, fields

class TestModel(models.Model):
    _name = "test.model"

    test_char = fields.Char(string="Test Character", required=True, translate=True)
    test_boolean = fields.Boolean(string="Test Boolean", help="either True or False")
    test_selection = fields.Selection([('select1', 'Select1'), ('select2', 'Select2'), ('select3', 'Select3')], string="Test Selection")
    test_text = fields.Text(string="Test Text")
    test_integer = fields.Integer(string="Test Integer")
    test_date = fields.Date(string="Test Date")
    
