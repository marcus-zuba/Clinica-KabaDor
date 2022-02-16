$("#id_cep").change(function () {
  const url = "/clinica/buscar_endereco/";
  const cep = $(this).val();  
  $.ajax({                    
    url: url,                    
    data: {
      'cep': cep       
    },
    success: function (data) {   
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