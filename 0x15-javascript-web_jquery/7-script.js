//fetching name of API data and displaying
//it in DIV#character
let url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
$.get(url, function (data, stat){
    $('DIV#character').text(data.name);
});