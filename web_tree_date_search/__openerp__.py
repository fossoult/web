# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2015 Noviat nv/sa (www.noviat.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

{
    'name': 'Tree dates search',
    'version': '3.0',
    'author': 'Noviat, Odoo Community Association (OCA)',
    'website': 'http://www.noviat.com',
    'license': 'AGPL-3',
    'category': 'Web',
    'depends': [
        'web',
    ],
    'data': [
        'views/assets_backend.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}
