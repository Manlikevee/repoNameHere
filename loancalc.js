var principal = 0;
var interestRate = 0;
var timesCompounded = 0;
var termOfLoan = 0;
var amount = 0;

pamount.addEventListener("input", simpleInterest);
interest.addEventListener("input", simpleInterest);
tenur.addEventListener("input", simpleInterest);
edate.addEventListener("input", simpleInterest);
mdate.addEventListener("input", simpleInterest);


let today = new Date().toISOString().substr(0, 10);
document.querySelector("#edate").value = today;




function simpleInterest() {
  console.log("yes")
  var principal = parseFloat(document.getElementById("pamount").value);
  var interestRate = parseFloat(document.getElementById("interest").value);
  interestRate = interestRate / 100;
  var termOfLoan = parseFloat(document.getElementById("tenur").value);
  var today = new Date();
  var tomorrow = new Date();
  tomorrow.setDate(today.getDate() + termOfLoan);

  var days = document.getElementById("tenur").value;
  var date = new Date(document.getElementById("edate").value);
  date.setDate(date.getDate() + parseInt(days));
  document.getElementById("mdate").valueAsDate = date;
//   var seconddate =  date.setDate(date.getDate() - parseInt(days));
//   document.getElementById("edate").valueAsDate = date;
  

  var simpleInt = principal * interestRate * termOfLoan / 365;
  var amount = (principal + simpleInt).toFixed(2);
  document.getElementById("iamt").value = simpleInt.toFixed(2);
  document.getElementById("mdamt").value =  amount;
//   document.getElementById("mdate").value = tomorrow;
  console.log(tomorrow)
}