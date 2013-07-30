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
    $(".info").remove();
    $(".hidden").show();
  }
</script>

<div data-role="fieldcontain">
  <div class="text-centered">

  <form action="/doScan" method="POST" data-ajax="false"
	accept-charset="utf-8"
	enctype="multipart/form-data">
    <input type="hidden" name="lat"/>
    <input type="hidden" name="lon"/>
    <div class="info">
      現地を教える許可をあげてください
    </div>

    <label for="code" class="hidden">
      写真取る
    </label>
    <input type="file" class="hidden" name="code" accept="image/*" capture="camera">
    <input type="submit" class="hidden" name="submit" value="提出" />
  </form>
  </div>
</div>

</%block>
