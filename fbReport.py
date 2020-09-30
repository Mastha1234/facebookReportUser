latest version.

Install this script?
Ask a question, post a review, or report the script.
// ==UserScript==
// @name         Report fb
// @namespace    https://greasyfork.org/scripts/37908-report-fb/code/Report%20fb.user.js
// @version      1.0.2
// @description  Script report facebook lũ vô văn hoá chửi team bạn
// @author       You
// @match        *://*.facebook.com/BanHoiVozerTraLoi*
// @match        *://*.facebook.com/zoom.beatvn*
// @match        *://*.facebook.com/beatvn.quotes*
// @match        *://*.facebook.com/sakertuan*
// @match        *://*.facebook.com/groups/phongthutoibeatvn*
// @match        *://*.facebook.com/groups/kysuduongpho*
// @match        *://*.facebook.com/groups/780485565464752*
// @match        *://*.facebook.com/groups/phongtrutgianbeatvn*
// @match        *://*.facebook.com/groups/tuyettinhcocbeatvn*
// @match        *://*.facebook.com/groups/BEATGAMER*
// @match        *://*.facebook.com/pg/BanHoiVozerTraLoi*
// @match        *://*.facebook.com/groups/370023386751036*
// @match        *://apps.facebook.com/beat_vn*
// @run-at       document-start
// @require      https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js
// @require      https://greasyfork.org/scripts/37907-arrive-js/code/arrivejs.js?version=246397
// @grant        none
// ==/UserScript==
var intv;
//reports personal accounts
if(/sakertuan/i.test(window.location.href)){
    console.log('ok');
    $(document).arrive('._1yzl', function(){
        intv = setInterval(function(){$('._1yzl').click();},500);
        $(document).unbindArrive('._1yzl');
    });

    $(document).arrive('._54nc[href^="/ajax/nfx/start_dialog?story_location=profile_someone_else&reportable"] ._54nh', function(){
        clearInterval(intv);
        $('._54nc[href^="/ajax/nfx/start_dialog?story_location=profile_someone_else&reportable"] ._54nh').click();
        $(document).unbindArrive('._54nc[href^="/ajax/nfx/start_dialog?story_location=profile_someone_else&reportable"] ._54nh');
    });
    $(document).arrive('#nfxQuestionNamedaccount > label._55sh._5ww6._5p_b.uiInputLabelInput > span', function(){
        $('#nfxQuestionNamedaccount > label._55sh._5ww6._5p_b.uiInputLabelInput > span').click();
        $('._42ft._4jy0.layerConfirm').click();
        $(document).unbindArrive('#nfxQuestionNamedaccount > label._55sh._5ww6._5p_b.uiInputLabelInput > span');
    });

    $(document).arrive('#nfxQuestionNamedfake > label._55sh._5ww6._5p_b.uiInputLabelInput > span', function(){
        $('#nfxQuestionNamedfake > label._55sh._5ww6._5p_b.uiInputLabelInput > span').click();
        $('._42ft._4jy0.layerConfirm').click();
        $(document).arrive('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span', function(){
            setInterval(function(){$('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span').click();},500);
            $(document).unbindArrive('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span');
        });
        $(document).unbindArrive('#nfxQuestionNamedfake > label._55sh._5ww6._5p_b.uiInputLabelInput > span');
    });
}
//reports groups
if(/phongthutoibeatvn|kysuduongpho|nguoibuon.gio.9|phongtrutgianbeatvn|tuyettinhcocbeatvn|nguoibuongio.72|vutuananhautumn|nguyen.vanduc.79677/i.test(window.location.href)){
    console.log('ok 2');
    $(document).arrive('#pagelet_group_actions i', function(){
        intv = setInterval(function(){$('#pagelet_group_actions i').click();},500);
        $(document).unbindArrive('#pagelet_group_actions i');
    });

    $(document).arrive('._54nc[href^="/ajax/report.php"] span', function(){
        clearInterval(intv);
        $('._54nc[href^="/ajax/report.php"] span').click();
        $(document).unbindArrive('._54nc[href^="/ajax/report.php"] span');
    });
    $(document).arrive('#nfxQuestionNamedhate span', function(){
        $('#nfxQuestionNamedhate span').click();
        $('#nfx_dialog_continue').click();
        $(document).unbindArrive('#nfxQuestionNamedhate span');
    });
    $(document).arrive('#nfxQuestionNamedrace span', function(){
        $('#nfxQuestionNamedrace span').click();
        $('#nfx_dialog_continue').click();
        $(document).unbindArrive('#nfxQuestionNamedrace span');
    });
    $(document).arrive('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span', function(){
        setInterval(function(){$('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span').click();},500);
        $(document).unbindArrive('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span');
    });
}
//reports pages
if(/beatvn\.world|zoom\.beatvn|beatvn\.quotes|nguoibuongio.hanoi/i.test(window.location.href)){
    console.log('ok 3');
    $(document).arrive('._p._4jy0._4jy4', function(){
        intv = setInterval(function(){$('._p._4jy0._4jy4').click();},500);
        $(document).unbindArrive('._p._4jy0._4jy4');
    });

    $(document).arrive('.uiContextualLayer ul > li:nth-child(6) ._54nh', function(){
        clearInterval(intv);
        $('.uiContextualLayer ul > li:nth-child(6) ._54nh').click();
        $(document).unbindArrive('.uiContextualLayer ul > li:nth-child(6) ._54nh');
    });
    $(document).arrive('#nfxQuestionNamedharassment span', function(){
        $('#nfxQuestionNamedharassment span').click();
        $('#nfx_dialog_continue').click();
        $(document).unbindArrive('#nfxQuestionNamedharassment span');
    });
    $(document).arrive('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span', function(){
        setInterval(function(){$('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span').click();},500);
        $(document).unbindArrive('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span');
    });
}
if(/beat_vn/i.test(window.location.href)){
    console.log('ok 4');
    $(document).arrive('.fsm.fwn.fcg a[ajaxify^="/ajax/report.php"]', function(){
        intv = setInterval(function(){document.querySelector('.fsm.fwn.fcg a[ajaxify^="/ajax/report.php"]').click();},500);
        $(document).unbindArrive('.fsm.fwn.fcg a[ajaxify^="/ajax/report.php"]');
    });

    $(document).arrive('#nfxQuestionNamedinappropriate span', function(){
        clearInterval(intv);
        $('#nfxQuestionNamedinappropriate span').click();
        $('#nfx_dialog_continue').click();
        $(document).unbindArrive('#nfxQuestionNamedinappropriate span');
    });
    $(document).arrive('#nfxQuestionNamedhate span', function(){
        clearInterval(intv);
        $('#nfxQuestionNamedhate span').click();
        $('#nfx_dialog_continue').click();
        $(document).unbindArrive('#nfxQuestionNamedhate span');
    });
    $(document).arrive('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span', function(){
        setInterval(function(){$('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span').click();},500);
        $(document).unbindArrive('._16gh[ajaxify^="/ajax/feed/filter_action/nfx_action_execute?action_name=REPORT"] span');
    });
}
setTimeout(function(){location.reload(etTimeout(function(){location.reload();},300000);
