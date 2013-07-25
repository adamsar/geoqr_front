#Basic error reporting for GeoQR
MESSAGES = {
  INVALID_LOGIN: "Invalid login"
  CODE_NOT_READABLE: "Code not readable"
  BAD_LOCATION: "Not close enough to location"
  }
  
class ErrorNotifier
  display: (msg) ->
    if msg
      $.mobile.showPageLoadingMsg $.mobile.pageLoadErrorMessageTheme, msg, true
      setTimeout $.mobile.hidePageLoadingMsg, 3000
    
  constructor: (@msgs) ->
    @display (MESSAGES[msg] for msg in @msgs).join("<br/>")

    
