document.getElementById('symptom-form').addEventListener('submit', function(event) {
    event.preventDefault();
    sendMessage();
});

function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== '') {
        var chatBox = document.getElementById('chat-box');
        var userMessage = document.createElement('div');
        userMessage.className = 'chat-message';
        userMessage.textContent = userInput;
        chatBox.appendChild(userMessage);

        sendToServer(userInput);
        document.getElementById('user-input').value = '';
    }
}

function displayResponse(response) {
    var chatBox = document.getElementById('chat-box');
    var botMessage = document.createElement('div');
    botMessage.className = 'bot-message';
    botMessage.textContent = 'Predicted disease: ' + response;
    chatBox.appendChild(botMessage);
}

function sendToServer(userInput) {
    var csrftoken = getCookie('csrftoken');  
    fetch('/predict_disease/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  
        },
        body: JSON.stringify({ symptoms: userInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            displayResponse(data.error);
        } else {
            displayResponse(data.predicted_disease);
        }
    })
    .catch(error => console.error('Error:', error));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
