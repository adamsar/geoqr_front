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
          function handle_errors(error)
          {
          }
          function handle_geolocation_query(position){
	    $("input[name=lat]").val(position.coords.latitude);
	    $("input[name=lon]").val(position.coords.longitude);
	    $("fieldset").html('<label for="code">写真撮影</label>' +
	  '<input type="file" name="code" accept="image/*" capture="camera"><br/>' +
	  '<input data-role="button"  type="submit" value="確認"/>');

          }
      </script>

<div data-role="fieldcontain">
  <div class="text-centered"
  <form action="/doScan" method="POST" data-ajax="false"
	accept-charset="utf-8"
	enctype="multipart/form-data">
    <input type="hidden" name="lat"/>
    <input type="hidden" name="lon"/>
    <fieldset datarole="controlgroup">
      
      <label for="code" class="camera">
	現地を教える許可をあげてください
      </label>
    </fieldset>
  </form>
  </div>
</div>
</%block>
