import React, { useState } from 'react';
import axios from 'axios';

const signUpPath = '/auth/login';

function Login() {
    
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [responseMessage, setresponseMessage] = useState('')

    async function handleSignUp(event) {
        event.preventDefault(); 
        console.log(email)
        if (!email.includes('@')) {
            console.log('Email is invalid');
            return;
        }

        if (email === '' || password === '') {
            console.log('Email or password is empty');
            return;
        }
        else {
            await axios.post(signUpPath, {
                'email': email,
                'password': password
            })
            .then(function (response) {
                alert('Response: ' + response.data.message);
                setresponseMessage(response.data.message)
                console.log(response.data);
            })
            .catch(function (error) {
                console.error(error);
            });
        }       
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleSignUp}>
                <label>
                    Email:
                    <br/>
                    <input
                    type="email"
                    placeholder="Email"
                    value = {email}
                    onChange = {(event) => setEmail(event.target.value)}
                />
                </label>
                <br/>
                <label>
                    Password:
                    <br/>
                    <input
                    type = "password"
                    placeholder='Password'
                    value = {password}
                    onChange = {(event) => setPassword(event.target.value)}
                />
                </label>
                <br/>
                <button type="submit">Login</button>
            </form>
            <p>{responseMessage && 'Welcome' + responseMessage}</p>
        </div>
    );
};

export default Login;
