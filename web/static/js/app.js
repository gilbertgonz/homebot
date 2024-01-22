// Get elements
var joyX = document.getElementById("joyX");
var joyY = document.getElementById("joyY");

// Create JoyStick object
var joyParam = {"internalLineWidth": "5", 
"externalLineWidth": "5", "externalStrokeColor": "#696969", 
"internalFillColor": "#696969", "internalStrokeColor": "#696969"};
var joy = new JoyStick('joyDiv', joyParam);

// Update UI values
setInterval(function(){ joyX.value=joy.GetX(); }, 50);
setInterval(function(){ joyY.value=joy.GetY(); }, 50);

// Function to send joystick data to backend
function sendJoystickToBackend(data) {
    fetch('/update_joystick', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(responseData => {
        console.log('Response from backend:', responseData);
    })
    .catch(error => {
        console.error('Error sending data to backend:', error);
    });
}

setInterval(function() {
    var x = joy.GetX();
    sendJoystickToBackend({ x });
}, 50);

setInterval(function() {
    var y = joy.GetY();
    sendJoystickToBackend({ y });
}, 50);