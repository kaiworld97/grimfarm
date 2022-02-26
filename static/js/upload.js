function loadFile(input) {
    let file = input.files[0];
    let file_img = document.getElementById("input_img");
    let empty_img = document.getElementById('empty_img')
    if (empty_img.style.display != 'none') {
        empty_img.classList.add('img_rotate3d')
        setTimeout(() => {
            empty_img.style.display = 'none'
            file_img.src = URL.createObjectURL(file);
            document.getElementById('input_img_wrapper').style.display = 'flex'
            document.getElementById('input_img_wrapper').classList.remove('hidden')
        }, 500)
    } else {
        file_img.classList.add('img_rotate3d')
        setTimeout(() => {
            file_img.classList.remove('img_rotate3d')
            file_img.src = URL.createObjectURL(file);
        }, 500)
    }
}

function click_style(input) {
    let style_img = document.getElementById('style_img')
    let empty_style = document.getElementById('empty_style')
    if (empty_style.style.display != 'none') {
        empty_style.classList.add('img_rotate3d')
        setTimeout(() => {
            empty_style.style.display = 'none'
            style_img.src = input.src
            document.getElementById('style_img_wrapper').classList.remove('hidden')
            document.getElementById('style_img_wrapper').style.display = 'flex'
        }, 500)
    } else {
        style_img.classList.add('img_rotate3d')
        setTimeout(() => {
            style_img.classList.remove('img_rotate3d')
            style_img.src = input.src
        }, 500)
    }


}

function img_style_change() {
    let file_img = document.getElementById("input_img");
    let style_img = document.getElementById('style_img')
    let file_img2 = file_img.src
    let style_img2 = style_img.src
    if (file_img2 == 'http://127.0.0.1:8000/1' | style_img2 == 'http://127.0.0.1:8000/1') {
        return alert('Nope!')
    }

    file_img.classList.add('move_right')
    style_img.classList.add('move_left')

    setTimeout(() => {
        file_img.classList.remove('move_right')
        style_img.classList.remove('move_left')
        file_img.src = style_img2
        style_img.src = file_img2
    }, 1200)
}

function posting() {
    let file = $('#select_file')[0].files[0]
    var num = $('input[name=style]:checked').val();
    let file_id = document.getElementById('select_file').value.split('\\')[2].split('.')[0]
    let key = String(new Date().getTime()) + file_id
    let form_data = new FormData()


    form_data.append("img", file)
    form_data.append("num", num)
    form_data.append("key", key)

    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:5000/api/v1/nsts/',
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        enctype: 'multipart/form-data',
        success: function (response) {
            console.log(response['file_url'])
            let output = document.getElementById('output')
            let out_img = document.createElement("img");
            out_img.src = response['file_url']
            out_img.style.width = "100%";
            out_img.style.height = "100%";
            out_img.style.visibility = "visible";
            out_img.style.objectFit = "cover"
            output.appendChild(out_img);
        }
    });
}

function posting1() {
    document.getElementById('style_box').classList.add('fade-out-box')
    document.getElementById('img_options').classList.add('fade-out-box')
    document.getElementById('input_p').classList.add('fade-out-box')
    document.getElementById('style_p').classList.add('fade-out-box')
    document.getElementById('input_img').classList.add('small_box')
    document.getElementById('style_img').classList.add('small_box')
    setTimeout(() => {
        document.getElementById('upload_container').style.display = 'none'
        document.getElementById('move1').src = document.getElementById('input_img').src
        document.getElementById('move2').src = document.getElementById('style_img').src
        document.getElementById('move1').style.width = document.getElementById('input_img').style.width
        document.getElementById('move2').style.width = document.getElementById('style_img').style.width
        document.getElementById('move1').style.height = document.getElementById('input_img').style.height
        document.getElementById('move2').style.height = document.getElementById('style_img').style.height
        document.getElementById('move_div').style.display = 'flex'
        setTimeout(() => {
            document.getElementById('move_div').style.display = 'none'
            document.getElementById('output').classList.remove('hidden')
            document.getElementById('output').classList.add('fade-in-box')
            setTimeout(() => {
                document.getElementById('output_btns').style.display = 'flex'
                document.getElementById('output_btns').classList.add('fade-in-box1')
            }, 3000)
        }, 2000)
    }, 1200)
}