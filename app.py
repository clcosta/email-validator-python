if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    from utils import *

    load_dotenv()
    
    EMAIL_ADRESS = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    app = EmailCheckerGui(
        sender=EMAIL_ADRESS,
        sender_password=PASSWORD,
        subject='Código Claudio Dev, Claudio'
    )