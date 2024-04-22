import firebase_admin
import firebase_admin.messaging
import database as db

def send_messages_to_everyone():
    registration_tokens = [token_tuple[0] for token_tuple in db.getFCMtokens()]

    message = firebase_admin.messaging.MulticastMessage(
        notification=firebase_admin.messaging.Notification(
            title='¡Aviso!',
            body='Debido al paso de la gabarra, el taller tendrá horario de 9:00 a 16:00. Disculpen las molestias.'
        ),
        tokens=registration_tokens,
    )

    response = firebase_admin.messaging.send_multicast(message)
    print('{0} messages can have been sent'.format(response.failure_count))
    print('{0} messages were sent successfully'.format(response.success_count))
