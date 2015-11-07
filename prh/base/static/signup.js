'use strict';
document.addEventListener('DOMContentLoaded', function() {
    function hideElm (elm) {
        elm.classList.add("hidden");
    }

    function showElm (elm) {
        elm.classList.remove("hidden");
    }

    var loginContainer = document.getElementById("meetup-login-container");
    var loginForm = document.getElementById("meetup-form");


    function getUrlParameter(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
            results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }

    (function(window, bRequest) {
        var btn = document.getElementById("login-with-meetup");
     
        btn.addEventListener("click", function () {
            var url = "https://secure.meetup.com/oauth2/authorize";
            url += "?client_id=svpri4nnnk6dgqc8gnpvuo0uk4";
            url += "&response_type=code";
            url += "&redirect_uri=" + window.MEETUP_REDIRECT_URI;
            window.location.href = url;
        });

        var code = getUrlParameter('code');
        if (!!code) {
            hideElm(loginContainer)
            showElm(loginForm)
            // loginWithMeetup(code);
            document.getElementById("id_meetup_code").value = code;
        } else {
            hideElm(loginForm)
            showElm(loginContainer)
        }


    })(window, window.bRequest);
});
