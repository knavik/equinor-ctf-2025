## Challenge Description
```
There are monsters everywhere and they are hungry for cookies. 
But you are a brave little cookie and you want to fight back. 
You have to find the solution in the cookie jar.
Sometimes you need to look at what is going on in the browser to find a flag.
```

## Solution

1. Start by registering a user
2. Login to the user

Clicking on the `Admin` navigation menu shows the following error:
```
You are not an admin.
```

Opening DevTools (F12) on Chrome we see that there is a cookie called `role`.
![Cookies!](image.png)

We can change the value from `user` to `admin`

![alt text](image-1.png)

By refreshing the webpage we see that we have access to the admin panel

**FLAG:** `EPT{Cookies_4_the_Win!!}`