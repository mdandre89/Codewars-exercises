function password(str) {return /^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).{8,}$/.test(str) ? true : false}