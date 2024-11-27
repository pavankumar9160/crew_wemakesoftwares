const captureInterval = 10 * 60 * 1000; // 10 minutes in milliseconds

function startVideoStream(callback) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            const video = document.createElement('video');
            video.style.display = 'none';
            document.body.appendChild(video);
            video.srcObject = stream;

            video.addEventListener('loadedmetadata', () => {
                video.play();
                callback(video, stream);
            });
        })
        .catch(err => {
            console.error("Error accessing camera:", err);
        });
}

// Function to stop the video stream
function stopVideoStream(stream) {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
    }
}

// Function to capture the image from the video stream
function captureImage(video, stream) {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageData = canvas.toDataURL('image/png'); // Convert to Base64

    sendImageToServer(imageData, stream); // Send image to server
}

// Function to send the captured image to the server
function sendImageToServer(imageData, stream) {
    // Convert Base64 to Blob
    const byteString = atob(imageData.split(',')[1]);
    const mimeString = imageData.split(',')[0].split(':')[1].split(';')[0];
    const ab = new Uint8Array(byteString.length);

    for (let i = 0; i < byteString.length; i++) {
        ab[i] = byteString.charCodeAt(i);
    }

    const blob = new Blob([ab], { type: mimeString });

    const formData = new FormData();
    formData.append('image', blob, 'captured_image.png');


    fetch('/Support_v2/capture-image/', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log('Image uploaded successfully:', data);
            const nextCaptureTime = Date.now() + captureInterval;
            localStorage.setItem('nextCaptureTime', nextCaptureTime);
            stopVideoStream(stream);
        })
        .catch(error => {
            console.error('Error uploading image:', error);
            stopVideoStream(stream);
        });
}

// Function to initialize the capture process
function initCapture() {
    const isLogged = localStorage.getItem('is_logged');
    if (isLogged) {
        const nextCaptureTime = parseInt(localStorage.getItem('nextCaptureTime')) || Date.now();
        const now = Date.now();

        function formatDate(timestamp) {
            const date = new Date(timestamp);
            return date.toLocaleString();
        }

        const readableNextCaptureTime = formatDate(nextCaptureTime);
        const readableNow = formatDate(now);

        console.log('Next Capture Time:', readableNextCaptureTime);
        console.log('Current Time:', readableNow);

        if (now >= nextCaptureTime) {
            startVideoStream(captureImage);
        }
    }
}

// // Start capture on page load
// document.addEventListener('DOMContentLoaded', () => {
//     const isLogged = localStorage.getItem('is_logged');
//     if (isLogged) {
//         initCapture();
//         setInterval(initCapture, 60 * 1000);
//     }
// });