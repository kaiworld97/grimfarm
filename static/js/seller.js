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


function loadFile(input){
    let file = input.files[0];
    let file_name = document.getElementById('img_name');
    file_name.textContent = file.name;

    let file_img = document.createElement("img");
    file_img.setAttribute("class", 'new_img')
    file_img.src = URL.createObjectURL(file);

    file_img.style.width = "8vw";
    file_img.style.height = "8vw";
    file_img.style.visibility = "visible";
    file_img.style.objectFit = "contain";


    // document.getElementById('btn').classList.add('hidden')
    document.getElementById('choose_pic').classList.add('hidden')

    let container = document.getElementById("profileimg");

    container.style.width = "100px";
    container.innerHTML = '';
    container.appendChild(file_img);


}