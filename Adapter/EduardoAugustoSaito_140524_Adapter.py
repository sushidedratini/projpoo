from abc import ABC, abstractmethod


class INotificador(ABC):
    @abstractmethod
    def enviar(self, mensagem, destinatario):
        pass


class NotificadorEmail(INotificador):
    def enviar(self, mensagem, destinatario):
        print(f"Email\nPara: {destinatario}\nMensagem: {mensagem}")


class AdaptadorSMS(INotificador):
    def enviar(self, mensagem, destinatario):
        print(f"SMS\nPara: {destinatario}\nMensagem: {mensagem}")


class AdaptadorPush(INotificador):
    def enviar(self, mensagem, destinatario):
        print(f"PUSH\nPara: {destinatario}\nMensagem: {mensagem}")


class SMS():
    def __init__(self, adapter: AdaptadorSMS):
        self.adapter = adapter

    def enviarSMS(self, mensagem, numero):
        self.adapter.enviar(destinatario=numero, mensagem=mensagem)


class Push():
    def __init__(self, adapter: AdaptadorPush):
        self.adapter = adapter

    def enviarPush(self, mensagem, idDispositivo):
        self.adapter.enviar(destinatario=idDispositivo, mensagem=mensagem)


def main():

    # Envio via e-mail
    nf_email = NotificadorEmail()
    nf_email.enviar("Eduardo", "Hello World!")

    # Envio via SMS
    adapter_sms = AdaptadorSMS()
    sms = SMS(adapter=adapter_sms)
    sms.enviarSMS(numero="1291234-5678", mensagem="Teste envio SMS!")

    # Envio via PUSH
    adapter_push = AdaptadorPush()
    push = Push(adapter=adapter_push)
    push.enviarPush(idDispositivo="#123456", mensagem="Teste envio PUSH!")


if __name__ == '__main__':
    main()
