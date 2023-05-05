// index page js
const url = "http://127.0.0.1:8000/"

// ----- on site load -----
let username = get_cookie("username")
if (!!username){
    document.getElementById("username-input").value = username;
}

// ----- actions -----
document



// ------ functions -----


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


async function login(retry = 0){
    // re-hide error
    document.getElementById("username-error").style.display = "none";
    if (retry >= 2){
        console.log("Failed to connect.");
        return;
    }

    let inputText = document.getElementById("username-input").value;
    let key = get_cookie("key");

    // save provided username to cookie TODO: Provide date for expiry
    document.cookie = "username=" + inputText;
    
    // attempt connection, fetch key if needed
    let response = await fetch(url+"username/",{
        method: "POST",
        headers: {
            'accept': 'application/json',
            'key': key,
            'content-type': "application/json"
        },
        body: JSON.stringify({"name":inputText,"key":key})
    });
    
    switch (response.status) {
        case 200:
            console.log("Success!");
            break;
        case 401:
        case 403:
            await get_key();
            login(retry + 1);
            break;
        default:
            login_error("Unknown error occured, maybe the server is down. Code "+response.status);
    }

    // now handle if the username is incorrect
    %TODO
}


/**
 * Sets error message below the username field
 * @param {string} msg 
 */
function login_error(msg){
    let errorbox = document.getElementById("username-error");
    errorbox.innerText = msg;
    errorbox.style.display = "block";
}


/**
 * Requests key from the API, saves it into cookies
 * @returns string of the new key
 */
async function get_key(){
    let response = await fetch(url+"key/", {method:"GET"});
    let data = await response.json();
    key = data.key;
    console.log("new key: "+key);
    document.cookie = "key=" + key;
    return "";

}

function validate_username(name){
    if (length(name) >= 3 || length(name) <= 20){
        return true;
    }
    return false;
}
