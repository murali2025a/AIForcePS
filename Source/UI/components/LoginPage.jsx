import React, { useState } from 'react';
import { AuthAPI } from '../api/AuthAPI';
import OtpInput from './OtpInput';

export default function LoginPage() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [showOtp, setShowOtp] = useState(false);

    const handleLogin = async () => {
        const res = await AuthAPI.login(username, password);
        if (res.status === "MFA_REQUIRED") setShowOtp(true);
        else alert(res.status);
    };

    return (
        <div>
            <input placeholder="Username" onChange={e => setUsername(e.target.value)} />
            <input placeholder="Password" type="password" onChange={e => setPassword(e.target.value)} />
            <button onClick={handleLogin}>Login</button>
            {showOtp && <OtpInput username={username} />}
        </div>
    );
}
