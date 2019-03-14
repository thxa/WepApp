/*
Sources:

--> https://www.w3schools.com/js/
--> https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/

*/

// var categories = "http://127.0.0.1:8000/api/v1/categories/"
const videos = "http://127.0.0.1:8000/api/v1/videos/"
// var category_d = "http://127.0.0.1:8000/api/v1/categories/%{id}/"
// var video_d = "http://127.0.0.1:8000/api/v1/videos/%{id}/"

// const app = document.getElementById('app');

const name = document.getElementsByName('name')[0].value;
const photo_url = document.getElementsByName('photo_url')[0].value;
const url = document.getElementsByName('url')[0].value;
const category = document.getElementsByName('category')[0].value;

const video = {
   "name": name,
   "photo_url": photo_url,
   "url": url,
   "category": category
}

function save() {
  console.log(name);
}

// // Create a request variable and assign a new XMLHttpRequest object to it.
// var request = new XMLHttpRequest();
//
// // Open a new connection, using the` GET request on the URL endpoint
// request.open('POST', videos, true);
//
// request.onload = function () {
// // Begin accessing JSON data here
// var data = JSON.parse(this.response);
// if (request.status >= 200 && request.status < 400) {
//   data.forEach(video => {
//
//   });
// } else {
//   const errorMessage = document.createElement('div');
//   errorMessage.textContent = `Gah, it's not working!`;
//   app.appendChild(errorMessage);
//   console.log('error');
//   }
//
// }

// Send request
request.send();



/*
Json Post to api
     {
        "name": "",
        "photo_url": "",
        "url": "",
        "category": 1
    }
*/
