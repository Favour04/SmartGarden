import React, { useState, useRef } from 'react';
import './Auth.css'
import { handleSignUp } from './signuphandler';
import { handleSignIn } from './signinhandler';

function Auth() {
    const [signUpdata, setSignUp] = useState({
        email:'',
        username:'' ,
        password:'',
        confirm:''
    });
    const [signIndata, setSignIn] = useState({
        email:'',
        password:''
    });

    const [responseMessage, setresponseMessage] = useState('')

    function handleSignUpChange(event) {
        const { name, value } = event.target;
        setSignUp((prevState) => ({
            ...prevState,
            [name]: value
        }));
    }

    function handleSignInChange(event) {
        const { name, value } = event.target;
        setSignIn((prevState) => ({
            ...prevState,
            [name]: value
        }));
    }

    let container = useRef(null)

    function toggle() {
        if (container.current){
            container.current.classList.toggle('sign-in');
            container.current.classList.toggle('sign-up');
        }
        }

    React.useEffect(() => {
        if (container.current) {
            container.current.classList.add('sign-in');
        }
    }, []);


    
    return (
        <div ref={container} id="container" className="container">
            {/* FORM SECTION */}
            <div className="row">
			    {/* SIGN UP */}
			    <div className="col align-items-center flex-col sign-up">
				    <div className="form-wrapper align-items-center">
					    <form className="form sign-up" onSubmit={(event) => handleSignUp(event, setresponseMessage)}>
						    <div className="input-group">
							    <i className='bx bxs-user'></i>
							    <input
                                name="username"
                                type="text" 
                                placeholder="Username"
                                value = {signUpdata.username}
                                onChange={handleSignUpChange}
                                />
						    </div>
						    <div className="input-group">
							    <i className='bx bx-mail-send'></i>
							    <input
                                name="email"
                                type="email" 
                                placeholder="Email"
                                value = {signUpdata.email}
                                onChange={handleSignUpChange}
                                />
						    </div>
						    <div className="input-group">
							    <i className='bx bxs-lock-alt'></i>
							    <input
                                name="password"
                                type="password" 
                                placeholder="Password"
                                value = {signUpdata.password}
                                onChange={handleSignUpChange}
                                />
						    </div>
						    <div className="input-group">
							    <i className='bx bxs-lock-alt'></i>
							    <input
                                name="confirm"
                                type="password" 
                                placeholder="Confirm password"
                                value = {signUpdata.confirm}
                                onChange={handleSignUpChange}
                                />
						    </div>
						    <button>
							    Sign up
						    </button>
                            <div><p>{responseMessage && responseMessage}</p></div>
						    <p>
							    <span>
								    Already have an account? 
							    </span>
							    <b 
                                onClick={toggle} 
                                className="pointer">
								    Sign in here
							    </b>
						    </p>
					    </form>
				    </div>
			    </div>
			    {/* END SIGN UP */}

			    {/* SIGN IN */}
                <div className="col align-items-center flex-col sign-in">
				    <div className="form-wrapper align-items-center">
					    <form className="form sign-in" onSubmit={(event) => handleSignIn(event, setresponseMessage)}>
						    <div className="input-group">
							    <i className='bx bxs-user'></i>
							    <input
                                 name="email"
                                 type="email"
                                 placeholder="Email"
                                 value = {signIndata.email}
                                 onChange={handleSignInChange}
                                 />
						    </div>
						    <div className="input-group">
							    <i className='bx bxs-lock-alt'></i>
							    <input
                                 name="password"
                                 type="password" 
                                 placeholder="Password"
                                 value = {signIndata.password}
                                 onChange={handleSignInChange}
                                 />
						    </div>
						    <button>
							    Sign in
						    </button>
                            <div><p>{responseMessage && responseMessage}</p></div>
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
                                onClick={toggle} 
                                className="pointer">
								    Sign up here
							    </b>
						    </p>
					    </form>
                    </div>
				    <div className="form-wrapper">
                    </div>    
                </div>
                {/* {END OF SIGN IN} */}
            </div>
            {/* END OF FORM SECTION */}
        
            {/* CONTENT SECTION */}
		    <div className="row content-row">
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

                {/* SIGN UP CONTENT */}
                <div className="col align-items-center flex-col">
				    <div className="img sign-up"></div>
				    <div className="text sign-up">
					    <h2>
						    Join with us
					    </h2>
	
				    </div>
			    </div>
			    {/* END SIGN UP CONTENT */}
		    </div>
		    {/* END CONTENT SECTION */}
        </div>
    );
};

export default Auth;
