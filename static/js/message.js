import { insertPost, request, SendSocketUser } from './module/helper.js'

const id_user = JSON.parse(document.getElementById('id_user').textContent)
const place_message = document.querySelector('.content_message')
const id_conversation = window.location.href.split('/')[4]
const id_other_user = document.getElementById('user_conv').textContent

function my_message(content) {
    place_message.innerHTML += '<div class="my_message">'+ content + '</div>'
}

function other_message(content) {
    place_message.innerHTML += '<div class="other_message">'+ content + '</div>'
}

function scroll_bottom() {
    const box_message = document.querySelector('.container_message')
    box_message.scrollTop = box_message.scrollHeight;
}

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

    SendSocketUser(id_user)
    SendSocketUser(id_other_user)
    
    let data_send = {
        "content_message" : document.getElementById('input_message').value,
        "id_receiving" : id_other_user,
        "id_conversation" : id_conversation
    }
    
    insertPost(
        data_send,
        '/api/v0/message/insertmessage/'
    )
    document.getElementById('input_message').value = ""
})

request(
    '/api/v0/message/messageconversation/' + id_conversation
).then(data => {
    for (let i = 0; i < data.count; i++) {
        if (data.results[i].id_giving == id_user) {
            my_message(data.results[i].content_message)
        } else{
            other_message(data.results[i].content_message)
        }
    }
    scroll_bottom()
})


document.getElementById('input_message').addEventListener('click', (e) => {
    const data_read = {
        "id_conversation" : id_conversation
    }
    insertPost(
        data_read,
        '/api/v0/message/readmessage/'
    )
})