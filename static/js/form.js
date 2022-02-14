function atualizarForm(){
  tipo_funcionario = document.getElementById("tipo_funcionario");
  medico_form_div = document.getElementById("form-medico");
  if(tipo_funcionario.value=="medico"){
    medico_form_div.removeAttribute("hidden");
  }
  else{
    medico_form_div.setAttribute("hidden", "hidden");
  }
}