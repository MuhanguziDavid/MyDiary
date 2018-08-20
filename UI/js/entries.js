function add_an_entry(){
    var url = host_name + "/api/v1/entries";
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'authorization':'Bearer '+get_cookie("auth_token")
        },
        body: JSON.stringify({
            "title": document.getElementById("entryTitle").value,
            "description": document.getElementById("entryDetails").value,
        })
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        if(data.message == "Entry has been created"){
            alert("Entry created successfully");
            console.log(data);
        }else{
            console.log(data.message);
        }
    })
    .catch(function(error){
        console.log(error);
    });
}

function get_all_entries(){
    var url = host_name + "/api/v1/entries";
    fetch(url, {
        method: 'GET',
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
            entries = data.entries;
            entries_list = "";
            for(var i=0; i<entries.length; i++){
                entries_list += `
                    <li>
                        <b><a href="#" onclick="get_an_entry(${entries[i]["entry_id"]})">${entries[i]["title"]}</a></b>
                        <br/>creation_time: ${entries[i]["creation_time"]}
                    </li>
                `;
            }
            document.getElementById("all_entries").innerHTML = entries_list;
        }else{
            console.log(data);
        }
    })
    .catch(function(error){
        console.log(error);
    });
}

function edit_an_entry(entry_id){
    var url = host_name + "/api/v1/entries/"+entry_id;
    fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'authorization':'Bearer '+get_cookie("auth_token")
        },
        body: JSON.stringify({
            "title": document.getElementById("entryTitle").value,
            "description": document.getElementById("entryDetails").value,
        })
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        if(data.message == "Entry has been created"){
            alert("Entry created successfully");
            console.log(data);
        }else{
            console.log(data.message);
        }
    })
    .catch(function(error){
        console.log(error);
    });
}
