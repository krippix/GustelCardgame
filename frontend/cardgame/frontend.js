const url = "http://127.0.0.1:8000/"

console.log("Starting");

get_test();

async function get_test(){
    let response = await fetch(url,{method: "GET"});
    let data = await response.json();
    console.log(data);
}

async function set_username(){
    var inputText = document.getElementById("input-field").value;
    document.cookie = "username=" + inputText
    let response = await fetch(url,{
        method: "POST",
        headers: {
            'Content-Type': "application/json",
            'Accept': 'application/json'
        },
        body: JSON.stringify({name:inputText, desc: "dein mamaer"})
    })
    console.log(await response.json());
}