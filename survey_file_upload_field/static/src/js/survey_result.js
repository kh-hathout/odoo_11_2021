odoo.define('survey_file_upload_field.survey_result', function (require) {
'use strict';

require('web.dom_ready');
var survey = require('survey.survey');
var field_utils = require('web.field_utils');

var the_form = $('.js_surveyform');

if(!the_form.length) {
    return $.Deferred().reject("DOM doesn't contain '.js_surveyform'");
}

    var prefill_controller = the_form.attr("data-prefill");
    // Pre-filling of the form with previous answers
    function prefill(){
        if (! _.isUndefined(prefill_controller)) {
            var prefill_def = $.ajax(prefill_controller, {dataType: "json"})
                .done(function(json_data){
                    _.each(json_data, function(value, key){
                        // prefill of text/number/date boxes
                        var input = the_form.find(".form-control[name=" + key + "]");
                        if (input.attr('date')) {
                            // display dates in user timezone
                            var moment_date = field_utils.parse.date(value[0]);
                            value = field_utils.format.date(moment_date, null, {timezone: true});
                        }
                        input.val(value);
                        var file_input = the_form.find(".file_container[name=" + key + "]");
                        if (file_input.attr('file')) {
                            // display dates in user timezone
                            _.each(value[0], function(val){
                                file_input.append('<span class="col-md-12"><i class="fa fa-download"></i><a href="' + val[0] + '">' + val[1] + '</a></span>');
                            });
                        }

                        // special case for comments under multiple suggestions questions
                        if (_.string.endsWith(key, "_comment") &&
                            (input.parent().hasClass("js_comments") || input.parent().hasClass("js_ck_comments"))) {
                            input.siblings().find('>input').attr("checked","checked");
                        }

                        // checkboxes and radios
                        the_form.find("input[name^=" + key + "][type!='text']").each(function(){
                            $(this).val(value);
                        });
                    });
                })
                .fail(function(){
                    console.warn("[survey] Unable to load prefill data");
                });
            return prefill_def;
        }
    }

    // Launch prefilling
    prefill();
});
