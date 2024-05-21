async function update_map() {
    try {
        const response = await fetch('/get_gps');
        const data = await response.json();
        const { latitude, longitude } = data;
        
        const map_frame = document.getElementById('map_frame');
        map_frame.src = `https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1612512.050923047!2d${longitude}!3d${latitude}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808583a3a688d7b5%3A0x8c891b8457461fa9!2sSan%20Francisco%20Bay%20Area%2C%20CA!5e0!3m2!1sen!2sus!4v1715501127406!5m2!1sen!2sus`;
    } catch (error) {
        console.error('Error fetching GPS data:', error);
    }
}

// Update the map when the page loads
window.onload = update_map;