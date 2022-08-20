from naas_drivers import linkedin
import naas
import pandas as pd

LI_AT = "AQEDARCNSioDe6wmAAABfqF-HR4AAAF-xYqhHlYAtSu7EZZEpFer0UZF-GLuz2DNSz4asOOyCRxPGFjenv37irMObYYgxxxxxxx"
JSESSIONID = "ajax:12XXXXXXXXXXXXXXXXX"

# First message
FIRST_MESSAGE = "Hello there, nice to connect!"
naas.scheduler.add(cron="0 * * * *")
df_invitation = linkedin.connect(LI_AT, JSESSIONID).invitation.get_received() # change ID
df_invitation
def accept_new_contact(df):
    df_accept = pd.DataFrame()
    for index, row in df.iterrows():
        fullname = row.FULLNAME
        status = row.INVITATION_STATUS
        invitation_id = row.INVITATION_ID
        shared_secret = row.SHARED_SECRET
        if status == "PENDING":
            print(fullname)
            tmp_df = linkedin.connect(LI_AT, JSESSIONID).invitation.accept(invitation_id, shared_secret)
            df_accept = pd.concat([df_accept, tmp_df])
    return df_accept

df_accept = accept_new_contact(df_invitation)
df_accept
