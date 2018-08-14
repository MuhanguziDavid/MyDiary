function register_user(){
    var url = host_name + "/api/v1/auth/signup";
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "username": document.getElementById("username").value,
            "email": document.getElementById("email").value,
            "password": document.getElementById("password").value,
            "confirm_password": document.getElementById("confirm_password").value,
        })
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        if(data.message == "Account Created Successfully"){
            set_cookie("auth_token", data.auth_token, 1);
            window.location.href = "home.html";
            // post_login_message("Logged in Successfully, Welcome");
        }else{
            document.getElementById('signup_feedback').innerHTML = "Feedback: " + data.message;
            console.log("Feedback: ",data.message);
        }
    })
    .catch(function(error){
        console.log(error);
    });
}

function login_user(){
    var url = host_name + "/api/v1/auth/login";
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "username": document.getElementById("username").value,
            "password": document.getElementById("password").value,
        })
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        if(data.message == "Logged in Successfully"){
            let setthecookie = set_cookie("auth_token", data.auth_token, 1);
            //window.location.href = "home.html";
            console.log(setthecookie);
            //post_login_message("Logged in Successfully, Welcome");
        }else{
            document.getElementById('login_feedback').innerHTML = "Feedback: " + data.message;
            console.log("Feedback: ",data.message);
        }
    })
    .catch(function(error){
        console.log(error);
    });
}

// function post_login_message(){
//     document.getElementById('home_feedback').innerHTML = "welcome";
// }

function get_all_entries(){
    var url = host_name + "/api/v1/entries";
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8',
            'authorization':'Bearer '+get_cookie("auth_token")
        }
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        if(data.status == "success"){
            console.log(data);
        }else{
            console.log("Feedback: ",data);
        }
    })
    .catch(function(error){
        console.log(error);
    });
}
