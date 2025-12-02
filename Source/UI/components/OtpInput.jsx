import React, { useState } from 'react';
import { AuthAPI } from '../api/AuthAPI';

export default function OtpInput({ username }) {
    const [otp, setOtp] = useState('');

    const handleVerify = async () => {
        const res = await AuthAPI.verifyOtp(username, otp);
        alert(res ? "Login Success" : "OTP Failed");
    };

    return (
        <div>
            <input placeholder="Enter OTP" onChange={e => setOtp(e.target.value)} />
            <button onClick={handleVerify}>Verify OTP</button>
        </div>
    );
}
