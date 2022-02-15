$("#id_cep").change(function () {
  const url = "/clinica/buscar_endereco/"  // get the url of the `load_cities` view
  const cep = $(this).val();  // get the selected country ID from the HTML input
  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
    data: {
      'cep': cep       // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_cities` view function
      $("#id_logradouro").val(data[0].logradouro).prop("disabled", true);
      $("#id_bairro").val(data[0].bairro).prop("disabled", true);
      $("#id_cidade").val(data[0].cidade).prop("disabled", true);
      $("#id_estado").val(data[0].estado).prop("disabled", true);
      $("#submit-form").prop("disabled", true);
    },
    error: function(data){
      $("#id_logradouro").val("").prop("disabled", false);
      $("#id_bairro").val("").prop("disabled", false);
      $("#id_cidade").val("").prop("disabled", false);
      $("#id_estado").val("").prop("disabled", false);
      $("#submit-form").prop("disabled", false);
    }
  });
});