function submit_user(){
    // var url = "http://127.0.0.1:5000/api/v1/auth/signup";
    fetch('http://127.0.0.1:5000/api/v1/auth/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=UTF-8'
        },
        body: JSON.stringify({
            "username": document.getElementById("username").value,
            "email": document.getElementById("email").value,
            "password": document.getElementById("password").value,
            "confirm_password": document.getElementById("confirm_password").value,
        })
    })
    // .then((response) => response.json())
    .then(function(response){
        return response.json()
    })
    .then(function(data){
        if(data.message == "Account Created Successfully"){
            window.location.href = "index.html";
        }else{
            console.log("Feedback: ",data.message);
        }
    })
    .catch(function(error){
        console.log(error);
    });
}
