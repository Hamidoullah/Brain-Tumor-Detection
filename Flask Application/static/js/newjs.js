$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('#btn-predict').hide();  // Ensure the predict button is hidden initially

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imageUpload").change(function () {
        var file = this.files[0];
        var validTypes = ['image/jpeg', 'image/png', 'image/jpg'];
        if (validTypes.includes(file.type)) {
            $('.image-section').show();
            $('#btn-predict').show();
            $('#result').text('');
            $('.loader').hide();  // Hide loader when the file is selected
            $('#result').hide();  // Ensure result is hidden initially
            readURL(this);
        } else {
            alert("Veuillez télécharger une image valide (JPEG, PNG).");
            $('#imageUpload').val('');  // Clear the input field
        }
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                if (data == "Tumor") {
                    $('#result').text(' Résultat :  tumeur');
                } else {
                    $('#result').text(' Résultat :  sain');
                }
                console.log('Success!');
            },
            error: function (xhr, status, error) {
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text('Erreur de traitement. Veuillez réessayer.');
                console.log('Error:', error);
            }
        });
    });
});
