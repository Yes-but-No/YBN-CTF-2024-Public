The `/nuke` endpoint requires an admin role. We can get the admin role from the api endpoint. 
Simply visit `/api/users/2/roles` with a `POST` to assign the admin role to the user. 
Then we can visit `/nuke` to get the flag.
