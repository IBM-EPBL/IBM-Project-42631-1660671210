function moveinputsignup() {
   var name = document.forms["sform"]["username"].value;
   var email = document.forms["sform"]["email"].value;
   if (name.length < 7)
   {
      alert("Username must be greater than 6")
      return;
   }
   if(email.length == 0)
      {
         alert("Enter Email ID to move further")
         return;
      }
   var element = document.getElementById("firsthalf");
   var element2 = document.getElementById("passhalf");
   element.classList.toggle("active");
   element2.classList.toggle("active");
}
function swipeup() {
   var element = document.getElementById("signupscreen");
   var element2 = document.getElementById("loginscreen");
   element.classList.toggle("active");
   element2.classList.toggle("active");
}
