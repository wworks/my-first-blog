from gcm import *

gcm = GCM("AIzaSyAhXO4yU0eTXc3cfoMVvsy0WA3T8uTT_H4")
data = {'the_message': 'You have x new friends', 'param2': 'value2'}

reg_id = 'APA91bH6HIUlPVEBsMAmgVIDCrB6kwl8bdO6Oer_TrZEpOjolSsWIbMnuo8hmpBdvvTrr2srX1j70WSRZaSKrXIWHs89-_cTqRoKMETP3Nmo7EB6wt13A-HxYUfPRz_uqJ7nVzlZBNKw'

gcm.plaintext_request(registration_id=reg_id, data=data)

