$(document).ready(function(){

	$('ul.tabs li').click(function(){
		var tab_id = $(this).attr('data-tab');

		$('ul.tabs li').removeClass('current');
		$('.tab-content').removeClass('current');

		$(this).addClass('current');
		$("#"+tab_id).addClass('current');
	})

});



function open_modal(){
    console.log('hi')
    document.getElementById(`info_edit`).showModal();
}

$(function(){
        // 	이미지 클릭시 해당 이미지 모달
        $(".news_line").click(function() {
            $("#news_detail${data}").show();
        });

        // .modal안에 button을 클릭하면 .modal닫기
        $(".modal button").click(function(){
            $("#info_edit").hide();
            location.reload();
            console.log('refresh')
        });
    });