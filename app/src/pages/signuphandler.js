import axios from 'axios'

const signUpPath = '/auth/signup';

export async function handleSignUp(event, responseSetter) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const username = formData.get('username');
    const email = formData.get('email');
    const password = formData.get('password');

    console.log(email)
    if (!email.includes('@')) {
        console.log('Email is invalid');
        return;
    }

    if (email === '' || password === '') {
        console.log('Email or password is empty');
        return;
    }
    else if (password.length < 8) {
        console.log('Email or password is too short');
        return;
    }
    else {
        await axios.post(signUpPath, {
            'email': email,
            'password': password,
            'username': username
        })
        .then(function (response) {
            alert('Response: ' + response.data.message);
            responseSetter(response.data.message)
            console.log(response.data);
        })
        .catch(function (error) {
            console.error(error);
        });
    }       
};