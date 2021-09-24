# -*- coding: utf-8 -*-
import werkzeug
import json
import base64

import odoo.http as http
from odoo.http import request
from odoo import SUPERUSER_ID

from odoo.addons.survey.controllers.main import WebsiteSurvey
from odoo.addons.web.controllers.main import binary_content

class WebsiteSurvey(WebsiteSurvey):

    @http.route(
        ["/web/binary/download/<int:file_id>"],
        type='http', auth="public", website=True, sitemap=False)
    def binary_download(self, file_id=None, **post):
        if file_id:
            binary_file = request.env['survey.binary'].browse([file_id])
            if binary_file:
                status, headers, content = binary_content(model='survey.binary', id=binary_file.id, field='binary_data', filename_field=binary_file.binary_filename, env=request.env(user=SUPERUSER_ID))
                content_base64 = base64.b64decode(content) if content else ''
                headers.append(('Content-Type', 'application/octet-stream'))
                headers.append(('Content-Length', len(content_base64)))
                headers.append(('Content-Disposition', 'attachment; filename=' + binary_file.binary_filename + ';'))
                return request.make_response(content_base64, headers)
        return False


    @http.route(['/survey/submit/<model("survey.survey"):survey>'], type='http', methods=['POST'], auth='public', website=True)
    def submit(self, survey, **post):
        page_id = int(post['page_id'])
        questions = request.env['survey.question'].search([('page_id', '=', page_id), ('type', '=', 'upload_file')])

        for question in questions:
            answer_tag = "%s_%s_%s" % (survey.id, page_id, question.id)
            post[answer_tag] = request.httprequest.files.getlist(answer_tag)
        return super(WebsiteSurvey, self).submit(survey, **post)


    @http.route(['/survey/prefill/<model("survey.survey"):survey>/<string:token>',
                 '/survey/prefill/<model("survey.survey"):survey>/<string:token>/<model("survey.page"):page>'],
                type='http', auth='public', website=True)
    def prefill(self, survey, token, page=None, **post):
        json_prefill = super(WebsiteSurvey, self).prefill(survey, token, page=page, **post)
        UserInputLine = request.env['survey.user_input_line']
        ret = {}

        # Fetch previous answers
        if page:
            previous_answers = UserInputLine.sudo().search([('user_input_id.token', '=', token), ('page_id', '=', page.id)])
        else:
            previous_answers = UserInputLine.sudo().search([('user_input_id.token', '=', token)])

        for answer in previous_answers:
            if not answer.skipped:
                answer_tag = '%s_%s_%s' % (answer.survey_id.id, answer.page_id.id, answer.question_id.id)
                answer_value = None
                if answer.answer_type == 'upload_file':
                    answer_value = [("/web/binary/download/%s" % (file.id), file.binary_filename) for file in answer.user_binary_line]
                    if answer_value:
                        ret.setdefault(answer_tag, []).append(answer_value)

        json_prefill = json.loads(json_prefill.get_data().decode('utf-8'))
        json_prefill.update(ret)
        return json.dumps(json_prefill)