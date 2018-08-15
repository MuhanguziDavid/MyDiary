function set_cookie(cookie_name, cookie_value, exdays) {
    var date = new Date();
    date.setTime(date.getTime()+ (exdays*24*60*60*1000));
    expires = date.toGMTString();
    document.cookie = cookie_name + "=" + cookie_value + ";expires=" + expires + ";path=/";
}

function get_cookie(cookie_name) {
    var name = cookie_name + "=";
    var decoded_cookie = decodeURIComponent(document.cookie);
    var many_cookies = decoded_cookie.split(';');
    for(var i = 0; i < many_cookies.length; i++) {
        var single_cookie = many_cookies[i];
        while (single_cookie.charAt(0) === ' ') {
            single_cookie = single_cookie.substring(1,single_cookie.length);
        }
        if (single_cookie.indexOf(name) === 0) {
            return single_cookie.substring(name.length, single_cookie.length);
        }
    }
    return "";
}

function check_cookie(){
    var username = get_cookie("username");
    if (username != ""){
        alert("Welcome " + username);
    }else{
        username = prompt("please enter your username:", "");
        if (username != "" && username != null){
            set_cookie("username", username, 1);
        }
    }
}
