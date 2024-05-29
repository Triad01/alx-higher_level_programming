$.ajax({
  url: "https://swapi-api.alx-tools.com/api/films/?format=json",
  method: "GET",
  success: function (response) {
    for (const movie of response.results) {
      $("UL#list_movies").append("<li>" + movie.title + "</li>");
    }
  },
});
