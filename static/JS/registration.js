// Modal Functionality
document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("registrationModal");
    const openModalButtons = document.querySelectorAll(".box a");
    const closeModalButton = document.querySelector(".modal .close");

    // Open Modal
    openModalButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            modal.style.display = "block";
        });
    });

    // Close Modal
    closeModalButton.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Close Modal on Outside Click
    window.addEventListener("click", (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });

    // Form Submission
    const form = document.getElementById("registrationForm");
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        alert("Thank you for registering!");
        modal.style.display = "none";
    });
});