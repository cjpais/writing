# Handling Universal Links in SwiftUI

*Last Updated: Nov 2020*

*Using: iOS SDK 14.2*

I struggled for a long time to figure out how to implement Universal Links properly. 
In addition there was very little documentation on how you open into your app from a QR code. 
This guide serves as a way to implement the base level of Universal Link functionality as 
well as handling QR codes. 

## Overview

[Universal Links](https://developer.apple.com/ios/universal-links/) allow you to redirect users
from a webpage directly into your app's context. It is applicable only for iOS devices. 
With Universal Links you can maintain the context the user previously had on the webpage
but give them a native experience. Often times this is called deep linking. 

By adding a specific file (`apple-app-site-association`) on your webserver, you can support
Universal Links relatively easily. When your app is downloaded the user's device will query
your server for this file. Once it's done this, any time the user visits one of the routes provided
in this file, they will be directed into your native experience.

**Steps to Implement**

1. Add Apple App Site Association (AASA)
   * Validate AASA 
2. Add Entitlements to App
3. Use `onOpenURL` to handle Links
4. Use `onContinueUserActivity` to handle QR Codes
5. Handle Routing 
6. Testing Universal Links
   * Notes Link
   * Web Link
   * QR Link 

## Adding Apple App Site Association

Before working on the App at all we want to have everything set up for the app to support our 
Universal Link. The first thing to do is create the `apple-app-site-association` (AASA) and 
serve it. This will allow Apple to know when to open your app.

### Creating your AASA

For example [my AASA](https://digitaldirtbag.xyz/apple-app-site-association) looks like this:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "UWFLB4GC25.com.pais.rockaholic",
        "paths": ["/route/*"]
      }
    ]
  },
  "activitycontinuation": {
    "apps": [
      "UWFLB4GC25.com.pais.rockaholic"
    ]
  }
}
```

Breaking this down you only need to do two things.

1. Change the `appID` to be your `TEAM_ID.APP_BUNDLE_ID`
   * My `TEAM_ID = UWFLB4GC25` 
     * Your team ID can be found [here](https://developer.apple.com/account/#/membership)
     * Alternatively navigate to `developer.apple.com` > Accounts > Membership.
   * My `APP_BUNDLE_ID = com.pais.rockaholic` 
2. Change the `paths` to be the URL's you want to treat as universal links.
   * I will be handling all paths starting with `route`
   * For more information see [Apple's Documentation](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/UniversalLinks.html) (it's quite good)

> `activitycontinuation` may not be necessary here, but according to [this blog](https://medium.com/@barsh/my-first-date-with-ios-universal-links-90dfabc88bb8) it was.
> If you run into trouble with your Universal Links you may want to add this too.

### Serving your AASA

Once you have your `apple-app-site-association` created, you will want to add this file 
to your webserver.

The requirements for serving it are as follows:

* Have it named `apple-app-site-association`
* Have it served over HTTPS
* Have it served with the `Content-Type` header set to `application/json`
* Have it be valid JSON
* Have it served at the root directory or `/.well-known` directory

### Validating AASA

There are a few tools you can use to validate your AASA after you have it on your server.
Even if you validate your AASA you may run into some frustration, but it is a good thing
to check off your list.

The [Branch AASA Validator](https://branch.io/resources/aasa-validator/) is the best I found. 
Just put in your domain and it will check everything for you. You should see all green like the 
below if it's good!

![](aasa_valid.png)

[Apple has their own validation tool](https://search.developer.apple.com/appsearch-validation-tool), however it doesn't think my App is valid 🤷🏽‍♂️. I wouldn't recommend it. 
It just added to the confusion of the process.

## Add Entitlements to App

## Using `onOpenURL` to handle links

`onOpenURL` is a callback which will be called when a user taps a link that matches the 
specified `paths` in your AASA. This should happen from a webpage, the notes application, etc.
However this will only happen when the link is opened in Safari as far as I can tell. If you want
to link from your site say `www.example.com` to `www.example.com/thing_to_handle/5` make sure
you specify the whole URL path instead of the shorthand `/thing_to_handle/5`. If you do the 
shorthand your Universal Link *will not* open by default. 

In your main `App` file you will have the `body: Scene` variable. You will want to handle `onOpenURL` within this. I've done it as my `TabView` get's rendered. So far this has worked.

```swift
    var body: some Scene {
        WindowGroup {
            TabView(selection: $selectedTab) {
                ExploreView(state: state)
                    .tag(TabIdentifier.explore)
                
                ExploreRoutesView(state: state)
                    .tag(TabIdentifier.route)
    
                AddView()
                    .tag(TabIdentifier.add)  
                
            }.onOpenURL { url in
                routeURL(url)
            }
        }
    }
```

You can see when getting the `onOpenURL` callback I am calling into a function `routeURL` which 
will handle the URL path to get to the same context as the webpage.

## Using `onContinueUserActivity`

If you generated a QR code which points to a URL above, you might notice that the QR code
opens your application but does not direct to the right view. In fact it doesn't call
`onOpenURL` at all. This left me puzzled for a while, but eventually figured out it should
be handled by `onContinueUserActivity` instead. So you can add a similar handler there.

You will want to use the type `NSUserActivityTypeBrowsingWeb` to pass to this function.
QR Codes will be opened in Safari in the background then directed to your app if that
path is handled by your app.

Unlike `onOpenURL` you will get an `NSUserActivity` in the callback. Fortunately it has
a very easy way to get the URL from it, and you can handle routing from there. 

```swift
    var body: some Scene {
        WindowGroup {
            TabView(selection: $selectedTab) {
                ExploreView(state: state)
                    .tag(TabIdentifier.explore)
                
                ExploreRoutesView(state: state)
                    .tag(TabIdentifier.route)
    
                AddView()
                    .tag(TabIdentifier.add)  
                
            }.onOpenURL { url in
                routeURL(url)
            }
            .onContinueUserActivity(NSUserActivityTypeBrowsingWeb, perform: { activity in
                routeURL(activity.webpageURL!)
            })
        }
    }
```


## Handle Routing 

Best to check out [Donny Wals guide](https://www.donnywals.com/handling-deeplinks-in-ios-14-with-onopenurl/) on handling Universal Links. 
He has some great examples on how
you can handle routing in your own app. I ended up using a similar approach. 

## Testing

I would test a few things. 

### Notes App

First would be in the Notes app. This seems like the most surefire way to see if you're on the
right path.
For me the Universal Link from the Notes app always worked. That is I had a note with the link
pasted into it. When I clicked the link it went directly to the app and where I wanted.

It should looks something like:

![](from_notes.mp4)

### Your Website

Second would be to test on your website. Ensure a link on your website will directly open your app.
As mentioned earlier make sure you are using the full URL (https://www.yourdomain.com) path or this won't work. Also if you type
the URL directly into Safari it will not launch your app. This is because if a user directly is
typing in the URL they are probably fine with the mobile experience, however if they are tapping a
link they are probably fine with the app launching.

It should look something like:

![](from_site.mp4)

### From a QR Code

Third would be to check the QR code. Open the camera app and point it to a QR Code which encodes
the URL you want to open in the app.

It should looks something like:

![](from_qr.mp4)

## Contact

There are some finicky things here which were not covered, if you run into something weird
don't hesitate to contact me `cj@cjpais.com`