
function handleTweetCreateFormDidSubmit(event){
    event.preventDefault();
    const myForm = event.target
    const myFormData = new FormData(myForm)
    const url = myForm.getAttribute("action")
    const method = myForm.getAttribute('method')
    const xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.onload = function(){
        const serverResponse = xhr.response
        console.log(serverResponse)
        const tweetsEl = document.getElementById("tweets")
        loadTweets(tweetsEl);
    }
    xhr.send(myFormData)
}

const tweetCreateFormEL = document.getElementById("tweet-create-form")
tweetCreateFormEL.addEventListener("submit", handleTweetCreateFormDidSubmit);

const tweetsEl = document.getElementById("tweets")

function loadTweets(tweetsElement){
    const xhr = new XMLHttpRequest
    const method = 'GET'
    const url = "/tweets"
    const responseType = 'json';

    xhr.responseType = responseType;
    xhr.open(method, url)
    xhr.onload = function(){
        const serverResponse = xhr.response;
        const listedItems = serverResponse.response;
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
loadTweets(tweetsEl);

function handleDidLike(tweet_id, currentCount){
    console.log(tweet_id, currentCount)
}   

function LikeBtn(tweet){
    return "<button class='btn btn-primary btn-sm' onclick='handleDidLike(" +tweet.id+ ","+ tweet.likes+ ")'>Like " + tweet.likes + "</button>"
}

function formatTweetElement(tweet){
    var formattedTweet = "<div class='col-12 col-md-10 border rounded py-3 mb-4' id='" +
     tweet.id + "'><p>" + tweet.content +
            "</p><div class='btn-group'>" +
                LikeBtn(tweet) +
             "</div></div>";
    return formattedTweet;
}
