
from flask import Flask, request, abort
from flask_sslify import SSLify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)
sslify = SSLify(app)

# set LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variable
channel_secret = '256ffc324a9dae86ebb2036e816a7f1f'
channel_access_token = 'DBbr1bR0GAPMDtB0nmZUgugF8qsP/SxN6J3+ysRlD5XpC55kqcljAOF5dh0gHFay7o/NbVCNYTbpS1JWZiGEMmocmW/0yIV1XytI/z2jKeXtsC420gPjps5VfjJsPOijeQmue43vxblLFuX79D1eFQdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@app.route("/test", methods=['GET'])
def test():
    return "Ok test"


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     # extract user's message
#     user_text = event.message.text

#     # check if user's message is "test"
#     if user_text == "test":
#         # reply to user
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text="This is a test message")
#         )

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # extract user's message
    user_text = event.message.text

    # check if user's message is anything
    if user_text.strip():  # Check if the message is not empty or contains only whitespace
        # reply to user with "Ok"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Ok")
        )


if __name__ == "__main__":
    # host = '171.103.221.226'
    host = '10.148.0.2'
    port = 5000  # replace with the actual port number you want to use
    app.run(debug=True, host=host, port=port)
