<%inherit file="base.mako" />

<%block name="title">
アクション選択してください
</%block>

<%block name="content">
<ul data-role="listview" data-theme="d">
  <li>
    <a href="/scan">スキャン</a>
  </li>   
  <li>
    <a href="/list">スキャンされた目録</a>
  </li>
  <li>
    <a href="/addListing">新規記載</a>
  </li>
</ul>
</%block>
