# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging

import requests
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

API_ENDPOINT = 'https://api.twitter.com'
API_VERSION = '1.1'
REQUEST_TOKEN_URL = '%s/oauth2/token' % API_ENDPOINT
REQUEST_FAVORITE_LIST_URL = '%s/%s/favorites/list.json' % (API_ENDPOINT, API_VERSION)
URLOPEN_TIMEOUT = 10




class MecTwitter(models.Model):

    _inherit = 'event.event'

    twitter_api_key = fields.Char(string='Twitter API key', help='Twitter API Key')
    twitter_api_secret = fields.Char(string='Twitter API secret', help='Twitter API Secret')
    twitter_screen_name = fields.Char(string='Get favorites from this screen name')

    @api.model
    def _request(self, event, url, params=None):
        """Send an authenticated request to the Twitter API."""
        access_token = self._get_access_token(event)
        try:
            request = requests.get(url, params=params, headers={'Authorization': 'Bearer %s' % access_token}, timeout=URLOPEN_TIMEOUT)
            request.raise_for_status()
            return request.json()
        except requests.HTTPError as e:
            _logger.debug("Twitter API request failed with code: %r, msg: %r, content: %r",
                          e.response.status_code, e.response.reason, e.response.content)
            raise

    @api.model
    def _refresh_favorite_tweets(self):
        ''' called by cron job '''
        event = self.env['event.event'].search([('twitter_api_key', '!=', False),
                                          ('twitter_api_secret', '!=', False),
                                          ('twitter_screen_name', '!=', False)])
        _logger.debug("Refreshing tweets for event IDs: %r", event.ids)
        event.fetch_favorite_tweets()

    @api.multi
    def fetch_favorite_tweets(self):
        WebsiteTweets = self.env['mec.twitter.tweet']
        tweet_ids = []
        for event in self:
            if not all((event.twitter_api_key, event.twitter_api_secret, event.twitter_screen_name)):
                _logger.debug("Skip fetching favorite tweets for unconfigured website %s", event)
                continue
            params = {'screen_name': event.twitter_screen_name}
            last_tweet = WebsiteTweets.search([('event_id', '=', event.id),
                                                     ('screen_name', '=', event.twitter_screen_name)],
                                                     limit=1, order='tweet_id desc')
            if last_tweet:
                params['since_id'] = int(last_tweet.tweet_id)
            _logger.debug("Fetching favorite tweets using params %r", params)
            response = self._request(event, REQUEST_FAVORITE_LIST_URL, params=params)
            for tweet_dict in response:
                tweet_id = tweet_dict['id']  # unsigned 64-bit snowflake ID
                tweet_ids = WebsiteTweets.search([('event_id', '=', event.id),('tweet_id', '=', tweet_id)]).ids
                if not tweet_ids:
                    new_tweet = WebsiteTweets.create(
                            {
                              'event_id': event.id,
                              'tweet': json.dumps(tweet_dict),
                              'tweet_id': tweet_id,  # stored in NUMERIC PG field
                              'screen_name': event.twitter_screen_name,
                            })
                    _logger.debug("Found new favorite: %r, %r", tweet_id, tweet_dict)
                    tweet_ids.append(new_tweet.id)
        return tweet_ids

    def _get_access_token(self, event):
        """Obtain a bearer token."""
        r = requests.post(
            REQUEST_TOKEN_URL,
            data={'grant_type': 'client_credentials',},
            auth=(event.twitter_api_key, event.twitter_api_secret),
            timeout=URLOPEN_TIMEOUT,
        )
        r.raise_for_status()
        data = r.json()
        access_token = data['access_token']
        return access_token
