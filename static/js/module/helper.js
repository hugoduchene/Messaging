function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

const insertPost = async function(data, url_request) {
    let response = await fetch(url_request, {
      method: 'POST',
      headers : {
        'Content-Type': 'application/json',
        'X-CSRFToken' : getCookie('csrftoken'),
        'credentials' : 'same-origin',
      },
      body: JSON.stringify(data)
    })
    let responsedata = await response.json()
    if (response.ok) {
      return responsedata
    
    } else {
      console.log(response.status)
    }
  }

const request = async function (url_request) {
    const headers = { 
        method: 'GET',
        headers: {
        'Content-Type': 'application/json',
        'credentials' : 'same-origin',
        },
    }
    try {
        let response = await fetch(url_request, headers)
        if (response.ok) {
            let data = await response.json()

            return data
        } else {
            console.error('retour du serveur : ', response.status)
        }
        } catch (e) {
        console.log(e)

        }
}

function conversation_click(elt, data_click){
  elt.addEventListener('click', (e) => {
    insertPost(
      data_click,
      '/api/v0/message/createconversation/',
    ).then(data => {
      window.location = '/message/'+ data['id']
    })
  })
}

function box_user_search(path_img, name, data){
  const container_box_user = document.createElement('a')
  container_box_user.classList.add('friends')
  conversation_click(container_box_user, data)

  const container_img = document.createElement('div')
  container_img.classList.add('user_pic')
  const img_user = document.createElement('img')
  img_user.src = path_img
  img_user.alt = "pic_user"
  container_img.append(img_user)
  container_box_user.append(container_img)

  const container_last_message = document.createElement('div')
  container_last_message.classList.add('container_last')

  const last_message = document.createElement('div')
  last_message.classList.add = "last_message"
  container_last_message.append(last_message)

  const title_name = document.createElement('div')
  title_name.classList.add = "title_name"
  title_name.textContent = name
  last_message.append(title_name)

  const content_last_message = document.createElement('div')
  content_last_message.classList.add('content_last_message')
  last_message.append(content_last_message)
  container_box_user.append(container_last_message)

  return container_box_user

}

function box_user(path_img, name, message, id_conversation){
  const container_box_user = document.createElement('a')
  container_box_user.href = '/message/' + id_conversation
  container_box_user.classList.add('friends')

  const container_img = document.createElement('div')
  container_img.classList.add('user_pic')
  const img_user = document.createElement('img')
  img_user.src = '/media/' + path_img
  img_user.alt = "pic_user"
  container_img.append(img_user)
  container_box_user.append(container_img)

  const container_last_message = document.createElement('div')
  container_last_message.classList.add('container_last')

  const last_message = document.createElement('div')
  last_message.classList.add = "last_message"

  const title_name = document.createElement('div')
  title_name.classList.add('title_name')
  title_name.textContent = name
  last_message.append(title_name)

  const content_last_message = document.createElement('div')
  content_last_message.classList.add('content_last_message')
  content_last_message.textContent = message
  
  container_last_message.append(last_message)
  last_message.append(content_last_message)
  container_box_user.append(container_last_message)

  return container_box_user
}


function ConnectSocketUser(id_user){
  const chatSocketUser = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/messages/'
    + id_user
    + '/'
  )
  
  return chatSocketUser
}

function SendSocketUser(id_user){
  const socketUser = ConnectSocketUser(id_user)
    socketUser.onopen = () => {
        socketUser.send(JSON.stringify({
            'send' : 'OK',
        }));
      }
}

export{
    request,
    insertPost,
    box_user_search,
    box_user,
    ConnectSocketUser,
    SendSocketUser,
}