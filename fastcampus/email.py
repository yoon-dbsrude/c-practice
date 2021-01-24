def send_email(from_email, to_email, subject, contents):
    print('From : '+ from_email)
    print('To : ' + to_email)
    print('Subject : ' + subject)
    print('Contents')
    print('-'*30)
    print(contents)
    print('-'*30)
    print('\n')
    print('*'*40)

my_email='yoon@email.com'

to_list={}
to_list['John']='John@email.com'
to_list['Jessi']='Jessiemail.com'
to_list['Park']='Park@email.com'
to_list['name']='Chris@email.com'


contents='''Thank you for inviting my page!
              - yoon -'''

for name in to_list.keys():
    to_email=to_list[name]
    subject = 'Dear. '+ name
    if '@' not in to_email:
        continue
    send_email(my_email, to_email , subject, contents)


