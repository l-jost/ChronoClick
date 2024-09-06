# Device Requirements

Initial draft for the device requirements. This is subject to change!

## Functional Requirements

| ID | Group | Name | Requirement | Rational |
|----|-------|------|-------------|----------|
|REQ-01-01|Timer|Count down|The device shall support countdown intervals ranging from 10 minute up to 30 days.|Accommodates various user tasks requiring different time frames.|
|REQ-01-02|Timer|Count up|The device shall support count-up functionality, continuing up to 30 days.|Enables tracking elapsed time since the last action.|
|REQ-01-03|Timer|Count up / down|The device shall count down, prompt the user that the timer expired and then count up.|To show how long overdue the action is.|
|REQ-01-04|Timer|Start / Reset|The device shall have an option to start and reset the timer using a single button|Multiple functions with a minimal interface.|
|REQ-01-05|Interface|Time display|The device shall feature a display that clearly shows time remaining, timer expired status, or count-up time. In addition the the device identification.|The user needs to know!|
|REQ-01-06|Interface|Color Change|The device shall be capable of displaying at least 2 colors.| Improves user recognition and promptness in responding to alerts.|
|REQ-01-07|Interface|Low battery indication|The device shall provide a low battery warning when the battery level drops below 20%, using visual indicators.|Ensures users have adequate time to replace the battery before complete depletion.|
|REQ-01-08|Interface|Single Button|The device shall be operated with a single button.|Very simple but effective interface.|
|REQ-01-09|Interface|Haptic Feedback|The press of the button should have a haptic feedback.|Makes it nicer to use.|
|REQ-01-10|Configuration|App Configuration|The device shall be configurable using a mobile application compatible with both Android.|"Do You Guys Not Have Phones?"|
|REQ-01-11|Configuration|Custom timer intervals|The device shall allow users to set custom time intervals for counting down.|Users need to set different timers for various tasks.|
|REQ-01-12|Configuration|Up / Down configuration|The device shall allow users to select counting modes (count up, count down, or automatic transition) via the mobile app.|Allows user control over timer functionalities.|
|REQ-01-13|Configuration|Persistence|The device shall retain all user configurations and settings in non-volatile memory, ensuring persistence even when the battery is replaced or fully depleted.|Prevents the need for reconfiguration after battery changes, enhancing user convenience.|


## Non-function Requirements
| ID | Group | Name | Requirement | Rational |
|----|-------|------|-------------|----------|
|REQ-02-01|Performance|Accuracy|The device shall maintain time accuracy within ±1 second per minute, ±1 minute per hour, and ±1 hour per day.|Clear and testable accuracy specification.|
|REQ-02-02|Performance|Run time|The device shall achieve a minimum battery life of 1 year under typical usage conditions, including continuous timer operation with periodic alerts.|We don't want to replace the battery often.|
|REQ-02-03|Usability|Display accuracy|The device shall adjust display accuracy based on timer settings: display time in seconds for intervals up to 60 minutes, in minutes for intervals up to 24 hours, and in hours for intervals up to 30 days.|Prevents unnecessary precision for longer timers, conserving power and simplifying the display.|
|REQ-02-04|Usability|User|The device shall be simple to use, with setup taking less than 2 minutes.|The device should be easily accessible and intuitive for all users, including those with limited technical skills.|
|REQ-02-05|Usability|Size|The device shall have a diameter not exceeding 30mm and a thickness not exceeding 8mm.|We want something that we can put on many things|
|REQ-02-06|Usability|Battery Replacement|The device shall be designed to allow easy battery replacement without tools.|Nobody wants to use tools to change batteries.|
|REQ-02-07|Usability|Identification|The device shall allow users to assign a unique name or icon to each device via the mobile app, which will be displayed on the screen.|To differentiate between multiple devices in the same location.|
|REQ-02-08|Durability|Drop resistance|The device shall comply with IEC 60068-2-31, ensuring it can withstand drops from a height of 1 meter onto a hard surface without functional damage.|We all drop things.|
|REQ-02-09|Durability|Dust and water intrusion|The device shall be IP4X rated|This ensures the device is robust enough for daily use in different environments.|

## Technical Requirements
| ID | Group | Name | Requirement | Rational |
|----|-------|------|-------------|----------|
|REQ-03-01|Power|Power Source|The device shall be powered by a removable CR2032 battery.|Very easy to replace and cheap.|
|REQ-03-02|Interface|Display|The device should feature a round display.|Looks good :)|
|REQ-03-03|Setup|NFC|The device shall be configured using NFC.|Very low power and technology inside most phones.|
