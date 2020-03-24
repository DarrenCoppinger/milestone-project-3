var form = document.getElementsByTagName('form')[0],
    genre = document.getElementById('genre_name');

/*original code credit: "https://github.com/Code-Institute-Submissions/dhamma1991-milestone-project-3/" */
form.addEventListener("submit", function (event) {
    if (!genre.validity.valid) {
        $("#genre_name").removeClass("valid");
        $("#genre_name").addClass("invalid");
        $("#genre_name_label").addClass("active");
        $("#genre_name").prop("aria-invalid", "true");
        event.preventDefault();
        $('select').material_select();
    }


}, false);

