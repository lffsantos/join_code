$(function() {

    $('#reportrange').daterangepicker({
        autoUpdateInput: false,
        startDate: "25/01/2020",
        endDate: "26/01/2020",
        ranges: {
            'Hoje': [moment(), moment()],
            'Ontem': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            'Últimos 7 dias': [moment().subtract(6, 'days'), moment()],
            'Últimos 30 dias': [moment().subtract(29, 'days'), moment()],
            'Esse Mês': [moment().startOf('month'), moment().endOf('month')],
            'Mês Anterior': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        },
        locale: {
            "format": "DD/MM/YYYY",
            "separator": " - ",
            "applyLabel": "Aplicar",
            "cancelLabel": "Limpar",
            "fromLabel": "De",
            "toLabel": "Para",
            "customRangeLabel": "Custom",
            "weekLabel": "W",
            "daysOfWeek": ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex','Sab'],
            "monthNames": ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
            "firstDay": 1

        },
    });

    $('#reportrange').on('apply.daterangepicker', function(ev, picker) {
        $(this).val(picker.startDate.format('DD/MM/YYYY') + ' - ' + picker.endDate.format('DD/MM/YYYY'));
    });

    $('#reportrange').on('cancel.daterangepicker', function(ev, picker) {
        $(this).val('');
    }); 

    listaCargos();

});

let url_base = window.location.origin;

function show(tipo){
    $('.data-content').hide();
    if (tipo === 'listaFuncionarios'){
        listaFuncionarios()
    } else if(tipo === 'maisAntigo'){
        maisAntigo()
    } else{
        totalporCargos()
    }

}

filter_params = () => {
    let admissao =  $('input[name=datefilter]').val()
    
        let params = '?cargo='
        params += $('#cargoFilter').val() !== '' ? $('#cargoFilter').val() : '' 
    if (admissao !== ''){
        params += '&admissao__gte='+admissao.split(' - ')[0]
        params += '&admissao__lte='+admissao.split(' - ')[1]
    }
    return params
}

listaFuncionarios = () => {
    $('#listaFuncionarios').show();
    let query_string = filter_params();
    let url = url_base + '/api/pessoas/' + query_string;
    $('#tablefuncionarios tbody').html('')
    $.get(url, function(data) {
        $.each( data, function( index, value ){
            $('#tablefuncionarios tbody').append(
                '<tr>' +
                '<td>'+value.nome+'</td>' +
                '<td>'+value.cargo+'</td>' +
                '<td>'+value.admissao+'</td>' +
                '</tr>'
            );
        });
        
    })
    
}

maisAntigo = () => {
    $('#maisAntigo').show();
    $('#maisAntigo').html('');
    let url = url_base + '/mais-antigo';
    $.get(url, function(data) {
        $('#maisAntigo').append('<h3> Nome: </h3>'+ data.nome)
        $('#maisAntigo').append('<h3> Cargo: </h3>'+ data.cargo)
    }).fail(function() {
         $('#maisAntigo').html('Não existem Funcionarios cadastrado')
    });
}

totalporCargos = () => {
    $('#TotalporCargos').show();
    $('#tableCargos tbody').html('')
    let url = url_base + '/total-por-cargo';
     $.get(url, function(data) {
         let result = JSON.parse(data);
         $.each( result, function( index, value ){
            $('#tableCargos tbody').append(
                '<tr>' +
                '<td>'+value.nome+'</td>' +
                '<td>'+value.total+'</td>' +
                '</tr>'
            );
         })
    }).fail(function() {
         $('#tableCargos').html('Não existem Funcionarios cadastrado')
    });
}

listaCargos = () => {
    $('#cargoFilter').html('');
    let url = origin + '/api/cargos/'
    $('#cargoFilter').append('<option></option>');
    $.get(url, function(data) {
        $.each( data, function( index, value ){
            $('#cargoFilter').append('<option value="'+value.id+'">'+value.nome+'</option>');
        });
        
    })  
}

$(document).on('click', '#filtrarFuncionarios', function(){
    listaFuncionarios();
})