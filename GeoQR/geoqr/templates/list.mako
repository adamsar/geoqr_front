<%inherit file="base.mako" />

<%block name="title"> 
スキャンされた目録
</%block>

<%block name="left_buttons">
<a href="/actions" data-icon="arrow-l">戻</a>
</%block>

<%block name="content">
<ul data-role="listview">
  % for checkin in checkins:
  <li
     % if checkin['validated']:
       class="completed"
     % else:
     % if checkin['expired']:
       class="expired"
     % endif
     % endif
     >
    <a data-ajax="false" href="/view?id=${checkin['location']['id']}">
      ${checkin["location"]["code"]}
    </a>
  </li>
  % endfor
</ul>
</%block>
