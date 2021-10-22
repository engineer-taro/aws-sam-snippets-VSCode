# aws-sam-snippets-VSCode

[Japanese README](README_ja.md)

This repository is under development to comfortably write SAM templates in VSCode.
It is currently under development, so there are many things that are not supported, but we plan to push it out gradually starting with the minimum functionality.
Also, CloudFormation is not covered by this repository, so please use another extension dedicated to CloudFormation.

# How to use

![use-sample.gif](images/use-sample.gif)  
You can get a snippet by typing `sam` followed by a letter.

\*To avoid conflicts with other extensions, we decided to use a string starting with `sam`.

# Release Info

## 1.0.0

First release.  
Add the description following Type: to the snippet.  
This will be up to the property name of Properties.

# About the progress of development

We are currently in phase 1.  
The order in which features will be added is planned to be as follows

## Phase 1

Add the description following Type: to the snippet.  
This will be up to the property name of Properties.

## Phase 2 Now

[EventSource](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventsource. html) and other frequently used snippets.

## Phase 3

[CorsConfiguration](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-api- corsconfiguration.html) Target those that are not frequently described.

## Phase 4 and later

Necessary functions will be added sequentially.
