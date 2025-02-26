function handleEmptyLength(){
    let lengthInput = document.getElementById("lengthValue");
    let errorDiv = document.getElementById("lengthError");
    let submitButton = document.getElementById("submitButton");
    let form = document.getElementById("passwordForm");

    // Load saved length value from localStorage
    if (localStorage.getItem("passwordLength")) {
        lengthInput.value = localStorage.getItem("passwordLength");
    }

    lengthInput.addEventListener("input", function () {
        let min = parseInt(this.min);
        let max = parseInt(this.max);
        let value = parseInt(this.value);

        if (value < min || value > max || isNaN(value)) {
            errorDiv.classList.remove("d-none");  // Show error
            submitButton.disabled = true;  // Disable button
        } else {
            errorDiv.classList.add("d-none");  // Hide error
            submitButton.disabled = false;  // Enable button
            localStorage.setItem("passwordLength", value); 
        }
    });

    // Prevent form submission if value is invalid
    form.addEventListener("submit", function (event) {
        let value = parseInt(lengthInput.value);
        if (value < 8 || value > 32 || isNaN(value)) {
            event.preventDefault();  // Stop form submission
            errorDiv.classList.remove("d-none");  // Show error
        } else {
            localStorage.setItem("passwordLength", value);  // Save before submitting
        }
    });
}

function saveSelectedCheckbox() {
    document.getElementById("passwordForm").addEventListener("submit", function () {
        localStorage.setItem("uppercaseCheck", document.getElementById("uppercaseCheck").checked);
        localStorage.setItem("lowercaseCheck", document.getElementById("lowercaseCheck").checked);
        localStorage.setItem("numbersCheck", document.getElementById("numbersCheck").checked);
        localStorage.setItem("specialCheck", document.getElementById("specialCheck").checked);
    });
    
    window.addEventListener("load", function () {
        // Set default values if they are null (first visit)
        if (localStorage.getItem("uppercaseCheck") === null) {
            localStorage.setItem("uppercaseCheck", "true");
        }
        if (localStorage.getItem("lowercaseCheck") === null) {
            localStorage.setItem("lowercaseCheck", "true");
        }
        if (localStorage.getItem("numbersCheck") === null) {
            localStorage.setItem("numbersCheck", "true");
        }
        if (localStorage.getItem("specialCheck") === null) {
            localStorage.setItem("specialCheck", "false"); // Default to unchecked
        }
        document.getElementById("uppercaseCheck").checked = localStorage.getItem("uppercaseCheck") === "true";
        document.getElementById("lowercaseCheck").checked = localStorage.getItem("lowercaseCheck") === "true";
        document.getElementById("numbersCheck").checked = localStorage.getItem("numbersCheck") === "true";
        document.getElementById("specialCheck").checked = localStorage.getItem("specialCheck") === "true";
    });
}

document.addEventListener("DOMContentLoaded", function () {
    handleEmptyLength();
    saveSelectedCheckbox();
});
