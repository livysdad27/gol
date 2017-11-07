#Regression Test/Sign-Off Notes

###This is what is being done by the Product Owner to sign-off on stories.  This list is dynamic and will change periodically.

1. Patient - Sign into [https://th.dev.provinnovate.com/dogfood](https://th.dev.provinnovate.com/dogfood) as TeleHeathPresenterTZ in one window using the dogfood endpoint.  Note that anyone with the presenter role in AD will work.
    1. Create a conference
2. Patient - waiting room
    1. Click on the conference to start it.
    2. The camera should light up.
    3. Double-check waiting room layout
    4. Ask a question
    5. Test My Connection - click retest, then proceed
3. Provider - joins conference
    1. Open the conference from an incognito browser window, and sign in using your p number.
    2. In the conference URL, replace "conference" with "visit" to ensure that endpoint works.  It should look something like: [https://th.dev.provinnovate.com/visit/bNjiWOjc](https://th.dev.provinnovate.com/visit/bNjiWOjc)
    3. Conference should switch to audio\video view
    4. This should be a first run from the browser/incognito window - WebRTC asks for use of the camera and mic *
5. Patient and provider 
    1. Double check layout of video windows look ok
    2. Enable\disable fullscreen
    3. Enable\disable video feed - changes should be reflected on both sides.
    4. Mute\unmute
6. Open/Check the Chat Window
    1. Make sure it flies out.
    2. Enter some text and ensure that populates.
    3. Enter text that is bigger than the window.
    4. Enter so many messages that messages scroll up.
    5. After scrolling up to review them, enter a new message to ensure the focus moves down to the bottom of the chat window.
    6. close the chat window
    7. Reopen it to make sure chat stuff is still there.
    8. Check that when typing, a notification appears on the other side.
7. Disconnect one side from video (one browser window)
8. Reconnect the conference - all is well?

###Other Checks
* Rerun the checks above while disconnecting one side (close of browser and unplug/disable networking) on both sides in different parts of the process.
* Rerun the checks above and disconnect network from either side, reconnect to ensure that the reconnect happens.
* Login as two Telepresenters, see what happens
* Login as two Providers, see what happens.
* Logout on Telepresenter side first and then Provider side first.
* Ensure that feedback is visible in splunk somewhere.
