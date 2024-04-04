document.addEventListener("DOMContentLoaded", function () {
  $("#add_item").click(addItem);
  $("#remove_item").click(removeItem);
  $("#clear_list").click(clearList);

  function addItem() {
    $("UL.my_list").append("<li>Item</li>");
  }

  function removeItem() {
    $(".my_list li:last-child").remove();
  }

  function clearList() {
    $(".my_list").empty();
  }
});

