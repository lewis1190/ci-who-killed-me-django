const profilePictureInput = document.getElementById('profilePictureInput');
const saveButton = document.getElementById('saveButton');
const discardButton = document.getElementById('discardButton');
const profileForm = document.getElementById('profileForm');

// Enable/disable buttons based on file selection
profilePictureInput.addEventListener('change', function (e) {
    const file = e.target.files[0];

    // Enable buttons if a file is selected
    const hasFile = file !== undefined && file !== null;
    saveButton.disabled = !hasFile;
    discardButton.disabled = !hasFile;

    if (file) {
        // Preview the image
        const reader = new FileReader();
        reader.onload = function (event) {
            document.getElementById('profilePicture').src = event.target.result;
        };
        reader.readAsDataURL(file);
    }
});

// Clear file input and disable buttons when discarding
discardButton.addEventListener('click', function () {
    // Clear the file input
    profilePictureInput.value = '';

    // Disable buttons
    saveButton.disabled = true;
    discardButton.disabled = true;

    // Reload the page
    location.reload();
});

// Disable buttons after form submission
profileForm.addEventListener('submit', function () {
    saveButton.disabled = true;
    discardButton.disabled = true;
});
