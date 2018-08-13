function setCookie(cookie_name, cookie_value, exdays) {
    var date = new Date();
    date.setTime(date.getTime()+ (exdays*24*60*60*1000));
    expires = date.toGMTString();
    document.cookie = cookie_name + "=" + cookie_value + ";expires=" + expires + ";path=/";
}


