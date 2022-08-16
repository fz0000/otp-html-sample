import time

import pyotp

HTML_CODE = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <style>
        table, th, td {{
          border: 1px solid;
          border-collapse: collapse;
        }}


    </style>
</head>
<body>
<div>
    <table>
        <tr>
            <th>Accout</th>
            <th>Code</th>
        </tr>
        <tr>
            <td>{0}</td>
            <td>{1}</td>
        </tr>
    </table>
</div>
</body>
</html>
'''

def get_code(str_key):
    totp = pyotp.TOTP(str_key)
    return totp.now()


time.sleep(1)
account = 'account-name'
totp_account = get_code('account-key')

cur_html = HTML_CODE.format(account, totp_account)

with open('/path/to/index.html', 'w') as f:
    f.write(cur_html)
