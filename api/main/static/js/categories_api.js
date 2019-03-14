/*
Sources:
--> https://www.w3schools.com/js/js_ajax_intro.asp
--> https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/

*/

const categories_url = "http://127.0.0.1:8000/api/v1/categories/"

const categories = document.getElementById('categories');

const select = document.getElementById('category');

const list = document.createElement("div");
list.setAttribute("class", "categories");

categories.appendChild(list);

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest();

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', categories_url, true);

request.onload = function () {
  // Begin accessing JSON data here
var data = JSON.parse(this.response);

if (request.status >= 200 && request.status < 400) {
  data.forEach(category => {

    // in header
    const li = document.createElement('li');
    li.textContent = category.name;
    list.appendChild(li);

    // in form
    if (select) {
    const option = document.createElement('option');
    option.value = category.id;
    option.textContent = category.name;
    select.appendChild(option);
  }
    // console.log(category.name);
    // console.log(category.slug);
    // console.log(category.videos);
  });
} else {
  const errorMessage = document.createElement('div');
  errorMessage.textContent = `Gah, it's not working!`;
  app.appendChild(errorMessage);
  console.log('error');
  }

}

// Send request
request.send();
