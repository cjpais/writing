# Handling Universal Links in SwiftUI

*Last Updated: Nov 2020*

*iOS SDK 14.2*

I struggled for a long time to figure out how to implement Universal Links properly. 
In addition there was very little documentation on how you open into your app from a QR code. 
This guide serves as a way to implement the base level of Universal Link functionality as 
well as handling QR codes.

## Overview

[Universal Links](https://developer.apple.com/ios/universal-links/) allow you to redirect users
from a webpage directly into your app's context. It is applicable only for iOS devices. 
With Universal Links you can maintain the context the user previously had on the webpage
but give them a native experience.

By adding a specific file (`apple-app-site-association`) on your webserver, you can support
Universal Links relatively easily. When your app is downloaded the user's device will query
your server for this file. Once it's done this, any time the user visits one of the routes provided
in this file, they will be directed into your native experience.

**Steps to Implement**

1. Add Apple App Site Association (AASA)
   * Validate AASA 
2. Add Entitlements to App
   * Get Team ID
3. Use onOpenURL to handle Links
4. Use onContinueUserActivity to handle QR Codes
5. Handle Routing 
6. Testing Universal Links
   * Notes Link
   * Web Link
   * QR Link 

## Adding Apple App Site Association

### Validating AASA

There are a few tools you can use to validate your AASA after you have it on your server.
Even if you validate your AASA you may run into some frustration, but it is a good thing
to check off your list.

To have a valid AASA you need the following

* Have it named `apple-app-site-association`
* Have it served over HTTPS
* Have it be valid JSON
* Have it served at the root directory or `/.well-known` directory

The [Branch AASA Validator](https://branch.io/resources/aasa-validator/) is the best I found. 
Just put in your domain and it will check everything for you. You should see all green like the 
below if it's good!

![](aasa_valid.png)


[Apple has their own validation tool](https://search.developer.apple.com/appsearch-validation-tool), however it doesn't think my App is valid 🤷🏽‍♂️. I wouldn't recommend it. 
It just added to the confusion of the process.




### References

[Support Universal Links - Apple](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/UniversalLinks.html)
