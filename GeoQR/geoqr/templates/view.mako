<%inherit file="base.mako" />

<%block name="left_buttons">
<a href="/list" data-icon="arrow-l">Back</a>
</%block>

<%block name="title">
記載
</%block>

<%block name="content">
<div class="text-centered info">
${info}
</div>
% if canValidate:
<a href="/redeem?location=${id}" data-role="button" data-icon="check">まとめ</a>
% else:
<div class="redeemed">もうまとめられました</div>
% endif
</%block>
