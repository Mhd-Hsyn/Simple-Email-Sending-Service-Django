from django.core.mail import EmailMultiAlternatives
from decouple import config
from django.conf import settings

# def send_message_to_admin(admin_email, message_obj):
#     subject = message_obj.subject
#     message = f"""
#     Name: {message_obj.name}
#     Email: {message_obj.email}
#     Phone: {message_obj.phone}
#     Subject: {message_obj.subject}
#     Message:
#     {message_obj.body}
#     """

#     # Send the email
#     msg = EmailMultiAlternatives(
#         subject= subject,
#         body= message,
#         from_email= settings.DEFAULT_FROM_EMAIL,
#         to= [admin_email]
#     )
#     # msg.attach_alternative(message, "text/html")
#     msg.send()
#     return True


def send_message_to_admin(admin_email, message_obj):
    subject = message_obj.subject
    plain_message = f"""
    Name: {message_obj.name}
    Email: {message_obj.email}
    Phone: {message_obj.phone}
    Subject: {message_obj.subject}
    Message:
    {message_obj.body}
    """

    html_message = f"""
    <h2>New Message Received</h2>
    <p><strong>Name:</strong> {message_obj.name}</p>
    <p><strong>Email:</strong> {message_obj.email}</p>
    <p><strong>Phone:</strong> {message_obj.phone}</p>
    <p><strong>Subject:</strong> {message_obj.subject}</p>
    <p><strong>Message:</strong><br>{message_obj.body}</p>
    """

    msg = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[admin_email]
    )
    msg.attach_alternative(html_message, "text/html")
    msg.send()
    return True




# def send_subadmin_welcome_credentials(email: str, password: str, name: str, company_name: str) -> bool:
#     try:
#         # logo_path = os.path.join(settings.MEDIA_ROOT, 'logo.png')
#         # logo_path = config("LOGO")
#         # template_path = os.path.join(
#         #     settings.BASE_DIR,
#         #     # "superadmin/emails/templates/subadmin_password_email.html",
#         #     "superadmin/emails/templates/company_welcome_email.html",
#         # )

#         # # Open and read the template HTML file
#         # with open(template_path, "r") as template_file:
#         #     html_content = template_file.read()

#         # # Replace placeholders with actual values
#         # html_content = html_content.replace("[password]", password)
#         # html_content = html_content.replace("[email]", email)
#         # html_content = html_content.replace("[name]", name)
#         # html_content = html_content.replace("[company_name]", company_name)
#         # # html_content = html_content.replace("{logo_path}", logo_path)

#         # Send the email
#         msg = EmailMultiAlternatives(
#             f"{company_name} Account Created, Welcome To Auto-COI", html_content, config("EMAIL_HOST_USER"), [email]
#         )
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
#         return True

#     except Exception as error:
#         print("error====>",error)
#         return False

