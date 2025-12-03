document.addEventListener("DOMContentLoaded", function () {
   let toggle = document.querySelector(".toggle-menu");
   let nav = document.querySelector("header nav ul");
   toggle.addEventListener("click", function () {
      nav.classList.toggle("active");
   });
});
// End Click on toggle

document.addEventListener("DOMContentLoaded", function () {
   let home = document.getElementById("home-link");
   home.addEventListener("click", function (e) {
      e.preventDefault();
      window.location.href = "index.html";
   });
});
// End homePage

document.addEventListener("DOMContentLoaded", function () {
   let whoAre = document.getElementById("who-are-we-link");
   whoAre.addEventListener("click", function (e) {
      e.preventDefault();
      window.location.href = "who-are-we.html";
   });
});
// End who-are-we

document.addEventListener("DOMContentLoaded", function () {
   let services = document.getElementById("services-link");
   services.addEventListener("click", function (event) {
      event.preventDefault();
      window.location.href = "services.html";
   });
});
// End Services

document.addEventListener("DOMContentLoaded", function () {
   let Environmental = document.getElementById("Environmental-link");
   Environmental.addEventListener("click", function (event) {
      event.preventDefault();
      window.location.href = "Environmental.html";
   });
});
// End Environmental

document.addEventListener("DOMContentLoaded", function () {
   let connections = document.getElementById("contact-us-link");
   connections.addEventListener("click", function (e) {
      e.preventDefault();
      window.location.href = "contact-us.html";
   });
});
//End Contact Us

document.addEventListener("DOMContentLoaded", function () {
   let ouServices = document.getElementById("get-our-services-link");
   ouServices.addEventListener("click", function (event) {
      event.preventDefault();
      window.location.href = "get-our-services.html";
   });
});
// End Get our Services

document.addEventListener("DOMContentLoaded", function () {
   let singing = document.getElementById("Registration-link");
   singing.addEventListener("click", function (event) {
      event.preventDefault();
      window.location.href = "Registration.html";
   });
});

let btns = document.querySelectorAll(".input");

function focusFunc() {
   let parent = this.parentNode;
   parent.classList.add("focus");
}
function blurFunc() {
   let parent = this.parentNode;
   if (this.value == "") {
      parent.classList.remove("focus");
   }
}

btns.forEach((input) => {
   input.addEventListener("focus", focusFunc);
   input.addEventListener("blur", blurFunc);
});

// Get the modal
let modal = document.getElementById("registrationModal");

// Get the buttons that open the modal
let registrationButtons = document.querySelectorAll(".box a");

// Get the <span> element that closes the modal
let closeBtn = document.querySelector(".close");

// When the user clicks on a registration button, open the modal
registrationButtons.forEach((button) => {
   button.addEventListener("click", (event) => {
      event.preventDefault(); // Prevent default link behavior
      modal.style.display = "block"; // Show the modal
   });
});

// When the user clicks on <span> (x), close the modal
closeBtn.addEventListener("click", () => {
   modal.style.display = "none"; // Hide the modal
});

// When the user clicks anywhere outside the modal, close it
window.addEventListener("click", (event) => {
   if (event.target === modal) {
      modal.style.display = "none"; // Hide the modal
   }
});

// Handle form submission
document
   .getElementById("registrationForm")
   .addEventListener("submit", (event) => {
      event.preventDefault(); // Prevent form submission
      let name = document.getElementById("name").value;
      let email = document.getElementById("email").value;
      let password = document.getElementById("password").value;

      // Perform validation or send data to the server
      console.log("Name:", name);
      console.log("Email:", email);
      console.log("Password:", password);

      // Close the modal after submission
      modal.style.display = "none";
   });
// End Form Membership

document.querySelectorAll(".input-box input").forEach((input) => {
   input.addEventListener("focus", function () {
      this.style.borderColor = "#2c5f2d";
      this.style.boxShadow = "0 0 5px #2c5f2d";
   });

   input.addEventListener("blur", function () {
      this.style.borderColor = "#ccc";
      this.style.boxShadow = "none";
   });
});
// effect on border contact us

document.querySelector("form").addEventListener("submit", function (event) {
   event.preventDefault();
   alert("تم التسجيل بنجاح!");
});
// click on submit contact us
