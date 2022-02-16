$(document).ready(function() {
  const url = "/clinica/listar_especialidades/";
  const url2 = "/clinica/listar_medicos/";
  $.ajax({                      
    url: url,                  
    success: function (data) {   
      let html_data="";
      data.forEach(function (especialidade) {
        html_data += `<option value="${especialidade}">${especialidade}</option>`
      });
      $("#id_especialidade").html(html_data);
      const especialidade = $("#id_especialidade").val();  
      $.ajax({                      
        url: url2,
        data: {'especialidade': especialidade},                  
        success: function (data) {   
          let html_data="";
          data.forEach(function (medico) {
            html_data += `<option value="${medico.id}">${medico.nome}</option>`
          });
          $("#id_medico").html(html_data);
          atualizar_horarios();
        }
      });
    },
    error: function(data){
      $("#id_especialidade").html(`<option value="null">Não há especialidades cadastradas</option>`)
      $("#id_especialidade").prop("disabled", true)
      $("#id_medico").html(`<option value="null">Não há médicos cadastrados</option>`)
      $("#id_medico").prop("disabled", true)
      $("#submit-form").prop("disabled", true)
    }
  });
});

$("#id_especialidade").change(function () {
  const url = "/clinica/listar_medicos/";
  const especialidade = $(this).val();  
  $.ajax({                      
    url: url,
    data: {'especialidade': especialidade},                  
    success: function (data) {   
      let html_data="";
      data.forEach(function (medico) {
        html_data += `<option value="${medico.id}">${medico.nome}</option>`
      });
      $("#id_medico").html(html_data);
      atualizar_horarios();
    }
  });
});

let atualizar_horarios = function(){
  const url = "/clinica/listar_agenda_medico/";
  const dia = $("#id_data_day").val();
  const mes = $("#id_data_month").val();
  const ano = $("#id_data_year").val();
  const data = `${ano}-${mes}-${dia}`;
  const medico = $("#id_medico").val();  
  $.ajax({                      
    url: url,
    data: {
      'data': data,
      'id_doctor': medico
    },                  
    success: function (data) {   
      let html_data="";
      data.forEach(function (horario) {
        html_data += `<option value="${horario}">${horario}</option>`
      });
      $("#id_horario").html(html_data);
    },
    error: function(data){
      $("#id_horario").html(`<option value="null">Não há horários disponíveis nesta data!</option>`)
      $("#id_horario").prop("disabled", true)
      $("#submit-form").prop("disabled", true)
    }
  });
}

$("#id_data_day").change(atualizar_horarios);
$("#id_data_month").change(atualizar_horarios);
$("#id_data_year").change(atualizar_horarios);
$("#id_medico").change(atualizar_horarios);

