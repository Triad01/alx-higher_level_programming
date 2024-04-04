$(document).ready(function () {
  // Function to fetch and display translation
  function fetchTranslation() {
    const languageCode = $("#language_code").val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.getJSON(apiUrl, function (data) {
      const helloMessage = data.hello;
      $("#hello").text(helloMessage);
    });
  }

  // Fetch translation when clicking the Translate button
  $("#btn_translate").click(fetchTranslation);

  // Fetch translation when pressing ENTER in the language code input field
  $("#language_code").keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
