import axios from 'axios';

const signUpPath = '/auth/login';

export async function handleSignIn(event, responseSetter) {
    event.preventDefault();
    console.log(event.target)
    const formData = new FormData(event.target);
    const email = formData.get('email');
    const password = formData.get('password');
    console.log(email)
    if (!email.includes('@')) {
        console.log('Email is invalid');
        return;
    }

    if (email === '' || password === '') {
        console.log('Email or password is empty');
    }
    else {
        await axios.post(signUpPath, {
            'email': email,
            'password': password
        })
        .then(function (response) {
            alert('Response: ' + response.data.message);
            console.log(response.data);
            responseSetter(response.data.message);
        })
        .catch(function (error) {
            console.error(error);
        });
    }       
};