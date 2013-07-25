<%inherit file="base.mako" />

<%block name="left_buttons">
<a href="/actions" data-icon="arrow-l">戻</a>
</%block>

<%block name="title">
新規記載
</%block>

<%block name="content">
<h2>新規記載を追加</h2>
<form action="/doAdd" method="POST" data-ajax="false">
  住所 <input type="text" name="address"/>
  コード／タイトル <input type="text" name="code" />
  情報 <textarea name="info">コード褒美</textarea>
    <input type="submit" value="作成" />
</form>
</%block>
