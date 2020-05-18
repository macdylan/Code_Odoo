# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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
#
##############################################################################

from odoo import fields, models, SUPERUSER_ID

class lang(models.Model):
    _inherit = "res.lang"
    
    def init(self):
        res = False
        langs = self.search([('code','=','vi_VN')])
        
        if langs:
            write_args = {'grouping': '[3,3,3]'}
            res = langs.write(write_args)
            
        return res
lang()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
