<%inherit file="base.mako" />

<%block name="header">
ログイン
</%block>

<%block name="content">

<form data-ajax="false" action="/doLogin" method="POST">

  メールアドレス <input type="text" name="email" />
  パスワード <input type="password" name="password" />
  <input type="submit" value="Login" /> 

</form>

</%block>
