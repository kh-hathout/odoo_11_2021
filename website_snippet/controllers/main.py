# © 2019 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.http import Controller, route
from odoo.addons.web.controllers.main import Binary


class WebsiteSnippet(Controller):

    @route(
        '/website_snippet/thumbnail/<int:sid>',
        type='http',
        auth='user',
        website=True,
    )
    def website_snippet_thumbnail(self, sid, **kw):
        kw['model'] = 'website_snippet.snippet'
        kw['field'] = 'thumbnail_small'
        kw['id'] = sid

        return Binary().content_image(**kw)
