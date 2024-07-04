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
             <div className="col align-items-center flex-col sign-in">
				    <div className="form-wrapper align-items-center">
					    <div className="form sign-in">
						    <div className="input-group">
							    <i className='bx bxs-user'></i>
							    <input
                                 type="email"
                                 placeholder="Email"
                                 value = {email}
                                 onChange={(event) => setEmail(event.target.value)}
                                 />
						    </div>
						    <div className="input-group">
							    <i className='bx bxs-lock-alt'></i>
							    <input 
                                 type="password" 
                                 placeholder="Password"
                                 value = {password}
                                 onChange={(event) => setPassword(event.target.value)}
                                 />
						    </div>
						    <button onClick={handleSignIn}>
							    Sign in
						    </button>
						    <p>
							    <b>
								    Forgot password?
							    </b>
						    </p>
						    <p>
							    <span>
								    Don't have an account?
							    </span>
							    <b 
                                onClick={() => {
                                    let container = document.getElementById('container')
                                    container.classList.toggle('sign-in')
                                    container.classList.toggle('sign-up')
                                }} 
                                className="pointer">
								    Sign up here
							    </b>
                                <div><p>{onClick && onClick}</p></div>
						    </p>
					    </div>
                    </div>
				    <div className="form-wrapper">
                    </div>
                     {/* SIGN IN CONTENT */}
                    <div className="col align-items-center flex-col">
                        <div className="text sign-in">
                            <h2>
                                Smart Garden
                            </h2>
                        </div>
                        <div className="img sign-in"></div>
                    </div>
                    {/* END OF SIGN IN CONTENT */}
                    </div>
        </div>
    );
};

export default Login;
