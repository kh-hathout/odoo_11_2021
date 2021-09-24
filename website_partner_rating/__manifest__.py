# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Customer Review',
    'category': 'Website',
    'summary': 'Website Customet/Partner Rating',
    'website': 'www.browseinfo.in',
    'version': '11.0.0.1',
    'description': """
        You can see reviews details with Reviewer name, Rating, Date, Short & Long Description.User can submit their review only when 
    they are logged in. If the user is not logged in, then the system will provide link to login page and once after login user will
    straight away redirected to the partner page.
        You can publish/unpublish reviews from front end website page. For that you must be logged in as Administrator.
        You will able to see Avg. Rating and No. of reviews link at the top of partner detail page in website. By clicking on that you will redirect to reviews list.

        """,
    'license':'OPL-1',
    'author': 'BrowseInfo',
    'depends': ['website','website_crm_partner_assign','website_partner'],
    'installable': True,
    'data': [
        'views/template.xml',
        'views/mail_message_view.xml',
    ],
    'application': True,
    "images":['static/description/Banner.png'],
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
