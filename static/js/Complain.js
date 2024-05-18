// complain.js

document.addEventListener("DOMContentLoaded", function() {
    const openComplaintBoxBtn = document.getElementById('openComplaintBox');
    const complaintBox = document.getElementById('complaintBox');
    const complaintForm = document.getElementById('complaintForm');

    // Function to toggle complaint box visibility
    function toggleComplaintBox() {
        if (complaintBox.style.display === 'block') {
            complaintBox.style.display = 'none';
        } else {
            complaintBox.style.display = 'block';
        }
    } 

    // Event listener for the "Complain" button
    openComplaintBoxBtn.addEventListener('click', function() {
        toggleComplaintBox();
    });

    // Event listener for submitting the complaint form
    complaintForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(complaintForm);
        fetch('/complaint/submit/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Hide the complaint box after submission
                complaintBox.style.display = 'none';
                // Redirect to the complaints list page
                window.location.href = '/complaints/';
            } else {
                // Handle form errors
                alert('Error: ' + JSON.stringify(data.errors));
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
