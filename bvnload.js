// function myFunction() {

//     const account_number = document.getElementById("myText").value;
//     const bank_number = document.getElementById("subwaystation").value;
//     console.log(`my variable is ${account_number}`);
//     console.log(`my variable is ${bank_number}`);
   
    
//     myFunctions(account_number);
//   }
 



function myFunctions() {
const options = {
method: 'POST',
headers: {
  Accept: 'application/x-www-form-urlencoded',
  'Content-Type': 'application/x-www-form-urlencoded',
  Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MzE5MWQ3ODAzNGQ2NzkzZDQ4Y2VmMmYiLCJpYXQiOjE2NjI1OTAzMjh9.75IthXbKWw3Pyl_oAQ9hRiZAALdv3ejk8GctmS4mnVM'
},
body: new URLSearchParams({bvn: '12212223121'})

};


fetch('https://api.okra.ng/v2/sandbox/products/kyc/bvn-verify', options)
.then(response => response.json())
.then(response => {
    console.log(response)
    alert(response.data.identity.fullname)
        // Create element:
const vi = response.data.identity.fullname
const f_name = response.data.identity.firstname
const l_name = response.data.identity.lastname
const m_name = response.data.identity.middlename
const lga = response.data.identity.lga_of_origin
const nationality = response.data.identity.nationality
const addresss = response.data.identity.lga_of_origin
const nin = response.data.identity.nin
const dob = response.data.identity.dob
const arraytest = response.data.identity.email[1]
const para = document.createElement("p");
para.innerHTML = `my variable is ${vi} , <p>  ${addresss}  </p> , <p>  ${nin}  </p>,  <p>  ${dob}  </p> ,  <p>  ${nationality}  </p>, <p>  ${lga}  </p>  `;
console.log(para)
const dates = new Date()
const datajob =`${dob}`;
const final = datajob.split("T");
const finalme = final[0];
console.log(final);
console.log(finalme);
console.log(final);
console.log(arraytest)
const fullDates = dates.toLocaleString('en-US')
console.log(fullDates)
// Append to another element:
document.getElementById("in1").value = `${f_name}`;
document.getElementById("in2").value = `${m_name}`;
document.getElementById("in3").value = `${l_name}`;
document.getElementById("in4").value = `${finalme}`;
} )
.catch(err => console.error(err));


}
myFunctions();



