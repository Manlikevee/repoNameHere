const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');


const fname = document.getElementById('in1');
const mname = document.getElementById('in2'); 
const lname = document.getElementById('in3');
const dob = document.getElementById('in4');



form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
    
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
    const usernameValue = username.value.trim().toLowerCase();
    const emailValue = email.value.trim().toLowerCase();
    const passwordValue = password.value.trim().toLowerCase();
    const password2Value = password2.value.trim().toLowerCase();


    const fname2 = fname.value.trim().toLowerCase();
    const mname2 = mname.value.trim().toLowerCase();
    const lname2 = lname.value.trim().toLowerCase();
    const dob2 = dob.value.trim();
    



    if(usernameValue === '') {
        setError(username, 'first name is required');
    }  else if (usernameValue !== fname2) {
        setError(username, "first name doesnt match");
    }
         else {
        setSuccess(username);
    }

    if(emailValue === '') {
        setError(email, 'last name is required');
    } else if (emailValue !== lname2) {
        setError(email, "Last Name doesn't match");
    } else {
        setSuccess(email);
    }

    if(password2Value === '') {
        setError(password2, 'dob is required');
    } else if (password2Value !== mname2) {
        setError(password2, "Last Name doesn't match");
    } else {
        setSuccess(password2);
    }

    if(passwordValue === '') {
        setError(password, 'dob is required');
    } else if (passwordValue !== dob2) {
        setError(password, "Dob Doesnt Match Bvn Details");
    } else {
        setSuccess(password);
    }




    if (document.querySelectorAll('.form_body_column')[0].classList.contains('success') && document.querySelectorAll('.form_body_column')[1].classList.contains('success') && document.querySelectorAll('.form_body_column')[2].classList.contains('success') && document.querySelectorAll('.form_body_column')[3].classList.contains('success')) {
        console.log('trues')
        form.submit()
    }
    else {
        console.log('almost')
    }



};