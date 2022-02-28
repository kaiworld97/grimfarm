function open_modal(){
    console.log('hi')
    document.getElementById(`buy_now`).showModal();
}

$(function(){
        // 	이미지 클릭시 해당 이미지 모달
        $(".news_line").click(function() {
            $("#news_detail").show();
        });

        // .modal안에 button을 클릭하면 .modal닫기
        $(".modal button").click(function(){
            $("#buy_now").hide();
            location.reload();
            console.log('refresh')
        });
    });
