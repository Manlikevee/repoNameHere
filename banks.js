const displayLoading = () => {
  let overlay = document.getElementsByClassName('loading-overlay')[0]
  overlay.classList.toggle('is-active')
};

const hideLoading = () => {
  let overlay = document.getElementsByClassName('loading-overlay')[0]

  // 👇️ hides element (still takes up space on page)
  overlay.classList.remove('is-active')
};

// const accname = document.getElementById('accname');
// const dog = document.createElement('p')
const getAccountNumbers = () => {
    displayLoading();
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
        hideLoading();

      }).catch(error => {
        alert(error)
        hideLoading();
      } )


}

getAccountNumbers();






