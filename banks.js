// const accname = document.getElementById('accname');
// const dog = document.createElement('p')
const getAccountNumbers = () => {
    fetch( `https://api.paystack.co/bank/` , {
        headers: {
            "Authorization" : "Bearer sk_test_d1b83ae902e7135db7d879d7121ec665e0a8243d" 
         }
      }).then(response => {
        console.log(response);
        if (!response.ok) {
            throw Error("Invalid Api Request");
        }
        return response.json();
      })
      .then(data => {
        console.log(data.data)
        const html = data.data.map(user => {
            return `<option value="${user.code}"> ${user.name} </option>`
        }).join(" ");
        
        document.querySelector("#app").insertAdjacentHTML("afterbegin", html );
      }).catch(error => {
        alert(error)
      } )


}

getAccountNumbers();





