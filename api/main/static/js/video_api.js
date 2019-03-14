/*
Sources:

--> https://www.w3schools.com/js/
--> https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/

*/

// var categories = "http://127.0.0.1:8000/api/v1/categories/"
var videos = "http://127.0.0.1:8000/api/v1/videos/"
//
// var category_d = "http://127.0.0.1:8000/api/v1/categories/%{id}/"
// var video_d = "http://127.0.0.1:8000/api/v1/videos/%{id}/"

const app = document.getElementById('app');

const blocks = document.createElement('div');
blocks.setAttribute('class', 'blocks')

const block = document.createElement('div');
block.setAttribute('class', 'block');

const name = document.createElement("div");
// name.setAttribute('class', 'title');
name.textContent = "name";

app.appendChild(blocks);

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', videos, true);

request.onload = function () {
// Begin accessing JSON data here
var data = JSON.parse(this.response);

if (request.status >= 200 && request.status < 400) {
  data.forEach(video => {

    const block = document.createElement('div');
    block.setAttribute('class', 'block');
    // block.style = "background-image: url(" + video.photo_url + ")" // https://www.w3schools.com/css/css_background.asp

    const name = document.createElement("div");
    name.setAttribute('class', 'title');
    name.textContent = video.name;

    const img = document.createElement("img");
    img.setAttribute('class', 'img');
    img.src = video.photo_url;

    const url = document.createElement("a");
    url.setAttribute('class', 'video');
    // url.target = "_blank";
    url.href = video.url;

    url.appendChild(name);
    // block.appendChild(img);
    url.appendChild(img)
    block.appendChild(url);
    blocks.appendChild(block);
    console.log(video.category);
    console.log(video.slug);
  });
} else {
  const errorMessage = document.createElement('div');
  errorMessage.setAttribute('class', 'error');
  errorMessage.textContent = `Gah, it's not working!`;
  app.appendChild(errorMessage);
  console.log('error');
  }

}

// Send request
request.send();
