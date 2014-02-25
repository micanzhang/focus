require.config({
  paths: {
      "jquery" :"jquery-1.10.2.min",
      "bootstrap" : "bootstrap.min"
  }
});

require(['jquery', 'bootstrap'], function($, _){
    //$(".alert").alert('close');
})