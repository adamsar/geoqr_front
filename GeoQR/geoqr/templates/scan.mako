<%inherit file="base.mako" />

<%block name="left_buttons">
<a href="/actions" data-icon="arrow-l">Back</a>
</%block>

<%block name="title">
スキャン
</%block>

<%block name="content">
      <script>
          $(window).ready(function(){
            initiate_geolocation();
          });

          function initiate_geolocation() {
              navigator.geolocation.getCurrentPosition(handle_geolocation_query, handle_errors);
          }          

	  function handle_errors(error){	  
          }

          function handle_geolocation_query(position){
	    //Put the lat and long in their proper place
	    $("input[name=lat]").val(position.coords.latitude);
	    $("input[name=lon]").val(position.coords.longitude);
	    //And use a mini "template" to render a proper form
	    $("#form-container").html('' +
	      '<input type="file" name="code" accept="image/*" capture="camera"><br/>' +
	      '<a data-role="button" href="javascript:$(\'form\').submit();">Ok</a>');
          }
      </script>

<div data-role="fieldcontain">
  <div class="text-centered"

  <form action="/doScan" method="POST" data-ajax="false"
	accept-charset="utf-8"
	enctype="multipart/form-data">
    <input type="hidden" name="lat"/>
    <input type="hidden" name="lon"/>
      <div id="form-container">
	<label for="code" class="camera">
	  現地を教える許可をあげてください
	</label>
      </div>
  </form>
  </div>
</div>

</%block>
