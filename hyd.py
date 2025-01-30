# from flask import  request, jsonify
# from flask_cors import CORS
# from groq import Groq
# from flask import Flask
# from flask_mail import Mail, Message
# app = Flask(__name__)
# CORS(app)
# mail = Mail(app)


# app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your SMTP server
# app.config['MAIL_PORT'] = 587  # Typically 587 for TLS
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'atharvapatange07@gmail.com'  # Your email username
# app.config['MAIL_PASSWORD'] = 'jyuaqdukerzipxad'  # Your email password
# app.config['MAIL_DEFAULT_SENDER'] = 'Atharva Patange <atharvapatange07@gmail.com>'  # Default sender email


# def send_professional_email(recipient_email, email_content):
#     try:
#         subject = 'Report of Deep Fake Fraud Case'
#         msg = Message(subject, recipients=[recipient_email])
#         msg.body = email_content
#         mail.send(msg)
#     except Exception as e:
#         raise RuntimeError(f"Failed to send email: {str(e)}")


# api_key_llama="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"  
# def get_mail_context(user_chat):
#     prompt=f"""You are an AI assistant tasked with drafting a professional email to a government authority regarding a case of deep fake fraud. Below is the chat history between the user and the chatbot, which outlines the user's experiences with deep fake issues related to news, images, or videos. 
# User Chat History:{user_chat}
# Based on the information provided in the chat history, please generate a concise and professional email that includes the following elements:
# 1. A brief introduction of the user and the purpose of the email.
# 2. A summary of the deep fake issues faced by the user, including any specific examples mentioned in the chat.
# 3. A request for assistance or action from the government authority regarding this matter.
# 4. A polite closing statement.

# The email should be clear, formal, and suitable for communication with a government official.
# """


#     client = Groq(api_key=api_key_llama)

#     response = client.chat.completions.create(
#         messages=[{"role": "user", "content": prompt}],
#         model="llama3-8b-8192", 
#         temperature=0.3
#     )
    
#     llama_response_content = response.choices[0].message.content
 
#     return llama_response_content


# @app.route('/mail', methods=['POST'])
# def mail():
#     try:
#         data = request.json
#         users_chat=data.get("user_chat")
#         context=get_mail_context(users_chat)
#         recipient_email='siddharamsutar23@gmail.com'
#         send_professional_email(recipient_email, context)

#         return jsonify({'message': 'Report sent successfully!'}), 200


#     except Exception as e:
#         return jsonify({'error': str(e)}), 500



# if __name__ == "__main__":
#     app.run(debug=True)





from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
from groq import Groq
import os

app = Flask(__name__)
CORS(app)
mail = Mail()

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'atharvapatange07@gmail.com'  # Your email username
app.config['MAIL_PASSWORD'] = 'brkivwmgbxrcorsu'  # Fetch password securely
app.config['MAIL_DEFAULT_SENDER'] = 'Atharva Patange <atharvapatange07@gmail.com>'  

mail.init_app(app)  # Initialize Mail

def send_professional_email(recipient_email, email_content):
    """ Sends a professional email using Flask-Mail """
    try:
        subject = 'Report of Deep Fake Fraud Case'
        msg = Message(subject, recipients=[recipient_email])
        msg.body = email_content
        mail.send(msg)
    except Exception as e:
        raise RuntimeError(f"Failed to send email: {str(e)}")

# Groq API Key (Consider storing securely instead of hardcoding)
api_key_llama = "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"

def get_mail_context(user_chat):
    """ Generates professional email content using Groq API """
    prompt = f"""You are an AI assistant tasked with drafting a professional email to a government authority regarding a case of deep fake fraud.
User Chat History: {user_chat}
Based on the provided chat history, generate a concise, formal, and professional email that includes:
1. A brief introduction of the user and the purpose of the email.
2. A summary of the deep fake issues faced by the user.
3. A request for assistance or action from the government authority.
4. A polite closing statement."""

    client = Groq(api_key=api_key_llama)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192",
        temperature=0.3
    )
    
    return response.choices[0].message.content

@app.route('/send-mail', methods=['POST'])  # Renamed route to avoid conflict
def send_mail_route():
    """ Flask route to receive email content and send an email """
    try:
        data = request.json
        users_chat = data.get("user_chat")
        
        if not users_chat:
            return jsonify({'error': 'Missing user_chat data'}), 400

        context = get_mail_context(users_chat)
        recipient_email = 'siddharamsutar23@gmail.com'
        send_professional_email(recipient_email, context)

        return jsonify({'message': 'Report sent successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
