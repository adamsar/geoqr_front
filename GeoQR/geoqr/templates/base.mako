<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <title>GeoQR</title>

    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.1/jquery.mobile-1.3.1.min.css" />
    <link rel="stylesheet" href="/static/style/geoqr.css" />
    <script src="http://code.jquery.com/jquery-1.8.3.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.3.1/jquery.mobile-1.3.1.min.js"></script>        
    <script src="/static/js/geoqr.js"></script>
    <script type="text/javascript">
      var errors = [];
      % if errors:
      % for error in errors:
        errors.push("${error}");
      % endfor 
      % endif
    </script>

  </head>

  <body>
      <div data-role="header">
	<%block name="left_buttons"/>
	<h1>
	  <%block name="title"/>
	</h1>
      </div>

      <div data-role="content">
	<%block name="content"/>
      </div>

      <!-- Notify users of the errors on the page -->
      <script type="text/javascript">
	$(document).ready(function(){
	  new ErrorNotifier(errors);
	});
      </script>
  </body>

</html>
