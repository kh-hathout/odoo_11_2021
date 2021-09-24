# -*- coding: utf-8 -*-


import logging

import requests

from odoo import api, fields, models, _
from odoo.addons.http_routing.models.ir_http import slug

from odoo.exceptions import UserError



_logger = logging.getLogger(__name__)

class Event(models.Model):
    _name = 'event.event'
    _inherit = ['event.event', 'website.seo.metadata', 'website.published.mixin']

    twitter_api_key = fields.Char(
        string='API Key',
        help='Twitter API key you can get it from https://apps.twitter.com/')
    twitter_api_secret = fields.Char(
        string='API secret',
        help='Twitter API secret you can get it from https://apps.twitter.com/')
    twitter_tutorial = fields.Boolean(string='Show me how to obtain the Twitter API Key and Secret')
    twitter_screen_name = fields.Char(
        string='Favorites From',
        help='Screen Name of the Twitter Account from which you want to load favorites.'
             'It does not have to match the API Key/Secret.')

    def _get_twitter_exception_message(self, error_code):
        if error_code in TWITTER_EXCEPTION:
            return TWITTER_EXCEPTION[error_code]
        else:
            return _('HTTP Error: Something is misconfigured')

    def _check_twitter_authorization(self):
        try:
            self.event_id.fetch_favorite_tweets()

        except requests.HTTPError as e:
            _logger.info("%s - %s" % (e.response.status_code, e.response.reason), exc_info=True)
            raise UserError("%s - %s" % (e.response.status_code, e.response.reason) + ':' + self._get_twitter_exception_message(e.response.status_code))
        except IOError:
            _logger.info(_('We failed to reach a twitter server.'), exc_info=True)
            raise UserError(_('Internet connection refused') + ' ' + _('We failed to reach a twitter server.'))
        except Exception:
            _logger.info(_('Please double-check your Twitter API Key and Secret!'), exc_info=True)
            raise UserError(_('Twitter authorization error!') + ' ' + _('Please double-check your Twitter API Key and Secret!'))

    @api.model
    def create(self, vals):
        TwitterConfig = super(ResConfigSettings, self).create(vals)
        if vals.get('twitter_api_key') or vals.get('twitter_api_secret') or vals.get('twitter_screen_name'):
            TwitterConfig._check_twitter_authorization()
        return TwitterConfig

    @api.multi
    def write(self, vals):
        TwitterConfig = super(ResConfigSettings, self).write(vals)
        if vals.get('twitter_api_key') or vals.get('twitter_api_secret') or vals.get('twitter_screen_name'):
            self._check_twitter_authorization()
        return TwitterConfig
