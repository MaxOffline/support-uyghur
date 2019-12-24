function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
const Ajax =  (url, method, body) => {
    let response = undefined
    if(!body){
        response =  fetch(url, {
            headers: { "Content-Type": "application/json",'X-CSRFToken':csrftoken, "Accept": "application/json"},
            credentials: "include",
            mode: "same-origin",
            method,
        })
    }else{
        response =  fetch(url, {
            headers: { "Content-Type": "application/json",'X-CSRFToken':csrftoken, "Accept": "application/json"},
            credentials: "include",
            mode: "same-origin",
            method,
            body,
        })
    }
    
    return  response
}

window.onload = async () =>{

const response = await Ajax(/check-token/, "POST", JSON.stringify({"token":csrftoken}));
if (response.status === 200){
    document.getElementById("voteform").remove();
    document.getElementById("question").remove();
    document.getElementById("message").innerHTML = "<div> You've already voted, Thank you! </div>"
}

const votesReponse = await Ajax(/get-total-votes/, "GET");
let data = await votesReponse.json();
data = JSON.parse(data)

document.getElementById("total").innerHTML = "Total Votes: " + (data[0].fields.agree + data[0].fields.disagree)
document.getElementById("yes").innerHTML = "Total Yes: " + data[0].fields.agree 
document.getElementById("no").innerHTML = "Total No: " + data[0].fields.disagree

}

const handleSubmit =  async (event) => {
    event.preventDefault();
    let value = ""
    document.getElementsByName("status").forEach(input => {
        if (input.checked === true){
            value = input.defaultValue;
        }
    })

    const result = {
        "agree":0,
        "disagree":0
    }

    if (value === "agree"){
        result.agree = 1
    } else if (value === "disagree") {
        result.disagree = 1
    }
    const response = await Ajax(/vote/, "POST", JSON.stringify(result));
    if (response.status === 200) {
        await Ajax(/token/, "POST", JSON.stringify({token:csrftoken}));
        document.location.reload();
    } 


}



