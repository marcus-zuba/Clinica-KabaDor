function atualizarForm(){
  tipo_funcionario = document.getElementById("tipo_funcionario");
  medico_form_div = document.getElementById("form-medico");
  especialidade = document.getElementById("id_especialidade");
  crm = document.getElementById("id_crm");
  if(tipo_funcionario.value=="medico"){
    medico_form_div.removeAttribute("hidden");
    especialidade.removeAttribute("disabled");
    crm.removeAttribute("disabled");
  }
  else{
    medico_form_div.setAttribute("hidden", "hidden");
    especialidade.setAttribute("disabled", "disabled");
    crm.setAttribute("disabled", "disabled");
  }
}