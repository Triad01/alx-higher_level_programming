const toggleHeader = () => {
  if ($("header").toggleClass("green")) {
    $("header").toggleClass("red");
  }
};

$("#toggle_header").click(toggleHeader);

