$(function(){
    $("#apartament_form").relatedSelects({
        onChangeLoad: '/world/load_json/',
        onChange: function(){
            $("#id_city_loader").val("");
            $('#id_city_loader').autocomplete('option', 'source', "/world/autocomplete?country=" + $("#id_country").val() + "&region=" + $("#id_region").val());

        },
        defaultOptionText: '-------',
        selects: {
           'country':		{ loadingMessage:'Loading Regions...' },
           'region':		{ loadingMessage:'Loading Cities...' }
        }
    });

    $( "#id_city_loader" ).autocomplete({
			source: "/world/autocomplete?country=" + $("#id_country").val() + "&region=" + $("#id_region").val(),
			minLength: 1,
			select: function(event,ui){
                $("#id_city").val(ui.item.id);
			}
    })

    $('.city').css('display','none');
    $('.city').after($('.city_loader'));
});