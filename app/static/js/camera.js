const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const capture = document.getElementById('capture');
const result = document.getElementById('result');

// Abrir câmera
navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
    video.srcObject = stream;
}).catch(err => {
    alert('Erro ao acessar a câmera: ' + err);
});

// Capturar imagem
capture.onclick = () => {
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('image', blob, 'capture.jpg');

        fetch('/scan', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            result.innerHTML = '<h2>Contagem:</h2>';
            const table = document.createElement('table');
            table.innerHTML = '<tr><th>Código</th><th>Quantidade</th></tr>';
            for (const [code, count] of Object.entries(data.counts)) {
                table.innerHTML += `<tr><td>${code}</td><td>${count}</td></tr>`;
            }
            result.appendChild(table);
        });
    }, 'image/jpeg');
};
