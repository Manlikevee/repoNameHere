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
    alert(response.data.fullname)
        // Create element:
const vi = response.data.fullname
const f_name = response.data.firstname
const l_name = response.data.lastname
const m_name = response.data.middlename
const lga = response.data.lga_of_origin
const nationality = response.data.nationality
const addresss = response.data.lga_of_origin
const nin = response.data.nin
const dob = response.data.dob
const arraytest = response.data.email[1]
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



