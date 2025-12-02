export const AuthAPI = {
    login: async (username, password) => {
        // Dummy API simulation
        return username && password ? {status: "MFA_REQUIRED"} : {status: "FAILURE"};
    },
    verifyOtp: async (username, otp) => {
        return otp === "123456";  // Dummy check
    }
};
