// index page js
const url = "http://127.0.0.1:8000/"

// script
let username = get_cookie("username")
if (!!username){
    document.getElementById("input-field").value = username;
}


async function get_test(){
    let response = await fetch(url,{method: "GET"});
    let data = await response.json();
    console.log(data);
}


// cookies are ; seperated string
function get_cookie(name){
    var cookieArr = document.cookie.split(";");
    for (var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");
        if (name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null
}


async function set_username(){
    var inputText = document.getElementById("input-field").value;
    document.cookie = "name=" + inputText
    let response = await fetch(url+"username/",{
        method: "POST",
        headers: {
            'Content-Type': "application/json",
            'Accept': 'application/json'
        },
        body: JSON.stringify({name:inputText,key:""})
    })
    console.log(await response.json());
}


function validate_username(name){
    if (length(name) >= 3 || length(name) <= 20){
        return true;
    }
    return false;
}