import { request, insertPost, box_user_search, box_user, ConnectSocketUser } from './module/helper.js'

const form_search = document.querySelector('.search_user_form')
const input_menu = document.querySelector('.input_menu')
const place_user = document.getElementById('box_user_search')
const id_user = JSON.parse(document.getElementById('id_user').textContent)


function box_user_menu(data){
    place_user.innerHTML = ""
    for (let i = 0; i < data.length; i++) {
        let id_user_searched = data[i].id
        
        let data_click = {
            "receipient": id_user_searched
        }
        
        
        place_user.append(box_user_search(
            data[i].image_profile, 
            data[i].username,
            data_click,
        ))

    }
}

function display_conversation() {
    request(
        '/api/v0/message/lastuser'
    ).then(data => {
        for (let i = 0; i < data.results.length; i++) {
            place_user.append(box_user(
                data.results[i].image_profile,
                data.results[i].username,
                data.results[i].last_message.content_message.substring(0,9) + '...',
                data.results[i].id,
            ))
        }
    })
}

display_conversation()


form_search.addEventListener('submit', (e) => {
    e.preventDefault()
    
    let data_input = {
        "searched_user" : input_menu.value
    }
    
    insertPost(
        data_input,
        '/api/v0/user/searchuser/',
    ).then(data => {
        box_user_menu(data)
    })

    input_menu.value = ""
})

ConnectSocketUser(id_user).onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

const mySocket  = ConnectSocketUser(id_user)
mySocket.onmessage = function(e) {
    console.log("hey")
    place_user.innerHTML = ""
    display_conversation()
    
};

