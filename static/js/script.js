$(document).ready(function() {
  $('form').submit(function (e) {
    $.ajax({
        type: "POST",
        url: '/auth',
        dataType: 'json',
        data: $('form').serialize(), // serializes the form's elements.
        success: function (data) {
            console.log(data)  // display the returned data in the console.

        }
    });
    e.preventDefault(); // block the traditional submission of the form.
  });
});
