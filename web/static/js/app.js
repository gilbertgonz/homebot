async function update_map() {
    try {
        const response = await fetch('/ip_notify');
        const data = await response.json();
        const { latitude, longitude } = data;
        
        const map_frame = document.getElementById('map_frame');
        map_frame.src = `https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d1252452.5770398783!2d${longitude}!3d${latitude}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1716281798831!5m2!1sen!2sus`;
    } catch (error) {
        console.error('Error fetching GPS data:', error);
    }
}

// Update map when page loads
window.onload = update_map;