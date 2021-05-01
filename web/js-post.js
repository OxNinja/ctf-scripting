/* This script is cool to send asynchronous POST requests to a given URI
*/

URI = "http://localhost/register";

var send = async (username, password) => {
    headers = {
        'Content-Type': 'application/json'
    }

    body = {
        username: username,
        password: password
    }

    request = await fetch(URI, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(body)
    });

    console.log(request);
}

send('admin', 'p4ssw0rd');