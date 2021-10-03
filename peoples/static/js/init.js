$(document).ready(function(){
    $('.cpf').mask('000.000.000-00', {reverse: true});
    $('.celular').mask('(00)00000-0009');
    $('.telefone').mask('(00)0000-0009');
    $('.idsenso').mask('000.000.000.000', {reverse: true});
    $('.dataformato').mask('00/00/0000', {reverse: true});
    $('.certidao').mask('000000 00 00 0000 0 00000 000 0000000 00', {reverse: true});

     $('.js-example-responsive').select2({
        theme: "classic",
         width: 'resolve',

    });

     // $('#modalSuporte').modal.open()

});