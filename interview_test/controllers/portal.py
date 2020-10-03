# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import math
import re

from werkzeug import urls
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute
from odoo.addons.website_sale.controllers.main import QueryURL
from odoo.addons.website_sale.controllers import main
from odoo.addons.website.controllers.main import Website
from odoo.addons.web_editor.controllers.main import Web_Editor

from odoo import fields as odoo_fields, tools, http, _
from odoo.exceptions import ValidationError, AccessError, MissingError, UserError
from odoo.http import content_disposition, Controller, request, route
from odoo.tools import consteq
#from odoo.addons.portal.controllers.portal import CustomerPortal
import base64, binascii
from odoo.addons.base.models.res_partner import Partner
from _operator import or_
from odoo.addons.http_routing.models.ir_http import unslug

from odoo.fields import Integer
from odoo.addons.website_sale.controllers.main import QueryURL
from odoo import api, models, fields, _
from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression
from email.policy import default

import urllib
import urllib.request
import urllib.parse
import requests


# --------------------------------------------------
# Misc tools
# --------------------------------------------------

class  Website(Website):
    _inherit = 'website'


    
    @http.route(['/get_interview_test_form'], type='http', auth='public', website=True, sitemap=False)
    def get_interview_test_form(self, *args, **post):
      
        qcontext = request.params.copy()
        qcontext['st']=fields.Boolean(default=False)
        qcontext['customerlist']= request.env['res.partner'].sudo().search([])
        if post:
            print("post",post)
            name=post.get('name')
            mobile=post.get('mobile')
            selectedcustomer=post.get('cutomers')
            vals = {
                'name':name,
                'phone':mobile,  
                'partner_id':selectedcustomer, 
                'type':"lead",
                 }
            if vals:
                print("vals",vals)
                crm=request.env['crm.lead'].sudo().create(vals)
                if crm:
                    print("crm",crm)
                    qcontext['st']=True
            
           
        response=request.render("interview_test.portalpages", qcontext)
        response.headers['X-Frame-Options'] = 'DENY'
        return response

   

   
