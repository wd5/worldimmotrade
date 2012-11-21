$(function(){
    $("#userprofile_form").relatedSelects({
        onChangeLoad: '/world/load_json/',
        defaultOptionText: '-------',
        selects: {
           'country':		{ loadingMessage:'Loading Regions...' },
            'region':		{ loadingMessage:'Loading Cities...' },
            'city':		{}
        }
    });
});