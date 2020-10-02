const id_conversation = JSON.parse(document.getElementById('id_conversation').textContent);
const id_user = JSON.parse(document.getElementById('id_user').textContent);
const content_message = document.querySelector('.content_message')


function my_message(content) {
    content_message.innerHTML += '<div class="my_message">'+ content + '</div>'
}

function other_message(content) {
    content_message.innerHTML += '<div class="other_message">'+ content + '</div>'
}

function scroll_bottom() {
    const box_message = document.querySelector('.container_message')
    box_message.scrollTop = box_message.scrollHeight;
}

window.addEventListener("DOMContentLoaded", (event) => {
    scroll_bottom()
  });

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/message/'
    + id_conversation
    + '/'
)

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    
    if (data.id_user != id_user) {
        other_message(data.message)
    } else {
        my_message(data.message)
    }

    scroll_bottom()
    
};

document.getElementById('form_message').addEventListener('submit', (e) => {
    e.preventDefault()
    chatSocket.send(JSON.stringify({
        'message': document.getElementById('input_message').value,
        'id_user' : id_user,
    }));
    document.getElementById('input_message').value = ""
})
    