var principal = 10000;
var interestRate = 12;
var timesCompounded = 1;
var termOfLoan = 365;
var top = 0;

var newrate = interestRate / 100;
var newsc = 1 + newrate;
var raised = (newsc)

var compountIntRaised = (raised)
var compountIntTop = (termOfLoan / 365 );
var compountIntToper = (termOfLoan / 30.4167 );
var men = Math.pow(compountIntRaised, compountIntTop);
var tot = (principal * men).toFixed(2)
var interest = (tot - principal).toFixed(2)
console.log(interest)
console.log(tot)

