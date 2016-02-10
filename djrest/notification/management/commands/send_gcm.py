#Google Cloud Messaging
from gcm import GCM
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = 'send Google Cloud Messaging'

    def handle(self, *args, **options):
        gcm = GCM(settings.GCM_API_KEY)

        registration_ids = [settings.TEST_REG_ID, ]

        notification = {
            "title": "Test title",
            "message": "Tap here to start the update!",
            #"uri": "market://details?id=gcm.play.android.samples.com.gcmquickstart"
        }

        response = gcm.json_request(registration_ids=registration_ids,
                                    data=notification,
                                    priority='high',
                                    delay_while_idle=False)

        # Successfully handled registration_ids
        if response and 'success' in response:
            for reg_id, success_id in response['success'].items():
                print('Successfully sent notification for reg_id {0}'.format(reg_id))

        # Handling errors
        if 'errors' in response:
            for error, reg_ids in response['errors'].items():
                # Check for errors and act accordingly
                if error in ['NotRegistered', 'InvalidRegistration']:
                    # Remove reg_ids from database
                    for reg_id in reg_ids:
                        print("Removing reg_id: {0} from db".format(reg_id))