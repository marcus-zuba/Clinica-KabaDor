$("#id_cep").change(function () {
  const url = "/clinica/buscar_endereco/"  // get the url of the `load_cities` view
  const cep = $(this).val();  // get the selected country ID from the HTML input
  $.ajax({                       // initialize an AJAX request
    url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
    data: {
      'cep': cep       // add the country id to the GET parameters
    },
    success: function (data) {   // `data` is the return of the `load_cities` view function
      $("#id_logradouro").val(data[0].logradouro);
      $("#id_bairro").val(data[0].bairro);
      $("#id_cidade").val(data[0].cidade);
      $("#id_estado").val(data[0].estado);
    },
    error: function(data){
      $("#id_logradouro").val("");
      $("#id_bairro").val("");
      $("#id_cidade").val("");
      $("#id_estado").val("");
    }
  });
});