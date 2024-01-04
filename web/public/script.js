function goToNextPage() {
    // Redirect to another page
    window.location.href = 'testpage.html';
}

function backToHomePage(){
    window.location.href = 'index.html';
}

document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:3000/test_get') // Replace with your API URL
        .then(response => response.json())
        .then(data => {
            const displayDiv = document.getElementById('api-data');
            displayDiv.innerHTML = JSON.stringify(data, null, 2); // Display data as formatted JSON
            // You can also loop through the data and format it as needed
        })
        .catch(error => console.error('Error fetching data:', error));
});
