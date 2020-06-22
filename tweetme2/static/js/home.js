
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




function handleTweetCreateFormError( msg, display){
    var myErrorDiv = document.getElementById('tweet-create-form-error')

    if (display === true){
        myErrorDiv.setAttribute("class", "alert alert-danger")
        myErrorDiv.innerText = msg;
    }
    else{
        myErrorDiv.setAttribute("class", "d-none alert alert-danger")
    }
}



function handleTweetCreateFormDidSubmit(event){
    event.preventDefault();
    const myForm = event.target
    const myFormData = new FormData(myForm)
    const url = myForm.getAttribute("action")
    const method = myForm.getAttribute('method')
    const xhr = new XMLHttpRequest()
    const responseType = 'json'
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function(){
        if(xhr.status === 201){
            handleTweetCreateFormError("", false)
            const newTweetJSON = xhr.response
            const newTweetElement = formatTweetElement(newTweetJSON)
            console.log(newTweetElement)
            const ogHTML = tweetsContainerElement.innerHTML
            tweetsContainerElement.innerHTML = newTweetElement + ogHTML;
            myForm.reset()
        }
        else if (xhr.status === 400){
            const errorJson = xhr.response
            const contentError = errorJson.content
            let contentErrorMsg;
            if (contentError){
                contentErrorMsg = contentError[0];
                if (contentErrorMsg){
                    handleTweetCreateFormError(contentErrorMsg, true);
                }
                else {
                    alert("An error has occured")
                }
            }
            else {
                alert("An error Occured, Please try again")
            }
            console.log(contentErrorMsg)
        }
        else if (xhr.status === 401){
            alert("You must Login")
            window.location.href = '/login'
        }
        else if (xhr.status === 403){
            alert("You Are not authorized please, Login")
            window.location.href = '/login'
        }
        else if(xhr.status === 500){
            const errorJson = xhr.response
            alert(errorJson)
        }
    }
    xhr.onerror = function(){
        alert("An error Occured, Please Try")
    }
    xhr.send(myFormData)
}

const tweetCreateFormEL = document.getElementById("tweet-create-form")
tweetCreateFormEL.addEventListener("submit", handleTweetCreateFormDidSubmit);

const tweetsContainerElement = document.getElementById("tweets")

function loadTweets(tweetsElement){
    const xhr = new XMLHttpRequest
    const method = 'GET'
    const url = "/tweets"
    const responseType = 'json';

    xhr.responseType = responseType;
    xhr.open(method, url)
    xhr.onload = function(){
        const serverResponse = xhr.response;
        const listedItems = serverResponse;
        var finalTweetStr = "";
        var i;
        for(i=0;i<listedItems.length; i++){
            var tweetObj = listedItems[i];
            var currentItem = formatTweetElement(tweetObj);
            finalTweetStr += currentItem;

        }
    tweetsElement.innerHTML = finalTweetStr;
    }   
    xhr.send()
}
loadTweets(tweetsContainerElement);

function handleDidActionBtn(tweet_id, currentCount, action){
    console.log(tweet_id, currentCount)
    const url = '/api/tweets/action/'
    const method =  'POST'
    const data = JSON.stringify({
        id: tweet_id,
        action: action
    })
    const xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
    xhr.onload = function(){
        loadTweets(tweetsContainerElement)
    }
    xhr.send(data)
}   

function LikeBtn(tweet){
    return "<button class='btn btn-primary btn-sm' onclick='handleDidActionBtn(" +tweet.id+ ","+ tweet.likes+",'like')>Like " + tweet.likes + "</button>"
}

function UnLikeBtn(tweet){
    return "<button class='btn btn-outline-primary btn-sm' onclick='handleDidActionBtn(" +tweet.id+ ","+ tweet.likes+",'unlike')>Unlike</button>"
}


function RetweetBtn(tweet){
    return "<button class='btn btn-outline-success btn-sm' onclick='handleDidActionBtn(" +tweet.id+ ","+ tweet.likes+",'retweet')>Retweet</button>"
}

function formatTweetElement(tweet){
    var formattedTweet = "<div class='col-12 col-md-10 border rounded py-3 mb-4' id='" +
     tweet.id + "'><p>" + tweet.content +
            "</p><div class='btn-group'>" +
                LikeBtn(tweet) +
                UnLikeBtn(tweet)+
                RetweetBtn(tweet)+
             "</div></div>";
    return formattedTweet;
}
