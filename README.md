OTP Manager
===========
This app generates one-time passwords (OTPs) for accounts registered by the user.  Instead of relying on having physical possession of something such as a mobile phone or hardware key, this app allows a user to generate OTPs from anywhere with internet access.

## Usage
To register a new account, simply click on `Add account` and enter a name and the secret key provided for the account.  (Spaces in the key do not matter.)

Refresh the page to generate new OTP codes.

## Security considerations
Firstly, there's no getting away from the fact that this app rather defeats the purpose of 2-factor authentication, as it is no longer necessary for the user to be in physical possession of an object such as a mobile phone or hardware key.

Notwithstanding that fundamental issue, there are a number of security features and potential vulnerabilities to be aware of before using this app.

- Clearly, it is essential to use a strong, unique password with this app.  Passwords are stored in the application database as hashes generated using SHA256, and not stored in the database directly.
- It is very important to remember this password.  While a user can reset their account by email, their keys would still be encrypted based on their original password, so would be inaccessible.
- OTP keys added by the user are stored encrypted in the database.  They are encrypted using a master key derived from the user's password, so they cannot be accessed either by the app's owner or an attacker in possession of the database and/or the application source code.
- The user's master key is stored in plain text on the session cookie.  This should not be a significant vulnerability as an attacker would need to be properly authenticated in order to obtain the encrypted keys from the database.
- An attacker should not be able to derive the user's password from the master key, as the key is generated using a strong irreversible hashing algorithm.
- Nonetheless, a determined attacker could in theory intercept the session cookie.  Session protection is set to `strong` in order to prevent an attacker from copying the cookie and using it to impersonate the user from another computer or IP address.

## Backend admin
To create a user:
`flask create_user --username user@example.com --password password`

To delete a user:
`flask delete_user --username user@example.com`

## Planned features
- Create new accounts using otp QR codes.
- Automatically refresh OTP codes based on time.
