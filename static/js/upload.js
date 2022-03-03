const no_href = window.location.href + 1
let input_type = 'file'
let style_type = 'url'
let input_now = ''
let style_now = ''

function loadFile(input) {
    let file = input.files[0];
    let file_img = document.getElementById("input_img");
    let empty_img = document.getElementById('empty_img')
    input_type = 'file'
    input_now = file
    file_img.src = URL.createObjectURL(file);
    if (empty_img.style.display != 'none') {
        empty_img.classList.add('img_rotate3d')
        setTimeout(() => {
            empty_img.style.display = 'none'
            document.getElementById('input_img_wrapper').style.display = 'flex'
            document.getElementById('input_img_wrapper').classList.remove('hidden')
        }, 500)
    } else {
        file_img.classList.add('img_rotate3d')
        setTimeout(() => {
            file_img.classList.remove('img_rotate3d')
        }, 500)
    }
}

function click_style(input) {
    let style_img = document.getElementById('style_img')
    let empty_style = document.getElementById('empty_style')
    style_img.src = input.src
    style_type = 'url'
    style_now = style_img.src
    if (empty_style.style.display != 'none') {
        empty_style.classList.add('img_rotate3d')
        setTimeout(() => {
            empty_style.style.display = 'none'
            document.getElementById('style_img_wrapper').classList.remove('hidden')
            document.getElementById('style_img_wrapper').style.display = 'flex'
        }, 500)
    } else {
        style_img.classList.add('img_rotate3d')
        setTimeout(() => {
            style_img.classList.remove('img_rotate3d')
        }, 500)
    }
}

function img_style_change() {
    let file_img = document.getElementById("input_img");
    let style_img = document.getElementById('style_img')
    let file_img2 = file_img.src
    let style_img2 = style_img.src
    if (file_img2 == no_href | style_img2 == no_href) {
        return alert('Nope!')
    }
    let ex_input_type = input_type
    let ex_style_type = style_type
    let ex_input_now = input_now
    let ex_style_now = style_now
    input_type = ex_style_type
    input_now = ex_style_now
    style_type = ex_input_type
    style_now = ex_input_now


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
    const username = document.getElementById('user_nickname')
    if (username == null) {
        return alert('Please Sign in')
    }
    let key = String(new Date().getTime()) + username.innerText.split(' ')[0]
    let form_data = new FormData()


    if (input_type == "url") {
        form_data.append("img_url", input_now)
    } else {
        form_data.append("img", input_now)
    }
    if (style_type == "url") {
        form_data.append("style_url", style_now)
    } else {
        form_data.append("style_img", style_now)
    }
    form_data.append("key", key)
    console.log(username.innerText.split(' ')[0])
    console.log(input_now)
    console.log(style_now)

    $.ajax({
        type: "POST",
        url: 'http://project-nst-dev.ap-northeast-2.elasticbeanstalk.com/api/v1/nsts/',
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        enctype: 'multipart/form-data',
        success: function (response) {
            console.log(response['file_url'])
            document.getElementById('output_img').src = response['file_url']
            document.getElementById('output_url').value = response['file_url']
        }
    });
}

function posting1() {
    if (document.getElementById('input_img').src == no_href | document.getElementById('style_img').src == no_href) {
        return alert('Nope!')
    }
    const username = document.getElementById('user_nickname')
    if (username == null) {
        return
    }
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
            document.getElementById('output_wrapper').style.display = 'flex'
            document.getElementById('output').classList.remove('hidden')
            document.getElementById('output').classList.add('fade-in-box')
            setTimeout(() => {
                document.getElementById('output_btns').style.display = 'flex'
                document.getElementById('output_btns').classList.add('fade-in-box1')
            }, 5000)
        }, 5000)
    }, 2800)
}

function url_img() {
    let img_src = prompt('url을 입력해주세요')
    if (img_src == null) {
        return
    }
    let input_img = document.getElementById('input_img')
    input_img.src = img_src
    input_now = input_img.src
    input_type = 'url'

    let empty_img = document.getElementById('empty_img')
    if (empty_img.style.display != 'none') {
        empty_img.classList.add('img_rotate3d')
        setTimeout(() => {
            empty_img.style.display = 'none'
            input_img.src = img_src;
            document.getElementById('input_img_wrapper').style.display = 'flex'
            document.getElementById('input_img_wrapper').classList.remove('hidden')
        }, 500)
    } else {
        input_img.classList.add('img_rotate3d')
        setTimeout(() => {
            input_img.classList.remove('img_rotate3d')
            input_img.src = img_src;
        }, 500)
    }
}

function url_style() {
    let style_src = prompt('url을 입력해주세요')
    if (style_src == null) {
        return
    }
    let style_img = document.getElementById('style_img')
    let empty_style = document.getElementById('empty_style')
    style_img.src = style_src
    style_now = style_img.src
    style_type = 'url'

    if (empty_style.style.display != 'none') {
        empty_style.classList.add('img_rotate3d')
        setTimeout(() => {
            empty_style.style.display = 'none'
            document.getElementById('style_img_wrapper').classList.remove('hidden')
            document.getElementById('style_img_wrapper').style.display = 'flex'
        }, 500)
    } else {
        style_img.classList.add('img_rotate3d')
        setTimeout(() => {
            style_img.classList.remove('img_rotate3d')
        }, 500)
    }
}


const canvas = document.getElementById("jsCanvas");
const ctx = canvas.getContext("2d");
const colors = document.getElementsByClassName("jsColor");
const range = document.getElementById("jsRange");
const mode = document.getElementById("jsMode");
const saveBtn = document.getElementById("jsSave");

const INITIAL_COLOR = "#2c2c2c";
const CANVAS_SIZE = 500;

canvas.width = CANVAS_SIZE;
canvas.height = CANVAS_SIZE;

ctx.fillStyle = "white";
ctx.fillRect(0, 0, CANVAS_SIZE, CANVAS_SIZE);
ctx.strokeStyle = INITIAL_COLOR;
ctx.fillStyle = INITIAL_COLOR;
ctx.lineWidth = 10;

let painting = false;
let filling = false;

function stopPainting() {
    painting = false;
}

function startPainting() {
    painting = true;
}

function onMouseMove(event) {
    const x = event.offsetX;
    const y = event.offsetY;
    if (!painting) {
        ctx.beginPath();
        ctx.moveTo(x, y);
    } else {
        ctx.lineTo(x, y);
        ctx.stroke();
    }
}

function handleColorClick(event) {
    const color = event.target.style.backgroundColor;
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
}

function handleRangeChange(event) {
    const size = event.target.value;
    ctx.lineWidth = size;
}

function handleModeClick() {
    if (filling === true) {
        filling = false;
        mode.innerText = "Fill";
    } else {
        filling = true;
        mode.innerText = "Paint";
    }
}

function handleCanvasClick() {
    if (filling) {
        ctx.fillRect(0, 0, CANVAS_SIZE, CANVAS_SIZE);
    }
}

function handleCM(event) {
    event.preventDefault();
}

function handleSaveClick() {
    const image = canvas.toDataURL();
    const link = document.createElement("a");
    link.href = image;
    link.download = "painting.png";
    link.click();
    link.remove()
}

if (canvas) {
    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", startPainting);
    canvas.addEventListener("mouseup", stopPainting);
    canvas.addEventListener("mouseleave", stopPainting);
    canvas.addEventListener("click", handleCanvasClick);
    canvas.addEventListener("contextmenu", handleCM);
}

Array.from(colors).forEach(color =>
    color.addEventListener("click", handleColorClick)
);

if (range) {
    range.addEventListener("input", handleRangeChange);
}

if (mode) {
    mode.addEventListener("click", handleModeClick);
}

if (saveBtn) {
    saveBtn.addEventListener("click", handleSaveClick);
}
const clear = document.getElementById("jsClear");
if (clear) {
    clear.addEventListener("click", () => ctx.clearRect(0, 0, canvas.width, canvas.height));
}

function go_drawing() {
    document.getElementById('upload_container').classList.add('right_slide_out')
    document.getElementById('upload_container').classList.remove('right_slide_in')
    setTimeout(() => {
        document.getElementById('upload_container').style.display = 'none'
        document.getElementById('upload_container').classList.add('hidden')
        document.getElementById('upload_container').classList.remove('right_slide_out')
    }, 90)
    document.getElementById('drawing').classList.add('left_slide_in')
    document.getElementById('drawing').classList.remove('hidden')
}

function go_upload() {
    document.getElementById('drawing').classList.add('left_slide_out')
    document.getElementById('drawing').classList.remove('left_slide_in')
    setTimeout(() => {
        document.getElementById('drawing').classList.add('hidden')
        document.getElementById('drawing').classList.remove('left_slide_out')
        document.getElementById('upload_container').style.display = 'flex'
        document.getElementById('upload_container').classList.remove('hidden')
    }, 90)
    document.getElementById('upload_container').classList.add('right_slide_in')
    ctx.clearRect(0, 0, canvas.width, canvas.height)
}

function go_image() {
    const image = canvas.toDataURL();
    document.getElementById('input_img').src = image
    document.getElementById('input_img_wrapper').style.display = 'flex'
    document.getElementById('empty_img').style.display = 'none'
    fetch(image)
        .then(res => res.blob())
        .then(blob => {
            const file = new File([blob], 'photo.png', blob)
            input_now = file
            input_type = 'file'
        })
    go_upload()
}

function go_style() {
    const image = canvas.toDataURL();
    document.getElementById('style_img').src = image
    document.getElementById('style_img_wrapper').style.display = 'flex'
    document.getElementById('empty_style').style.display = 'none'
    fetch(image)
        .then(res => res.blob())
        .then(blob => {
            const file = new File([blob], 'photo.png', blob)
            style_now = file
            style_type = 'file'
        })
    go_upload()

}

const jsBack = document.getElementById('jsBack')
const jsImage = document.getElementById('jsImage')
const jsStyle = document.getElementById('jsStyle')


if (jsBack) {
    jsBack.addEventListener('click', go_upload)
}
if (jsImage) {
    jsImage.addEventListener('click', go_image)
}
if (jsStyle) {
    jsStyle.addEventListener('click', go_style)
}

function download_img() {
    const down_link = document.createElement("a");
    down_link.href = document.getElementById('output_img').src
    down_link.download = "output_img.png";
    down_link.click();
    // down_link.remove()
}

function save_sell() {
    document.getElementById('output_btns').style.display = 'none'
    document.getElementById('output_img').classList.add('move_left_output')
    setTimeout(() => {
        document.getElementById('output_img').classList.remove('move_left_output')
        document.getElementById('save_wrapper').classList.remove('hidden')
    }, 2000)
}