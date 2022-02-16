$("#id_cep").change(function () {
  const url = "/clinica/buscar_endereco/"  
  const cep = $(this).val();  
  $.ajax({                       
    url: url,                    
    data: {
      'cep': cep       
    },
    success: function (data) {  
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