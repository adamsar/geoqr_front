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
    var fullLink = "http://zxing.appspot.com/scan?ret=";
    fullLink +=  encodeURIComponent("http://ec2-54-249-136-165.ap-northeast-1.compute.amazonaws.com/doScan?q={CODE}&lat=" + position.coords.latitude + "&lon" + position.coords.longitude);
    $("#scanLink").attr("href", fullLink);
    $(".info").remove();
    $(".hidden").show();
  }
</script>

<div data-role="fieldcontain">
  <div class="text-centered">
    <div class="info">
      現地を教える許可をあげてください
    </div>
    <a data-role="button" class="hidden" id="scanLink" href="#">スキャン</a>
  </div>
</div>

</%block>
