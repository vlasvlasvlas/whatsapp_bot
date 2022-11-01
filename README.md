# whatsapp_bot
simple test of whatsapp bot for local government web page

![imagen](https://user-images.githubusercontent.com/4071796/199302578-d9ec2998-a9e8-426b-b8f6-99f24a58766d.png)

# Details

Main objective:
- simple test of a python based whatsapp bot

arq:
- based on python (3.8), flask, and ngrok, who communicates to Twilio

## so:

human question / input:
- human -> whatsapp phone number (twilio) -> ngrok -> flask resource ( backend POST /bot )

bot answer / feedback :
- flask resource response ( backend POST /bot response ) -> ngrok -> twilio -> human 
